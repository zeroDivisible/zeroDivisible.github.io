Title: Curl: PUT a file using HTTP basic auth
Date: 2014-01-07 15:57:18 +0000
Tags: curl, PUT, rest, note
Category: Blog

There is a myriad of ways how a file can be ``PUT`` to a RESTful webservice. If you need to send one using HTTP basic authentication, here is one way to do this using ``curl``:

```
curl -u "username:password" -X PUT -H "Content-Type: text/xml" -d "@filepath"  https://example.com/api/v1/putreceiver
```

Brief summary of options:

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

