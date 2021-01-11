import requests
from requests import get
import socket

def current_lan_ip():
    #current lan ip address of the user to be displayed in each page
    ipaddr = socket.gethostbyname(socket.gethostname())
    if ipaddr == "127.0.0.1":
        return "No internet your localhost is {}".format(ipaddr)
    else:
        return "Connected with the IP Address {}".format(ipaddr)

def current_wan_ip():
    #gets your current external/WAN IP address
    ip = get('https://api.ipify.org').text
    return 'My public IP address is: {}'.format(ip)
  