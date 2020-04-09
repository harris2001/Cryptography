message = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
hx = 0x0
key = 'ICE'
i = 0
s = ""
for c in message:
    s+=str(hex(ord(c)^ord(key[i%3]))[2:])
    i+=1
print(s)
