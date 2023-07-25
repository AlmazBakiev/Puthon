import random

array = []
for _ in range(10):
    array.append(random.randrange(0, 2))

counter = 0
for i in array:
    if i != 0:
        counter += 1

print(array)

if counter < len(array) - counter:
    print(counter)
else:
    print(len(array) - counter)
