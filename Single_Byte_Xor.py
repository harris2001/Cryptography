from pwn import *

with open('file.txt') as handle:
    cipher = handle.read()
    cipher = cipher.decode('base64')
    
    for i in range(1,256,1):
        message = pwn.xor(cipher,i)
        # find from strings an English Alphabet string
        if ('Flag' in message):
            print i
            print decipherd
            return
