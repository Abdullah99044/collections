
alle_dagen_van_de_week = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

de_werkdagen = ["maandag" , "dinsdag" , "woensdag" , "donderdag" , "vrijdag"]

de_weekenddagen = ["zaterdag", "zondag" ]

print("Alle dagen van de week zijn : ")
for i in alle_dagen_van_de_week:
    print(i)
print("**********")


print("De werkdagen zijn : ")
for x in de_werkdagen:
    print(x)  
print("**********")

print("De weekenddagen zijn : ")
for n in de_weekenddagen:
    print(n)
print("**********")

print("Alle dagen van de week in omgekeerde volgorde zijn :")
for l in reversed(alle_dagen_van_de_week):
    print(l)
print("**********")

print("De werkdagen in omgekeerde volgorde zijn:")
for m in reversed(de_werkdagen):
    print(m)  
print("**********")

print("De weekenddagen zijn : ")
for k in reversed(de_weekenddagen):
    print(k)
print("**********")