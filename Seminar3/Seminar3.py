
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

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
print('Seminar3 Task N4')
N = int(input('Введите преобразуемое в двоичный формат положительное десятичное число, результат строка! --> '))
N = CheckInputInt(N)
if N > 0:
    result = ''
    while N!=0:
        result = str(N%2) + result
        N //=2
print(result)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
print('Seminar3 Task N5')
N = int(input('Введите размер числа Фибоначчи '))
N = CheckInputInt(N)
if N > 0:
    f1 = f2 = 1
    listFibon = [f1, f2]
    for i in range(2, N):
        nF,f1,f2=f1+f2,f2,f1+f2 # избыточность nF можно заменить на f2 оставлено для понимания процесса
        listFibon.append(nF)
        #f1=f2
        #f2=nF
    print(listFibon)
    f1 = f2 =1
    for i in range(-N, 1):
        nF,f1,f2=f1-f2,f2,f1-f2 # избыточность nF можно заменить на f2 оставлено для понимания процесса
        listFibon.insert(0, nF)
        #f1=f2
        #f2 = nF
    print(listFibon)
else:
    print('Размер числа фибоначи должен быть положительным целым числом, не вверный ввод!')