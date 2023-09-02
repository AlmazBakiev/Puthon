counter_1 = int(input("Введите длину первого списка: "))
counter_2 = int(input("Введите длину второго списка: "))

list_1 = []
list_2 = []

for i in range(counter_1):
    list_1.append(input(f"Введите {i + 1} число: "))

for i in range(counter_2):
    list_2.append(input(f"Введите {i + 1} число: "))

a = set()

for i in list_1:
    a.add(i)

for i in list_2:
    a.add(i)

result = []
for i in a:
    result.append(i)

for i in range(0, len(result) - 1):
    for j in range(len(result) - 1):
        if result[j] > result[j + 1]:
            temp = result[j]
            result[j] = result[j + 1]
            result[j + 1] = temp

print(result)
