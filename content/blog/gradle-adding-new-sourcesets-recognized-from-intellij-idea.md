---
title: "Gradle: adding new sourceSets recognized from Intellij IDEA"
date: 2014-01-10T11:44:08-00:00
tags: ["gradle", "intellij-idea"]
categories: ["blog"]
draft: false
---

Some of the bigger projects which I've been working on recently have a bit more complex ``Gradle`` build scripts for them. One nifty thing which I thought that it would be worth documenting is how one of such projects is dealing with multi-module projects - and having a separate build target configured for running functional tests for it.From time to time having normal tests configured in my ``Gradle`` build files is not enough - especially when I'm dealing with big, multi-module projects.

### Gradle

The task was very easily achievable by adding a new ``sourceSet`` in Gradle

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

If we want to reference this source set from a gradle task (because we just added a definition for now), we can create a simple task:

```groovy
task funcTest(type: Test) {
   testClassesDir = sourceSets.funcTest.output.classesDir
   classpath = sourceSets.funcTest.runtimeClasspath
}
```

This ads a ``funcTest`` task (of type ``Test``) and configures classpath for it. Name doesn't need to match the name of previously created sourceSet as the biding part happens in ``sourceSets.funcTest.output.classesDir``. Invoking that task then is as simple as:

```
gradle funcTest
``` 

in the command line.

### IntelliJ Idea
So, now once Gradle is configured and will work on it's own, the next step was to make this work within IntellJ Idea. Idea has really good (though not flawless) integration with Gradle, but somehow it's not able to automatically detect that we had just defined new test sources. Fix is quite easy though and it requires:

1. Importing ``idea`` plugin in the build file (if it's not done yet):

```groovy
import 'idea'
```

2. Configuring the plugin to recognise directories with fuctional tests as test directories, not sources:

```groovy
idea {
   module {
      testSourceDirs += file('src/functest/java')
      testSourceDirs += file('src/functest/resources')
   }
}
```

And hopefully, now after either importing or refreshing the project using JetGradle it should get properly recognised.
