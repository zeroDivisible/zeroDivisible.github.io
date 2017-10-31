---
title: "Gradle: adding new sourceSets recognized from Intellij IDEA"
date: 2014-01-10T11:44:08-00:00
tags: ["gradle", "intellij-idea"]
categories: ["blog"]
draft: false
---

From time to time having normal tests configured in my ``Gradle`` build files is not enough - especially when I'm dealing with big, multi-module projects. There might be a need to either create a functional test or maybe test the behaviour of code while playing with new library. If unit tests are not enough in this case, it's better to create some kind of functional or integration one, especially that once it's done in a structured way, your colleagues will know where to go if they want to check something. 

### Gradle

In one project which I was working on, there was a need to add functionl tests - which is easilly doable in Gradle by introducing new sourceSets and new test task:

```groovy
sourceSets {

   // all other source sets

   funcTest { test ->
      compileClasspath = sourceSets.main.output + sourceSets.test.output + configurations.testRuntime
      runtimeClasspath = output + sourceSets.main.output + sourceSets.test.output + configurations.testRuntime

      java.srcDirs = ['src/functest/java']
      resources.srcDirs = ['src/functest/resources/']
   }
}

```

The above defines a source set called ``funcTest``, which references sources from ``src/functest/java`` in current project and resources from ``src/functest/resources``. It also is based on outputs from ``main`` & ``test`` sourceSets (which are defined earlier in a similar manner and not shown here).

This alone is almost sufficient for gradle - if we want to refernce this source set from a gradle task (because currently it just exists without doing anything), we can create one:

```groovy
task funcTest(type: Test) {
   testClassesDir = sourceSets.funcTest.output.classesDir
   classpath = sourceSets.funcTest.runtimeClasspath
}
```

This ads a ``funcTest`` Gradle task (of type ``Test``) and configures classpath for it. Name doesn't need to match the name of previously created sourceSet as the biding part happens in ``sourceSets.funcTest.output.classesDir``. If it matches though, it will easilly show the relationship between those two. As usual with Gradle, you can run new task by typing 

```
gradle funcTest
``` 

in the command line.

### IntelliJ Idea
So, now once Gradle is configured and will work on it's own, the next step is to make it work with Idea. Idea has really nice (though not flawless) integration with Gradle, but somehow it's not able to automatically deduct that we had just defined new test sources based on what we had just configured. Fix is quite easy though and it requires:

1. Importing ``idea`` plugin in the build file (if it's not done yet):

```groovy
import 'idea'
```

2. Configuring the plugin to recognise directories with fuctional tests as test directories, not source ones:

```groovy
idea {
   module {
      testSourceDirs += file('src/functest/java')
      testSourceDirs += file('src/functest/resources')
   }
}
```

And hopefully, now after either importing or refreshing the project using JetGradle it should get properly recognised.
