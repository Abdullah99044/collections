import random

def zak_met_mEnm( y):
    m =  "oranje", "blauw", "groen", "bruin" , "geel"
    zak_mEnm = {}
    for i in range(y):
        a = random.choice(m)
        n = random.randint(1 , 40)
        zak_mEnm[a] = n
        
    return  zak_mEnm





i = int(input("Antal kleurs : "))
print(zak_met_mEnm( i ))