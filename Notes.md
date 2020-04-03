# PRINTABLES
### Returns all the printable ASCII characters

\>\>\> printables = string.printable

\>\>\> print(printables)

\>\>\> 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ \n


# UNHEXLIFY
### Return the binary data represented by the hexadecimal string hexstr

\>\>\> a = "9a87ec645a32cab578b2"

\>\>\> b = binascii.unhexlify(a)

\>\>\> print(b)

\>\>\> '\x9a\x87\xecdZ2\xca\xb5x\xb2'

# BYTES
### Returns a bytes object which is an immmutable (cannot be modified) sequence of integers in the range 0 <=x < 256

\>\>\> string = "Key"

\>\>\> arr = bytes(string, 'ascii')

\>\>\> print(arr)

\>\>\> b'Key'

# ORD
### Retruns the integer value of an ascii character

\>\>\> ord('a')

\>\>\> 97

# HEXDIGEST
### Returns the result of a hashing function a a string of double length

\>\>\>hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()

\>\>\>'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2'
