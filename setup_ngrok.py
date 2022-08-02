from pyngrok import ngrok
import os
from os import system as sys

###########################################
sys("pip install pyngrok")

#########################################################
# Ngrok Token Api
##########################################################
token = input("[+] Enter The Token: ") 
############################################################


def files():
    ngrok.set_auth_token(token)
    public_url = ngrok.connect(8000, "http", bind_tls=True)
    url = str(public_url)
    print(url)


files()
