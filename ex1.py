def fact(n:int):
    for i in range(n-1, 0, -1):
        n *= i
    return n

print("Введите число: ", end='')
k = int(input())
s = []

for i in range(k, 0, -1):
    s.append(fact(i))

print(s)