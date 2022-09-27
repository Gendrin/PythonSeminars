
#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
#dayWeek = int(input('Введите число соответствующее дню недели'))

#Task number 1
print('Task 1')
dayWeek = int(input('Enter the number corresponding to the day of the week '))

if dayWeek == 6 or dayWeek == 7:
   print(f'- {dayWeek} -> yes')
elif dayWeek <= 0 or dayWeek < 6:
   print(f'- {dayWeek} -> no')
else:
     print(f'- {dayWeek} -> It\'s not a day of the week')

#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('Task 2 - 1')
insertString = input("Enter numbers separated by spaces X Y Z -> ")
arrString=insertString.split()

x =  int(arrString[0])
y =  int(arrString[1])
z =  int(arrString[2])

print(f'x = {x} y = {y} z = {z}')

fierst = not (x or y or z)
second = not x and not y and not z
result = fierst == second

if result == True:
   print(' ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z -> The true')
else:
   print(' ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z -> The false')

print('Task 2 - 2')

for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)

#3. Напишите программу, которая принимает на вход координаты точки (X и Y),
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
print('Task3')
x = int(input('Введите координату X '))
y = int(input('Введите координату Y '))

def CheckQuarter(x,y):   
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4
    
print(f'- x={x}; y={y}; -> {CheckQuarter(x,y)}')