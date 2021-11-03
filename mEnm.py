import random
mEnm = ["oranje ", "blauw ", "groen ", "bruin "]
zak_mEnm = []



def zak_met_mEnm(x , z):
    y = 10
    global zak_mEnm
    for i in range (z):
        a = random.choice(x)
        n = random.randint(1,y)
        m = (a + str(n))
        zak_mEnm.append(m)
    return  zak_mEnm

def sort_func():
    global zak_mEnm
    a = sorted(zak_mEnm)
    print(a)


i = int(input("Antal kleurs : "))
zak_met_mEnm(mEnm , i)
sort_func()

