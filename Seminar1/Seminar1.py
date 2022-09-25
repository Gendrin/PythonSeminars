
#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#dayWeek = int(input('Введите число соответствующее дню недели'))

#Task number 1
dayWeek = int(input('Insert number for week day '))

if dayWeek == 6 or dayWeek == 7:
   print(f'- {dayWeek} -> yes')
elif dayWeek <= 0 or dayWeek < 6:
   print(f'- {dayWeek} -> no')

#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
insertString = input("Insert string without probel X Y Z -> ")
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