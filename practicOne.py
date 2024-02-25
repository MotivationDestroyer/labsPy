import datetime

print("Привет, Мир!")
#Конец задания №1
print("\n")
typeNone = None
typeInt = 1
typeFloat = 1.52
typeStr = "Амогус"
typeList = [2,4,6]
typeTuple = "Один","Два","Три"
typeDict = {
    "name": "Олег",
    "year": "22"
}
typeSet = {"Один","Два","Три"}


print(typeNone)
print(typeInt)
print(typeFloat)
print(typeStr)
print(typeList)
print(typeTuple)
print(typeDict)
print(typeSet)
#(можно было бы сделать type1, type2 и выводить всё через цикл через type + i)

typeInt=float(typeInt)
typeInt=int(typeInt)

typeFloat=str(typeFloat)
typeFloat=float(typeFloat)

print(len(typeStr), len(typeTuple), len(typeDict), len(typeSet))
print(typeStr[0],typeStr[-1])
print(typeList[0], typeList[-1])
print(typeTuple[0], typeTuple[-1])

print("\n")

print(typeStr[1: -1])
print(typeList[1: -1])
print(typeTuple[1: -1])

print("\n")

print(typeDict.get("name"))

#Конец задания №2
print("\n")

typeBoolOne = True
typeBoolTwo = False
print(typeBoolOne,typeBoolTwo)
print("\n")
print(typeBoolOne and typeBoolTwo !=1)
print(typeBoolOne or typeBoolTwo ==0)
print(not typeBoolOne)
print("\n")

a=1
b=2
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print("\n")

print(1+1)
print(1-1)
print(1*1)
print(1/1)
print(1**1)
print(1//1)
print(1%1)

print("\n")
#Конец задания №3

c=int(input("Введите число на интервале [-100; 100]"))
if(c > 100 or c < -100):
    print("Число вышло за диапазон [-100; 100]")
elif(c<-50):
    print("Число меньше -50")
elif(c==-50):
    print("Число является -50")
elif(c<0 and c>-50):
    print("число меньше 0, но больше -50")
elif(c>50):
    print("Число больше 50")
elif(c==50):
    print("Число является 50")
elif(c>0 and c<50):
    print("число больше 0, но меньше 50")

print("\n")
#Конец задания №4

for i in range(10):
    print(i)

print("\n")

i=0
while i <10:
    print(i)
    i+=1
print("\n")

FIO="Воротилкин Олег Игоревич"
for char in FIO:
    print(char)
print("\n")

FriendList='нет друзей','Серега','Нет друзей'
for Friend in FriendList:
    print(Friend)
print("\n")

FriendDict={
    'Кирилл':   datetime.date(2001,6,10),
    'Сергей':   datetime.date(2001,12,10)
}


for FriendName, FriendDate in FriendDict.items():
 if FriendDate.month <= 8 and FriendDate.month >= 6:
  print("Родились летом:")
  print(FriendName + ":", FriendDate)
 elif FriendDate.month >= 1 and FriendDate.month <= 2 or FriendDate.month == 12:
  print("Родились зимой:")
  print(FriendName + ":", FriendDate)