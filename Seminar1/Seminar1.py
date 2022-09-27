import math
#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
#dayWeek = int(input('Введите число соответствующее дню недели'))

#Task number 1
def CheckInputInt(testInput):
    try:
        return int(testInput)
    except ValueError:
        print('Incorrect data entry')
        return None

        

print('Task 1 - Проверяем день недели!')

dayWeek = CheckInputInt(input('Enter the number corresponding to the day of the week '))
if dayWeek != None:
    if dayWeek == 6 or dayWeek == 7:
       print(f'- {dayWeek} -> yes')
    elif dayWeek <= 0 or dayWeek < 6:
       print(f'- {dayWeek} -> no')
    else:
         print(f'- {dayWeek} -> It\'s not a day of the week')

#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('Task 2 - Проверяем истинность утверждения')

for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)

#3. Напишите программу, которая принимает на вход координаты точки (X и Y),
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
print('Task3 - Проверка принадлежности четверти')
x = CheckInputInt(input('Введите координату X '))
y = CheckInputInt(input('Введите координату Y '))

def CheckQuarter(x,y):   
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

if (x and y != None) and (x !=0 and y!=0):    
    print(f'- x={x}; y={y}; -> {CheckQuarter(x,y)}')
else:
    print('Incorrect data entry')

#4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print('Task4 - отображаем диапазоны четверти')

def CheckDiapazonQuarter(x):   
    if x==1: return 'x > 0 and y > 0'
    elif x==2: return 'x < 0 and y > 0'
    elif x==3: return 'x < 0 and y < 0'
    elif x==4: return 'x > 0 and y < 0'
    else:
        return 'Incorrect number! DiapazonQuarter 1 -4'

numQuarter = CheckInputInt(input('Введите номер четверти -> '))
if numQuarter!=None:
    print(CheckDiapazonQuarter(numQuarter))

#5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
print('Task5 - находим расстояние между двумя точками')

def DistTwoPoint(x1,y1,x2,y2):
    return round(math.sqrt((x1-x2)**2 + (y1-y2)**2),2)

insertString = input("Enter numbers separated by spaces coords point number 1 x1, y1 -> ")
arrString=insertString.split()
x1 =  CheckInputInt(arrString[0])
y1 =  CheckInputInt(arrString[1])

insertString = input("Enter numbers separated by spaces coords point number 2 x2, y2 -> ")
arrString=insertString.split()
x2 =  CheckInputInt(arrString[0])
y2 =  CheckInputInt(arrString[1])

if x1 and y1 and x2 and y2 != None: 
    print(f'out -> {DistTwoPoint(x1,y1,x2,y2)}')

