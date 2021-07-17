# 4xxBypasser
un outil pour bypasser les code d'états HTTP négatif coté client ( 4xx )

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

Arguments/options disponibles :

- __Proxy__ : mettez des proxies http ( peut éviter des refus de connexion )
- __Params__ : ajoutez des paramètres si jamais le code d'états l'indique ( 401 par ex )
- __Path__ : le chemin qui renvoie le code 4xx

Format pour les args Proxy et Params :  

Params > {'p1':'hello', 'p2':'world'}

Proxy > {"http": "proxy"}
