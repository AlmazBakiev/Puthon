from random import randint

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)

low = int(input("Нижняя граница: "))
high = int(input("Верхняя граница: "))

lowBorder = 0
highBorder = 0

for i in range(N):
    if a[i] >= low:
        lowBorder = i
        break

for i in range(lowBorder + 1, N):
    if a[i] > high:
        highBorder = i
        break

print(f"{lowBorder}, {highBorder}")
