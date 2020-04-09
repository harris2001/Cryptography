import binascii

def get_score(phrase):
    phrase = bytes(phrase)
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    ans = 0
    for c in phrase:
        if (c<=ord('z') and c>=ord('a') or c==' '):
            ans += character_frequencies[chr(c)]
    return ans


ct = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
ct = bytes.fromhex(ct)
print(ct)
maxx = 0
smax = ''
lista = []
for i in range(256):
    s = []
    for c in ct:
        s.append(c^i)
    score = get_score(s)/len(s)
    lista.append((score,bytes(s)))

lista.sort()
for a,b in lista:
    print(b,a)
