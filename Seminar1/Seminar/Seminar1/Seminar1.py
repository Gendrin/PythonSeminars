#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#dayWeek = int(input('Введите число соответствующее дню недели'))

#Task number 1
dayWeek = int(input('Insert number for week day '))

if dayWeek == 6 or dayWeek == 7:
   print(f'- {dayWeek} -> yes')
elif dayWeek <= 0 or dayWeek < 6:
   print(f'- {dayWeek} -> no')
