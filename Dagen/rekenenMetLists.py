

def addAndDisplayLists(x , y):
    print("Add lists : ")
    for x , j in zip(x , y):
        print(j , "+" , x , "=", j + x)
    print("************")

def substractAndDisplayLists (x, y):
    print("Subtract lists : ")
    for x , j in zip(x , y):
        print(j , "-" , x , "=", j - x)
    print("************")

def multiplyAndDisplayLists (x, y):
    print("Multiply lists : ")
    for x , j in zip(x , y):
        print(j , "*" , x , "=", j * x)
    print("************")

def divideAndDisplayLists(x, y):
    print("Divide lists : ")
    for x , j in zip(x , y):
        print(j , "/" , x , "=", j / x)
    print("************")

    


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


addAndDisplayLists(list1 , list2)
substractAndDisplayLists (list1 , list2)
multiplyAndDisplayLists(list1 , list2)
divideAndDisplayLists(list1 , list2)
