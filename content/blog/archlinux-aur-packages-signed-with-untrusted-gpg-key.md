---
title: "Archlinux and AUR packages signed With untrusted GPG key"
date: 2015-01-18T18:38:28+00:00
tags: ["ansible", "vagrant", "gpg-agent", "gpg", "makepkg", "aur", "archlinux"]
categories: ["blog"]
draft: false
---


[Archlinux](https://www.archlinux.org/) is my main Linux distribution. It might have a steep learning curve, but once configured, it works like a charm. Just don't leave it unused for few months - once back, you'll you won't recognize the OS. Oh, and don't do updates just before whatever deadlines you have for the stuff you're working on.

Recently I've been mostly using CentOS & RedHat Linux at work, so I had been playing with those OSs at home too. In the end, I wanted to get back to Arch. The way how I did this usually was building my personal environment ("playground") based on Arch. I have a set of [Ansible](http://www.ansible.com/home) playbooks, which I could use both from within [Vagrant](https://www.vagrantup.com/) and later on a physical PC.

Everything was going smoothly, until I started installing packages from [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository). There's a whole back-story of the rationale behind my problem, but it boils down to the fact that in my Ansible playbooks I needed to be able to either automatically trust incoming GPG keys or disable that verification check.

Some quick googling returned the results suggesting that I'm not the only one hitting this issue:

- [Having pacman verify packages](https://www.archlinux.org/news/having-pacman-verify-packages/)
- [GnuPG 2.1 and the pacman keyring](https://www.archlinux.org/news/gnupg-21-and-the-pacman-keyring/)
- [Two PGP Keyrings for Package Management in Arch Linux](http://allanmcrae.com/2015/01/two-pgp-keyrings-for-package-management-in-arch-linux/)
- [Verify all the Packages](https://pierre-schmitz.com/verify-all-the-packages/)

I didn't had a chance to play with [GnuPG 2.1](https://www.gnupg.org/faq/whats-new-in-2.1.html) before, so instead of disabling the check, I opted for finding means of trusting the incoming keys automatically. (hey, it's a playground for now). The final solution which I had decided to go for required addition of two simple tasks to my Ansible role.

To use an example, if I wanted to install [``kafka`` from AUR](https://aur.archlinux.org/packages/kafka/) (which was failing, because I didn't trust the keys used to sign that package). To trust those keys automatically form within Ansible role, I came with this monstrosity:

```
- name: import gpg keys
  sudo: yes
  sudo_user: "{{ makepkg_nonroot_user }}"
  command: gpg --recv-key {{ item }}
  with_items:
    - 865187967F1183BD
    - 14B7C839C4F7D536A7BC9CAB865187967F1183BD

- name: trust required gpg keys
  sudo: yes
  sudo_user: "{{ makepkg_nonroot_user }}"
  command: printf 'trust\n5\ny\nquit\n' | gpg --no-permission-warning --command-fd 0 --edit-key 14B7C839C4F7D536A7BC9CAB865187967F1183BD
```

By using ``sudo: yes`` and setting the user to the one stored in ``makepkg_nonroot_user`` variable, I'm stating that the task is being run as the non-root user who will later be used to install specific package. Command in second step is saying that I'm giving ultimate trust to specified key (only do so if you really trust the key!). It uses piping of input to standard ``gpg`` [``edit-key``](https://www.gnupg.org/gph/en/manual/r899.html) command, with the actions being read from standard input (``--command-fd 0`` sets file descriptor of command to ``0`` which is ``stdin``).

The mysterious command which we're passing:

```
trust
5
y
quit
```

was just an invocation of trusting a key, with highest level (5), confirming it with ``y`` and quitting the edit mode.
