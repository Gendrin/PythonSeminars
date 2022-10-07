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

def NotRepetitivelist(insertList):
    resultList = []
    for i in insertList:
        count = insertList.count(i)
        if count == 1:
            resultList.append(i)
    return resultList

def CreateRandomSign():
    if randint(0,1)==0:
        return '-'
    else:
        return '+'
def CreateStringPoly(inNum):
    if inNum!=None and inNum!=0 and inNum > 0:
        fierstList = CreateRandomList(0,9,inNum+1)
        print(f'Creating random List -> {fierstList}')
        i = 0
        resultString=''
        saveInNum=inNum
        inNum+=1
        flagZnak=False
        while i < len(fierstList):
            if fierstList[i]!=0 and i < saveInNum:
                inNum=inNum-1
                if flagZnak:
                    resultString += CreateRandomSign()+str(fierstList[i]) + '*x^' + str(inNum)
                else:
                    resultString += str(fierstList[i]) + '*x^' + str(inNum)
                    flagZnak=True
            else:
                inNum = inNum - 1
            if i == saveInNum:
                if fierstList[i]==0:
                    resultString +='=0'
                else:
                    resultString += CreateRandomSign()+str(fierstList[i]) + '=0'
            i+=1
        return resultString

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
print('Task2 Seminar N4')
insertNumber = CheckInputInt(input('Enter number for task N2: '))
print(f'Простые множетели числа {insertNumber} --> {CheckMnogNumber(insertNumber)}')

print('Task3 Seminar N4')
insertRangeList = CheckInputInt(input('Enter count number for list task №3: (numbers generated from 0..9 -> '))
fierstList = CreateRandomList(0,9,insertRangeList)
print(f'Creating random List -> {fierstList}')
print(f'Result List --> {NotRepetitivelist(fierstList)}')

print('Task4 Seminar N4 Fun')
insertString = input("Enter numbers separated by spaces -> ")
arrString=insertString.split()
for j in range(0,len(arrString)):
    inNumTsk4=CheckInputInt(arrString[j])
    resultString = CreateStringPoly(inNumTsk4)
    task4File = open("Task4.txt", "a")
    task4File.write(resultString + '\n')
    task4File.close
    print('writing in file Task4.txt -->'+resultString)


# 1. Формируем список коэффициентов 10 штук ф-ия
# 2. Формируем строку , первый К всегда положительный, следующие
# добавляют себе знак, если к =0 пропуск элемента.
# 3. Ф-ия формирующая знак.

#print(f'Простые множетели числа {saveNumber} --> {CheckMnogNumber(insertNumber)}')

#Источник: https://pythonpip.ru/osnovy/tochnost-python

# d = int(input('Введите точность числа Пи '))
# print(f'Число Пи с заданной точностью {d} равно {round(math.pi,d)}')
# test = []
# test = random.sample([1,2,3,4,5,6,7,8],2)
# print(test)
# print(random.sample([1,2,3,4,5,6,7,8],2))
