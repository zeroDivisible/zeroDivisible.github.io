---
title: "Using Emacs's ansi-term with ZSH"
date: 2015-01-04T20:47:00-00:00
tags: ["emacs", "zsh"]
categories: ["blog"]
draft: false
---


If instead of Bash you're using ZSH and you somehow decided to be even more hipster, you can try using ZSH from within Emacs. There are multiple terminal emulators accessible inside Emacs, but for me, when I had been running the whole setup on OSX, neither of them didn't play nicely with [ANSI escape codes](http://en.wikipedia.org/wiki/ANSI_escape_code). Solution which worked for me was described [on StackOverflow](http://stackoverflow.com/a/8920373/126781) and to work, required me to:

* add the following snippet somewhere in the configuration file

```
;; Use Emacs terminfo, not system terminfo
(setq system-uses-terminfo nil)
```

* obtain a copy of ``eterm-color.ti`` (one is available on [Apple's opensource website](http://opensource.apple.com/source/emacs/emacs-70/emacs/etc/e/eterm-color.ti?txt), saving it somewhere (i.e. ``/tmp/eterm-color.ti``

* run [tic](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/tic.1m.html), pointing it to newly saved file

```
tic -o /usr/share/terminfo /tmp/eterm-color.ti
```

After doing this, and starting new ``ansi-term`` (``M-x ansi-term``), ANSI escape codes were properly honored.
