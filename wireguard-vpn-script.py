import os
import time
import sys
from requests import get

ip = get('https://api.ipify.org').text

print('connecting to ssh of the vpn')
os.system('telnet (port) (your vps ip')
print('now connecting to vpn')
os.system('sudo wg-quick up wg0-client')
print('vpn is now connected!')
time.sleep(1)
print('now checking if ip has changed')
time.sleep(1)
print('My IP is: {}'.format(ip))
print('double checking if the vpn is actually connected by using wg')
time.sleep(1)
os.system('sudo wg')
