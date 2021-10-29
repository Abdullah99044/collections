import random

def spelProgramma(spelList , min , max):
    for i in range(min , max):
        print(random.choice(spelList))

SpelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet' , 'Cluedo']

max = int(input("Maximaal aantal spellen is : "))
min = int(input("Minimaal   aantal spellen is  : "))

spelProgramma(SpelList , max , min)