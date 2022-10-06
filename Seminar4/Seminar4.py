import math,random
import decimal
from decimal import Decimal
from random import randint
from random import sample
decimal.getcontext().prec=24

def CheckInputInt(testInput):
    try:
        return int(testInput)
    except ValueError as Err:
        print(f'Incorrect data entry -> {Err}')
        return None

def CalcAccuracy (inNum,inAcc):
    if inAcc.replace(".", "", 1).isdigit() and inNum.replace(".", "", 1).isdigit():
        inNum = Decimal(inNum)
        inNum = inNum.quantize(Decimal(inAcc))
        return inNum
    else: return False

def CheckMnogNumber(checkNumber):
    mnogNumber = 2 #Первый простой множитель
    resultList = []
    saveNumber=checkNumber
    while mnogNumber<= checkNumber:
        if checkNumber%mnogNumber == 0:
            resultList.append(mnogNumber)
            checkNumber//=mnogNumber
            mnogNumber = 2
        else:
            mnogNumber+=1
    return resultList

def CreateRandomList(fromInt, toInt,quantity):
    generateList = []
    for i in range(quantity):
        listNumber=randint(fromInt,toInt)
        generateList.append(listNumber)
    return generateList

print('Task1 Seminar N4')
#Вычислить число c заданной точностью d
inNumTsk1 = input("Enter a real number: -> ")
inAccTsk1 = input("Enter the required accuracy '0.0001': -> ")
result = CalcAccuracy(inNumTsk1,inAccTsk1)
print(result)
if result:
    print(result)
else: print('Accuracy not correct enter!')

#2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
insertNumber = CheckInputInt(input('Enter number for task N2: '))
print(f'Простые множетели числа {insertNumber} --> {CheckMnogNumber(insertNumber)}')

print('Task №3')
insertRangeList = CheckInputInt(input('Enter count number for list task №3: (numbers generated from 0..9 -> '))
print(CreateRandomList(0,9,insertRangeList))
#print(f'Простые множетели числа {saveNumber} --> {CheckMnogNumber(insertNumber)}')

#Источник: https://pythonpip.ru/osnovy/tochnost-python

# d = int(input('Введите точность числа Пи '))
# print(f'Число Пи с заданной точностью {d} равно {round(math.pi,d)}')
# test = []
# test = random.sample([1,2,3,4,5,6,7,8],2)
# print(test)
# print(random.sample([1,2,3,4,5,6,7,8],2))
