import math,random
import decimal
from decimal import Decimal
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




#Источник: https://pythonpip.ru/osnovy/tochnost-python

# d = int(input('Введите точность числа Пи '))
# print(f'Число Пи с заданной точностью {d} равно {round(math.pi,d)}')
# test = []
# test = random.sample([1,2,3,4,5,6,7,8],2)
# print(test)
# print(random.sample([1,2,3,4,5,6,7,8],2))
