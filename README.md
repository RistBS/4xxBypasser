# 4xxBypasser
a tool to bypass negative HTTP status codes on the client side (4xx)

Liscence : [MIT license](LICENSE)

Creator
=
[![Devs](https://img.shields.io/badge/Made_By-RistBS-blue.svg)]() 
-
<img src="https://contributors-img.web.app/image?repo=RistBS/GeckoSec" />

Installation :
=
    git clone https://github.com/RistBS/4xxBypasser
    cd 4xxBypasser && sudo pip3 install -r requirements.txt
    sudo python3 4xxbypasser.py

![](https://imgur.com/46hyY15.png)

Arguments / options available:
-
- __Proxy__: put http proxies (can avoid connection refusals)
- __Params__: add parameters if ever the status code indicates it (401 for example)
- __Path__: the path that returns the 4xx code


Format for the args Proxy et Params :  
-
Params > {'p1':'hello', 'p2':'world'}

Proxy > {"http": "proxy"}



Nginx Alias Traversal Attack :
=
Vulnerable code :
```nginx
location /admin {
    alias /var/www/site/data;
}
```
URL with a Payload : http://site.com/admin../<path/file>
-
<path/file> = a directory² from /site and a file located in this directory²

