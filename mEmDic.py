import random
zak_mEnm = {}

def zak_met_mEnm( y):
    m =  "oranje", "blauw", "groen", "bruin" , "geel"
    global zak_mEnm
    for i in range(y):
        a = random.choice(m)
        n = random.randint(1 , 40)
        zak_mEnm[a] = n
        
    return  zak_mEnm


def sort_func():
    global zak_mEnm
    x = zak_mEnm.items()
    a = sorted(x)

    return a




i = int(input("Antal kleurs : "))

zak_met_mEnm(i)
print(sort_func())


