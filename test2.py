import requests
from requests import get
import socket
import re
import json

def current_lan_ip():
    #current lan ip address of the user to be displayed in each page
    ipaddr = socket.gethostbyname(socket.gethostname())
    if ipaddr == "127.0.0.1":
        print("No internet your localhost is "+ ipaddr)
    else:
        print("Connected with the IP Address " + ipaddr)

def current_wan_ip():
    #gets your current external/WAN IP address
    ip = get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(ip))

def filter(repls, str):
    #ensures http://, https://, and www. are filtered out for user_result method
    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                  lambda k: repls[k.group(0)], str)      

def user_result(f_site):
    #getting results on website uptime/info
    try:
        r = requests.get('http://{}'.format(f_site))
        print(r.headers['server'])
        print(r.headers['Last-Modified'])
        print(r.status_code)
    except KeyError:
        print('N/A')
        return

if __name__ == '__main__':
    current_lan_ip()
    current_wan_ip()
    repls = {'http://': '', 'https://': '', 'www.': ''}
    website = input("Website: ")
    print(filter(repls, website))
    f_site = filter(repls, website)
    user_result(f_site)