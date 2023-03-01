# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
n = int(input())
lst = []
for i in range(n):
    a = int(input())
    lst.append(a)
x = int(input())
diff_min = abs(x-lst[0])
item = lst[0]
for i in lst:
    diff = abs(x-i)
    if diff < diff_min:
        diff_min = diff
        item = i
print(item)

    