A=[0] * int(input("Введите размер массива: "))
delitel = delimoe = q = 0
print("Заполните массив: ")
for i in range(len(A)):
    q = input()
    A[i] = None if q =="null" else int(q)
    if (A[i] is not None and A[i]>0):
        delitel += 1
        delimoe += int(A[i])
print(delimoe / delitel if delitel != 0 else "В массиве нет положительных чисел")
