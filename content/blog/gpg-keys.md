---
title: "GPG Keys"
date: 2014-01-07T09:46:37-00:00
tags: ["gpg", "keys"]
categories: ["blog"]
draft: false
---

I didn't have much chances to work with GPG - and when I usually do, it's to communicate with third-party services, when exchanging encrypted files. Usually keys which I'm using are being delivered to me - but especially when developing (& testing), I have a need to get back to the command line and somehow generate a key for myself. Each time when doing this, instead of reaching to `man`, I thought that I may document the command on this blog:

## Generate GPG Key
```
gpg --gen-key
```

### List GPG Keys
```
gpg --list-keys
```

### Import GPG Key
```
# public key
gpg --import ~/public_key.gpg

# secret key
gpg --allow-secret-key-import --import ~/secret_key.gpg
```


### Export GPG Key
```
# public key
# AAAAAA being the ID of the key from the command listing keys
gpg --output exported_key_pub.gpg --armor --export AAAAAA

# secret key
# AAAAAA being the ID of the key from key command listing keys
gpg --output exported_key_sec.gpg --armor --export-secret-key AAAAA
```
