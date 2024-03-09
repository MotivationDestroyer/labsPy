import random
def funct():
    print("Привет, мир!")
funct()

def funct2(name):
    print(name)
funct2("Oleg")

def funct3(a,b,c):
    d=0
    d=(b^2)-4*a*c
    return d
print(funct3(1,2,3))

def funct4():
    Fname =" "
    Lname=" "
    Fname = input("Введите имя ")
    Lname = input("Введите фамилию ")
funct4()

def funct5(num):
    if(num >33):
        print("Указано неправильное число!")
    else:
        return chr(num + ord('а'))
print(funct5(6))

#Конец задания 6
        
def funct6():
    Fname="Олег"
    Mname="Игоревич"
    Lname="Воротилкин"
    FullName=Lname + " " + Fname + " " + Mname
    print(len(FullName))
    print(FullName)
    print(Fname)
    print(FullName.upper())
    print(FullName.split())
funct6()

#Конец задания 7

def funct7():
    spisokType=[None, 1, 2.3, 'str', ['a', 'b', 'c'], (1, 2, 3), {'key': 'value'}]
    for spisok in spisokType:
        print(type(spisok))
    spisokType.pop()
    Fname="Олег"
    Mname="Игоревич"
    Lname="Воротилкин"
    FullName = Fname + Mname + Lname
    i=0
    spis=[]
    resultSpis=''
    for spisok in FullName:
        spis.append(FullName[i])
        i+=1
    
    print(resultSpis.join(spis))

    index=0
    while index <= len(FullName )-1:
        print(FullName[index] + ' - ' + str(index))
        index +=1
    print(FullName.find("а"))

funct7()

#Конец задания 8

def funct8(start = 0, end = 100):
    return random.randrange(start // 2, end // 2) * 2 + 1
 
print(funct8())

#Конец задания 9

def funct9(firstNum, secondNum):
    if(firstNum and secondNum != 0):
        return firstNum / secondNum 
    else:
        print("одно из чисел = 0")
print(funct9(2,1))

#Конец задания 10