
import random
def CheckInputInt(testInput):
    try:
        return int(testInput)
    except ValueError:
        print('Incorrect data entry')
        return None


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
print('Seminar3 Task N1')
insertString = input("Enter numbers list separated by spaces -> ")
arrString = insertString.split()
arrIntDigits = []
# check input variable
flagInsertData = True
for numI in arrString:
    if CheckInputInt(numI) == None:
        flagInsertData = False
    else:
        arrIntDigits.append(CheckInputInt(numI))
sumNechetDigitList = 0
if flagInsertData:
    for i in range(len(arrIntDigits)):
        if i % 2 != 0:
            sumNechetDigitList += arrIntDigits[i]
    print(f'{arrIntDigits} -> {sumNechetDigitList}')

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй
# и предпоследний и т.д.
print('Seminar3 Task N2')
N = input("Enter long create random list -> ")
N = CheckInputInt(N)
if N != None:
    numList = []
    resultMultiplecsingList = []
    print('Create random list N1 -> ')
    for i in range(N):
        numList.append(random.randint(0, 9))
    print(numList)
#умножаем пары
    if N%2!=0:
        rangeMult = N//2+1
    else:
        rangeMult = N//2
    j=N-1
    for i in range(rangeMult):
        resultMultiplecsingList.append(numList[i]*numList[j])
        j-=1
    print(resultMultiplecsingList)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Осталось добавить формирование рандом списка
print('Seminar3 Task N3')

lst = [1.1, 1.2, 3.1, 5, 10.01]

new_lst = [round(i%1.0,2) for i in lst if i%1!=0]
print(new_lst, '=>', max(new_lst) - min(new_lst))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
print('Seminar3 Task N4')

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
print('Seminar3 Task N5')