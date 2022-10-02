
import random
from random import sample

def CheckInputInt(testInput):
    try:
        return int(testInput)
    except ValueError as Err:
        print(f'Incorrect data entry -> {Err}')
        return None
def CreateRandomList(rangeList):
    result = sample(range(rangeList*2), rangeList)
    print(result,end=' ')
    return result

def CreateRandomListU(rangeList):
    result = []
    for i in range(rangeList):
        result.append(round(random.uniform(0, 9), 2))
    print(result, end=' ')
    return result

def SumOddDigits(listForSum):
    result=0
    for i in range(1,len(listForSum),2):
        result+=listForSum[i]
    return result

def FindSumPair(taskList):
    if len(taskList)%2!=0:
        rangeMult = len(taskList) // 2 + 1
    else:
        rangeMult = len(taskList) // 2
    j=len(taskList)-1
    result = []
    for i in range(rangeMult):
        if i != j:
            result.append(taskList[i]*taskList[j])
        else:
            result.append(taskList[i])
        j-=1
    return result

def FindRaznOdd(taskListOdd):
    listOddMinZero = [round(i % 1.0, 2) for i in taskListOdd if i % 1 != 0]
    return round(max(listOddMinZero) - min(listOddMinZero), 2)

def BinFormatGo(number):
    binList = []
    if number > 0:
        while number!=0:
            binList.insert(0,number%2)
            number //=2
    return binList

def CreateListFibonachi(number):
    if number > 0:
        f1 = f2 = f3 = f4 = 1
        resultList = [1,1]
        for i in range(-1,number):
            f1,f2=f2,f1+f2
            if i < number-3:
                resultList.append(f2)
            f3,f4=f4,f3-f4
            resultList.insert(0,f4)
        return resultList
    else:
        print('Размер числа фибоначи должен быть положительным целым числом, не вверный ввод!')

# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.

print('Seminar3 Task N1')
rangeTsk1 = CheckInputInt(input("Enter range list for Task1 -> "))
if rangeTsk1 != None:
    tsk1List = CreateRandomList(rangeTsk1)
    print(f' -> {SumOddDigits(tsk1List)}')

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй
# и предпоследний и т.д.
print('Seminar3 Task N2')
rangeTsk2 = CheckInputInt(input("Enter range list for Task2 -> "))
if rangeTsk2 != None:
    tsk2List = CreateRandomList(rangeTsk2)
    print(f' --> {FindSumPair(tsk2List)}')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Осталось добавить формирование рандом списка
print('Seminar3 Task N3')
#lst = [1.1, 1.2, 3.1, 5, 10.01]
rangeTsk3 = CheckInputInt(input("Enter range list for Task3 -> "))
if rangeTsk3 != None:
    tsk3List = CreateRandomListU(rangeTsk3)
    print(f' --> {FindRaznOdd(tsk3List)}')

print('Seminar3 Task N4')
numberTask4 = int(input('Введите преобразуемое в двоичный формат положительное десятичное число, результат список! --> '))
numberTask4 = CheckInputInt(numberTask4)
if numberTask4 != None:
    print(f'{numberTask4} --> {BinFormatGo(numberTask4)}')

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
print('Seminar3 Task N5')
numberFibonachi=int(input('Введите размер числа Фибоначи '))
numberFibonachi=CheckInputInt(numberFibonachi)
if numberFibonachi != None:
    print(f'{numberFibonachi} --> {CreateListFibonachi(numberFibonachi)}')
