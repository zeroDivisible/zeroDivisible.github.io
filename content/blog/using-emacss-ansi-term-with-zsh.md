---
title: "Using Emacs's ansi-term with ZSH"
date: 2015-01-04T20:47:00-00:00
tags: ["emacs", "zsh"]
categories: ["blog"]
draft: false
---


Emacs has a million and one shells which you can run interactively from within the editor. When my login shell was set to ZSH though - and I was running Emacs on OS X, none of the terminal emulators built into Emacs was could display [ANSI escape codes](http://en.wikipedia.org/wiki/ANSI_escape_code) correctly. Solution which worked for me was described [on StackOverflow](http://stackoverflow.com/a/8920373/126781) and required:

* adding the following snippet somewhere in the init config:

```
;; Use Emacs terminfo, not system terminfo
(setq system-uses-terminfo nil)
```

* obtaining a copy of ``eterm-color.ti`` (one is available on [Apple's opensource website](http://opensource.apple.com/source/emacs/emacs-70/emacs/etc/e/eterm-color.ti?txt), saving it somewhere (i.e. ``/tmp/eterm-color.ti``

* running [tic](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/tic.1m.html), pointing it to newly saved file

```
tic -o /usr/share/terminfo /tmp/eterm-color.ti
```

After doing this, and starting new ``ansi-term`` (``M-x ansi-term``), ANSI escape codes were properly displayed.
