# coding=windows-1251
import random


# Метод проверки целого числа
def CheckInputInt(testInput):
    try:
        return int(testInput)
    except ValueError:
        print('Incorrect data entry')
        return None


# Метод проверки ввода вещественного числа
def CheckInputFloat(testInput):
    try:
        return float(testInput)
    except ValueError:
        print('Incorrect data entry')
        return None


# Метод поиска суммы цифр входящих в целое число
def findSumDigit(chekDidit):
    sumDigit = 0
    while chekDidit != 0:
        if chekDidit < 10:
            sumDigit += chekDidit
        else:
            sumDigit += chekDidit % 10
        chekDidit = chekDidit // 10
    return sumDigit


# Метод поиска суммы цифр в вводимой строке
def checkSumInDigitString(checkString):
    result = 0
    for simbol in checkString:
        if simbol != '.' and simbol != '-':
            result += CheckInputInt(simbol)
    return result


# Числовое решение задачи N1 (до 4х цифр после запятой)
print('Task 1 seminar 2 fierst')
inputString = input('Enter number >> ')
inputDigit = CheckInputFloat(inputString)

if inputDigit != None:
    intPast = int(inputDigit)
    floatPast = round(inputDigit % 1, 4)
    # Обработка целой части числа
    sumDigit = 0
    sumDigit += findSumDigit(intPast)
    # Обработка дробной части числа
    floatPast = int(floatPast * 10000)
    sumDigit += findSumDigit(floatPast)
    print(f'Rezult >> {sumDigit}')

# Строковое решение задачи N1
print('Task 1 seminar 2 second')
inputString = input('Enter number >> ')
if CheckInputFloat(inputString) != None:
    print(f'Rezult >> {checkSumInDigitString(inputString)}')
else:
    print('Incorrect data entry')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
print('Task 2')
inputDigit = input('Enter integer digit ')
inputDigit = CheckInputInt(inputDigit)
if inputDigit != None:
    factorial = 1
    for i in range(inputDigit):
        i = i + 1
        factorial = i * factorial
        print(factorial, end=" ")
    print()

# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

print('Task 3')
insertNum = input('Enter number list >> ')
insertNum = CheckInputInt(insertNum)
if insertNum != None:
    numList = []
    for i in range(1, insertNum + 1):
        numList.append(round((1 + 1 / i) ** i))
    print(f'n={insertNum}:{numList} -> {sum(numList)}')

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
print('Task 4')

N = input('Enter number for create list [-N,N] >> ')
N = CheckInputInt(N)
if N != None:
    numList = []
    for i in range(-N, N + 1):
        numList.append(i)
    print(numList)

    positionOne = int(input('Enter positionOne numbers list >> '))
    positionTwo = int(input('Enter positionTwo numbers list >> '))

    if positionOne < len(numList) and positionOne > 0 and positionTwo < len(numList) and positionTwo > 0:
        print(numList[positionOne - 1] * numList[positionTwo - 1])
    else:
        print('No correct entering position list!')

# 5 Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
print('Task N5')
N = input('Enter number for create list [0,N] >> ')
N = CheckInputInt(N)
if N != None:
    numList = []
    for i in range(N):
        numList.append(i)
    print(f'-> {numList}')

    for i in range(N):
        randomIndex = random.randrange(N)
        tempNumber = numList[i]
        numList[i] = numList[randomIndex]
        numList[randomIndex] = tempNumber
    print(f'-> {numList}')
