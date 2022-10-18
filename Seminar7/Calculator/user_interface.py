import mod_control as mc
from os import system

def StartRationalMenu():
    #system('clear')
    print('Operations rational number:\n')
    print('1 - sum Сложение\n') # Сложение
    print('2 - sub Вычитание\n') # Вычитание
    print('3 - mul Умножение\n') # Умножение
    print('4 - div Деление\n') # Деление
    print('5 - pow Возведение в степень\n') # Возведение в степень
    print('6 - sqrt Квадратный корень\n') # Квадратный корень
    print('0 - previos menu\n')
    second = input()
    if second.isdigit():
        chk=int(second)
        if chk==1:
            mc.Operation(11)
            temp = input('Нажмите ввод для продолжения')
            StartRationalMenu()
        elif chk==2:
            mc.Operation(12)
            temp = input('Нажмите ввод для продолжения')
            StartRationalMenu()
        elif chk==0: StartMenu()

def StartComplexMenu():
    #system('clear')
    print('Operations complex number:\n')
    print('1 - sum Сложение\n') # Сложение
    print('2 - sub Вычитание\n') # Вычитание
    print('3 - mul Умножение\n') # Умножение
    print('4 - div Деление\n') # Деление
    print('0 - previos menu\n')
    second = input()
    if second.isdigit():
        chk=int(second)
        if chk==1:
            mc.Operation(21)
            temp = input('Нажмите ввод для продолжения')
            StartComplexMenu()
        if chk==2:
            mc.Operation(22)
            temp = input('Нажмите ввод для продолжения')
            StartComplexMenu()
        elif chk==0: StartMenu()

def StartMenu():
    #system('clear')
    print("Calculator welcomes you!\n\n\n")
    print("Working with:\n")
    print("1 - rational\n")
    print("2 - complex\n")
    print("0 - exit\n")
    fierst = input()
    if fierst.isdigit():
        chk=int(fierst)
        if chk==1: StartRationalMenu()
        elif chk==2: StartComplexMenu()
        elif chk==0: return
        else:
            print('Выбрано не верное число')
            return