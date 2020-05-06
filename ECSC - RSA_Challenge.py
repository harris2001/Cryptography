    
    if(n1%sol1==0):
        trythis(n1//sol1, sol1)
    else:
        trythis(n1//sol2, sol2)

def trythis(p,q):
    phi = (p-1)*(q-1)
    d = modInverse(e,phi)
    m = str(hex(pow(ct,d,n1)))[2:]
    try:
        print(binascii.unhexlify(m))
    except:
        m = "0"+m
        print(binascii.unhexlify(m))
def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
    if (m == 1) :
        return 0
    while (a > 1) :                          
        q = a // m                                            
        t = m                                                     
        m = a % m 
        a = t 
        t = y                                                                                               
        y = x - q * y 
        x = t                                                                           
    if (x < 0) :
        x = x + m0 
    return x

for i in range(1000):
    #qs = diff_qs
    #ps = (i*diff_qs)+diff_ps
    #main(ps,qs)

    ps = diff_ps
    qs = (i*diff_ps)+diff_qs
    main(ps,qs)
