n = int(input("Введите количество элементов для первого множества: "))
set1 = set()
for i in range(n):
    element = input(f"Введите элемент {i+1} для первого множества: ")
    set1.add(element)
m = int(input("Введите количество элементов для второго множества: "))
set2 = set()
for i in range(m):
    element = input(f"Введите элемент {i+1} для второго множества: ")
    set2.add(element)
print("Первое множество:", set1)
print("Второе множество:", set2)

result = sorted(set1 & set2)
print(result)