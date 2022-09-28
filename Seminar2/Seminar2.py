# Метод проверки целого числа
def CheckInputInt(testInput):
    try:
        return int(testInput)
    except ValueError:
        print('Incorrect data entry')
        return None
# Метод проверки ввода вещественного числа
def CheckInputFloat(testInput):
    try:
        return float(testInput)
    except ValueError:
        print('Incorrect data entry')
        return None
# Метод поиска суммы цифр входящих в целое число
def findSumDigit(chekDidit):
    sumDigit = 0
    while chekDidit != 0:
        if chekDidit < 10:
            sumDigit += chekDidit
        else:
            sumDigit += chekDidit % 10
        chekDidit = chekDidit // 10
    return sumDigit
# Метод поиска суммы цифр в вводимой строке
def checkSumInDigitString(checkString):
    result=0
    for simbol in checkString:
        if simbol!='.' and simbol!='-':
            result+=CheckInputInt(simbol)
    return result
# Числовое решение задачи N1 (до 4х цифр после запятой)
print('Task 1 seminar 2 fierst')
inputString = input('Enter number >> ')
inputDigit=CheckInputFloat(inputString)

if inputDigit!=None:
    intPast = int(inputDigit)
    floatPast = round(inputDigit%1,4)
    # Обработка целой части числа
    sumDigit=0
    sumDigit+=findSumDigit(intPast)
    # Обработка дробной части числа
    floatPast = int(floatPast*10000)
    sumDigit+=findSumDigit(floatPast)
    print(f'Rezult >> {sumDigit}')

# Строковое решение задачи N1
print('Task 1 seminar 2 second')
inputString = input('Enter number >> ')
print(f'Rezult >> {checkSumInDigitString(inputString)}')




##old_list = ['1', '2', '3', '4', '5', '6', '7']
#old_list='123.45'
#new_list = []
#for item in old_list:
#    if item != ',' and item != '.':
#        new_list.append(int(item))
 
#print (new_list)
 
##[1, 2, 3, 4, 5, 6, 7]
#old_list = ['1', '2', '3', '4', '5', '6', '7']
#new_list = list(map(int, old_list))
#print (new_list)
 
#[1, 2, 3, 4, 5, 6, 7]