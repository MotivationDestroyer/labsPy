n= int(input("Введите размер массива: "))
A = [0] * n
delitel = 0
delimoe = 0
q = 0
print("Заполните массив: ")
for i in range(n):
    q=input()
    if(q == "null"):
        A[i] = None
    else:
        A[i] = int(q)
    if(A[i] is not None and A[i]>0):
        delitel = delitel + 1
        delimoe = delimoe + int(A[i])
if(delitel is not 0):
    print(delimoe / delitel)
else:
    print("В массиве нет положительных чисел")