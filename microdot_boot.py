#!/usr/bin/env python

import time
import sys
import socket
import microdotphat             

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.168.1.1', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

hostname = socket.gethostname()
ip_address = get_ip()

print(ip_address)

microdotphat.write_string(hostname, offset_x=0, kerning=False)
microdotphat.show()
time.sleep(1.5)

for i in hostname[6:]:
    microdotphat.scroll(amount_x=8)
    microdotphat.show()
    time.sleep(0.2)

time.sleep(1.5)

## PRINT IP ADDRESS
microdotphat.clear()
microdotphat.scroll_to(position_x=0, position_y=0)
microdotphat.write_string(ip_address, offset_x=0, kerning=False)
microdotphat.show()
time.sleep(1.5)

for i in ip_address[6:]:
    microdotphat.scroll(amount_x=8)
    microdotphat.show()
    time.sleep(0.2)

time.sleep(1.5)
