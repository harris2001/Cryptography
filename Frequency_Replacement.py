ct = "Cooking MC's like a pound of bacon"
ct = ct.lower()
lexicon = ['e','t','a','o','i','n','s','h','r','d','l','u','w','m','f','c','g','y','p','b','k','v','j','x','q','z']

pin = []

for i in range(26):
    pin.append(0)

freq = list(pin)
for i in ct:
    diff = ord(i)-ord('a')
    if(diff > 0):
        pin[diff]+=1

arr = []

for i in range(26):
    arr.append((pin[i],chr(i+ord('a'))))
    #print((pin[i],chr(i+ord('a'))))
    
arr.sort(reverse = 1)

mapping = []
count = 0
for a,b in arr:
    mapping.append((lexicon[count],b))
    count+=1
    print(a,b)
print(mapping)

s = ''
for i in ct:
    for a,b in mapping:
        if(i == b):
            s += a
            break
        
print(s)
            
