---
title: "Curl: PUT a File using HTTP Basic Auth"
date: 2014-01-07T15:57:18-00:00
tags: ["curl", "PUT", "REST", "note"]
categories: ["blog"]
draft: false
---


When testing a local webservice, I needed to upload a file, with HTTP Basic Authentication. Quick googling returned a cURL onliner, which got the job done:

```
curl -u "username:password" -X PUT -H "Content-Type: text/xml" -d "@filepath"  https://example.com/api/v1/putreceiver
```

Explanation of what exactly was passed as arguments:

```
# sets the username and pass for HTTP basic auth
-u "username:password"

# specifies the HTTP verb which we will use as the request type
-X PUT

# adds extra header for content type
-H "Content-Type: text/xml"

# attaches the file
-d "@filepath"

# address of the webservice
https://example.com/api/v1/putreceiver
```
