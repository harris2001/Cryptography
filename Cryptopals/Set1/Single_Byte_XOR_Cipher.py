import binascii
ct = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
ct = bytes.fromhex(ct)
print(ct)
for i in range(256):
    s = []
    for c in ct:
        s.append(c^i)
    print(bytes(s))
