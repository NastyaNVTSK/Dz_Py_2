import random

def max_berries(a):
     m = len(a)
     max_berries = 0

     for i in range(m):
         berries = a [i] + a [(i-1) % m] + a [(i+1) % m]
         max_berries = max(max_berries, berries)

     return max_berries


N = 10
a = [random.randint(1, 10) for _ in range(N)]
print(f"Урожайность грядки: {a}")

result = max_berries(a)
print(f"Максимальное число ягод, которое может собрать модуль: {result}")