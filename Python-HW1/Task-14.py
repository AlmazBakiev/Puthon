number = int(input("Введите число: "))

for i in range(100):
    if pow(2, i) > number:
        break
    print(pow(2, i), end=", ")
