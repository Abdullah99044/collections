import random

def zak_met_mEnm(x , y):
    z = 40
    zak_mEnm = []
    for i in range(y):
        a = random.choice(x)
        zak_mEnm.append([a])
        n = random.randint(1,z)
        zak_mEnm.append(n)
    return  zak_mEnm

mEnm = ["oranje", "blauw", "groen", "bruin"]

i = int(input("Antal kleurs : "))
print(zak_met_mEnm(mEnm , i ))