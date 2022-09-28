# coding=windows-1251
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

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
print('Seminar3 Task N2')
