
import mod_control as mc

def StartDivMenu():
    print('Operations:\n')
    print("1 - '/' Деление\n") # Сложение
    print("2 - '//' Целочисленное деление\n") # Вычитание
    print("3 - '%' Остаток от деления\n") # Умножение
    print('0 - previos menu\n')
    chk=input()
    if chk=='1' or chk=='2' or chk=='3':
        mc.Operation('3' + chk)
        temp = input('Нажмите ввод для продолжения')
        StartDivMenu()
    elif chk=='0': StartRationalMenu()

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
    chk=input()
    if chk=='1' or chk=='2' or chk=='3' or chk=='5' or chk=='6':
            mc.Operation('1' + chk)
            temp = input('Нажмите ввод для продолжения')
            StartRationalMenu()
    elif chk=='4': StartDivMenu()
    elif chk=='0': StartMenu()

def StartComplexMenu():
    #system('clear')
    print('Operations complex number:\n')
    print('1 - sum Сложение\n') # Сложение
    print('2 - sub Вычитание\n') # Вычитание
    print('3 - mul Умножение\n') # Умножение
    print('4 - div Деление\n') # Деление
    print('0 - previos menu\n')
    chk=input()
    if chk=='1' or chk=='2' or chk=='3' or chk=='4':
        mc.Operation('2' + chk)
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
    chk=input()
    if chk=='1': StartRationalMenu()
    elif chk=='2': StartComplexMenu()
    elif chk=='0': return
    else:
        print('Выбрано не верное число')
        return
