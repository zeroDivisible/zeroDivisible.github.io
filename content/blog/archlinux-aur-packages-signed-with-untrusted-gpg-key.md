---
title: "Archlinux and AUR packages signed With untrusted GPG key"
date: 2015-01-18T18:38:28+00:00
tags: ["ansible", "vagrant", "gpg-agent", "gpg", "makepkg", "aur", "archlinux"]
categories: ["blog"]
draft: false
---


[Archlinux](https://www.archlinux.org/) is a really interesting Linux distribution - and it's one of my favorite ones. It might have a steep learning curve, but once you dig into it, it will work like a charm. Unless you will switch to some distro and want to come back after an undefined period of time.

As recently I've been mostly using CentOS & RedHat Linux, I wanted to get back to Archlinux, just to spice things a little and see what's going on in with my favorite distro. The easiest way of gradually going back, was to build my personal dev environment ("playground") based on Arch. I had decided to create a set of [Ansible](http://www.ansible.com/home) playbooks, which I could then use both with [Vagrant](https://www.vagrantup.com/) to spin the env, and later use the same set of scripts to provision my laptop, once I will decide to switch the main OS to Arch once again (it's not a question of "if", only "when" :)).

Everything was going smoothly, except when I had started to install packages from [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository). There's a whole separate back-story of the rationale behind my problem, but it boils down to the fact that in my Ansible playbooks I needed to be able to either automatically trust incoming keys or disable that verification check.

Some background details can be found here:

- [Having pacman verify packages](https://www.archlinux.org/news/having-pacman-verify-packages/)
- [GnuPG 2.1 and the pacman keyring](https://www.archlinux.org/news/gnupg-21-and-the-pacman-keyring/)
- [Two PGP Keyrings for Package Management in Arch Linux](http://allanmcrae.com/2015/01/two-pgp-keyrings-for-package-management-in-arch-linux/)
- [Verify all the Packages](https://pierre-schmitz.com/verify-all-the-packages/)

I didn't had a chance to play with [GnuPG 2.1](https://www.gnupg.org/faq/whats-new-in-2.1.html) before, so instead of disabling the check, I opted for finding means of trusting the incoming keys automatically. (as this is just a dev env, for now). The final solution which I had decided to go for required addition of two simple tasks to my Ansible role.

To use an example, if I wanted to install [``kafka`` from AUR](https://aur.archlinux.org/packages/kafka/) (which was failing, because I didn't trust the keys used to sign that package), I needed to add:

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

By using ``sudo: yes`` and setting the user to the one stored in ``makepkg_nonroot_user`` variable, I'm stating that task is being run as the non-root user who will later be used to install specific package. Command in second step is saying that I'm giving ultimate trust to specified key (only do so if you really trust the key!). It uses piping of input to standard ``gpg`` [``edit-key``](https://www.gnupg.org/gph/en/manual/r899.html) command, with the actions being read from standard input (``--command-fd 0`` sets file descriptor of command to ``0`` which is ``stdin``).

The command which we're passing:

```
trust
5
y
quit
```

is just an invocation of trusting a key, with highest level (5), confirming it with ``y`` and quitting the edit mode.
