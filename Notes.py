printables=string.printable #returns all printable characters 
'''
>>>printables = string.printable
>>>printables
>>>0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ 
'''

binascii.unhexlify(byt) # Return the binary data represented by the hexadecimal string hexstr
'''
>>>a = "9a87ec645a32cab578b2"
>>>b = binascii.unhexlify(a)
>>>print(b)
>>>'\x9a\x87\xecdZ2\xca\xb5x\xb2'
'''
