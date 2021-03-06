def get_score(phrase):
    '''WIKIPEDIA
    letters = {
            'e': 12.702, 't': 9.356, 'a': 8.167, 'o': 7.507,
            'i': 6.966, 'n': 6.749, 's': 6.327, 'h': 6.094,
            'r': 5.987, 'd': 4.253, 'l': 4.025, 'u': 2.758,
            'w': 2.560, 'm': 2.406, 'f': 2.228, 'c': 2.202,
            'g': 2.015, 'y': 1.994, 'p': 1.929, 'b': 1.492,
            'k': 1.292, 'v': 0.978, 'j': 0.153, 'x': 0.150,
            'q': 0.095, 'z': 0.077, ' ':
            }
    bigrams = {
            'th': 1.52,       'en': 0.55,       'ng': 0.18,
            'he': 1.28,       'ed': 0.53,       'of': 0.16,
            'in': 0.94,       'to': 0.52,       'al': 0.09,
            'er': 0.94,       'it': 0.50,       'de': 0.09,
            'an': 0.82,       'ou': 0.50,       'se': 0.08,
            're': 0.68,       'ea': 0.47,       'le': 0.08,
            'nd': 0.63,       'hi': 0.46,       'sa': 0.06,
            'at': 0.59,       'is': 0.46,       'si': 0.05,
            'on': 0.57,       'or': 0.43,       'ar': 0.04,
            'nt': 0.56,       'ti': 0.34,       've': 0.04,
            'ha': 0.56,       'as': 0.33,       'ra': 0.04,
            'es': 0.56,       'te': 0.27,       'ld': 0.02,
            'st': 0.55,       'et': 0.19,       'ur': 0.02
            }
    '''
    #################PRACTICAL CRYTPOGRAPHY##############################

    monograms = {
            'A' :  8.55, 'K' :  0.81, 'U' :  2.68,
            'B' :  1.60, 'L' :  4.21, 'V' :  1.06,
            'C' :  3.16, 'M' :  2.53, 'W' :  1.83,
            'D' :  3.87, 'N' :  7.17, 'X' :  0.19,
            'E' : 12.10, 'O' :  7.47, 'Y' :  1.72,
            'F' :  2.18, 'P' :  2.07, 'Z' :  0.11,
            'G' :  2.09, 'Q' :  0.10, 'H' :  4.96,
            'R' :  6.33, 'I' :  7.33, 'S' :  6.73,
            'J' :  0.22, 'T' :  8.94, ' ' : 1.3000
    }
    bigrams = {
            'TH': 2.71,  'EN': 1.13,  'NG': 0.89,
            'HE': 2.33,  'AT': 1.12,  'AL': 0.88,
            'IN': 2.03,  'ED': 1.08,  'IT': 0.88,
            'ER': 1.78,  'ND': 1.07,  'AS': 0.87,
            'AN': 1.61,  'TO': 1.07,  'IS': 0.86,
            'RE': 1.41,  'OR': 1.06,  'HA': 0.83,
            'ES': 1.32,  'EA': 1.00,  'ET': 0.76,
            'ON': 1.32,  'TI': 0.99,  'SE': 0.73,
            'ST': 1.25,  'AR': 0.98,  'OU': 0.72,
            'NT': 1.17,  'TE': 0.98,  'OF': 0.71 
    }
    trigrams = {
            'THE' :  1.81,  'ERE' :  0.31,  'HES' :  0.24,
            'AND' :  0.73,  'TIO' :  0.31,  'VER' :  0.24,
            'ING' :  0.72,  'TER' :  0.30,  'HIS' :  0.24,
            'ENT' :  0.42,  'EST' :  0.28,  'OFT' :  0.22,
            'ION' :  0.42,  'ERS' :  0.28,  'ITH' :  0.21,
            'HER' :  0.36,  'ATI' :  0.26,  'FTH' :  0.21,
            'FOR' :  0.34,  'HAT' :  0.26,  'STH' :  0.21,
            'THA' :  0.33,  'ATE' :  0.25,  'OTH' :  0.21,
            'NTH' :  0.33,  'ALL' :  0.25,  'RES' :  0.21,
            'INT' :  0.32,  'ETH' :  0.24,  'ONT' :  0.20
    }
    words = {
            'THE' :  6.42,   'ON' :  0.78,   'ARE' :  0.47,
            'OF' :  2.76,   'WITH' :  0.75,   'THIS' :  0.42,
            'AND' :  2.75,   'HE' :  0.75,   'I' :  0.41,
            'TO' :  2.67,   'IT' :  0.74,   'BUT' :  0.40,
            'A' :  2.43,   'AS' :  0.71,   'HAVE' :  0.39,
            'IN' :  2.31,   'AT' :  0.58,   'AN' :  0.37,
            'IS' :  1.12,   'HIS' :  0.55,   'HAS' :  0.35,
            'FOR' :  1.01,   'BY' :  0.51,   'NOT' :  0.34,
            'THAT' :  0.92,   'BE' :  0.48,   'THEY' :  0.33,
            'WAS' :  0.88,   'FROM' :  0.47,   'OR' :  0.30
    }

    ######################################################################
    
    ans = 0
    p_or = phrase
    phrase = phrase.upper().strip()
    for i in phrase:
        if(i in monograms): 
            ans += monograms[i]

    for i in range(0, len(phrase)-2, 2):
        ss = (phrase[i]+phrase[i+1])
        if(ss in bigrams):
            ans += bigrams[ss]

    return ans

def main():
    array = []
    with open("challenge.txt") as data:
        for line in data:
            ff = line
            ct = bytes.fromhex(ff)
            for i in range(256):
                s = ""
                for c in ct:
                    s+=chr(c^i)
                score = get_score(s)
                if score>50:
                    array.append((score,s))

    array.sort()
    
    for a,b in array:
        print(b,a)

if __name__ == "__main__":
    main()
