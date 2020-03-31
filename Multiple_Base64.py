import base64

def clear(s):
    return s.replace('\n','').replace('\r','')

def find_eq(s):
    for i in s:
        if i == '=':
            return 1
    return 0

with open('keys.txt') as handle:
    keys = handle.read()
    b1 = 0
    s1 = ''
    s2 = ''
    for key in keys:
        if b1 ==0:
            s1 += key
        else:
            s2 += key
        if key == '=':
            b1 = 1
    s1 = clear(s1)
    s2 = clear(s2)
    
    while(1):
        s1 = base64.b64decode(s1)
        s2 = base64.b64decode(s2)
        print(s1,s2)
        if (find_eq(s1) == 0) or (find_eq(s2) == 0):
            break;
