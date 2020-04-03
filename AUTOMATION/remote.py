import hashlib
import pwn
from Crypto import *

def connect_to():
    print("Connecting to:")
    host = input("host:")
    port = input("")
    print(host, port)
    rec = input("Do you want to connect through SSL?(yes/no):")
    if(rec[0]=='y'):
        r = remote(str(host),int(port),ssl=True)
    else:
        r = remote(str(host),int(port))
    
def send(r,data):
    r.send(dat)

def recv(r):
    return r.recv()

def main():
    connect_to()
    
if __name__ == "__main__":
    main()
