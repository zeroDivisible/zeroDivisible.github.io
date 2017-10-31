---
title: "GPG Keys"
date: 2014-01-07T09:46:37-00:00
tags: ["gpg", "keys"]
categories: ["blog"]
draft: false
---

From time to time I have a need to work with GPG keys - (i.e. when dealing with third party interfaces and encrypting files to be send). Usually keys which I'm using are being delivered to me - but especially when developing (& testing), I have a need to go back to command line and use gpg from within it. As each time when I'm doing so, I have to either read ``man`` for ``GPG`` or use Google, I just thought that I will put some of the most common things which I'm using in the blog post. 

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

