import random

firstNumber = random.randrange(0, 1000)
secondNumber = random.randrange(0, 1000)

print(firstNumber)
print(secondNumber)
print()

sum = firstNumber + secondNumber
multiply = firstNumber * secondNumber

expectedFNum = 0
expectedSNum = sum

while True:
    if expectedFNum + expectedSNum == sum and expectedFNum * expectedSNum == multiply:
        break
    expectedFNum += 1
    expectedSNum -= 1

print(expectedFNum)
print(expectedSNum)
