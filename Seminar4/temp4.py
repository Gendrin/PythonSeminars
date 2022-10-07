from random import randint

def CheckInputInt(testInput):
    try:
        return int(testInput)
    except ValueError as Err:
        print(f'Incorrect data entry -> {Err}')
        return None

def CreateRandomList(fromInt, toInt,quantity):
    generateList = []
    for i in range(quantity):
        listNumber=randint(fromInt,toInt)
        generateList.append(listNumber)
    return generateList

def CreateRandomSign():
    if randint(0,1)==0:
        return '-'
    else:
        return '+'


print('Task4 Seminar N4')
#inNumTsk5 = int(input("Enter a real number: -> "))
insertString = input("Enter numbers separated by spaces -> ")
arrString=insertString.split()
for j in range(0,len(arrString)):
    inNumTsk5=CheckInputInt(arrString[j])
    if inNumTsk5!=None and inNumTsk5!=0 and inNumTsk5 > 0:
        fierstList = CreateRandomList(0,9,inNumTsk5+1)
        print(f'Creating random List -> {fierstList}')
        i = 0
        resultString=''
        saveInNum=inNumTsk5
        inNumTsk5+=1
        flagZnak=False
        while i < len(fierstList):
            if fierstList[i]!=0 and i < saveInNum:
                inNumTsk5=inNumTsk5-1
                if flagZnak:
                    resultString += CreateRandomSign()+str(fierstList[i]) + '*x^' + str(inNumTsk5)  # + CreateRandomSign()
                else:
                    resultString += str(fierstList[i]) + '*x^' + str(inNumTsk5)
                    flagZnak=True
            else:
                inNumTsk5 = inNumTsk5 - 1
            if i == saveInNum:
                if fierstList[i]==0:
                    resultString +='=0'
                else:
                    resultString += CreateRandomSign()+str(fierstList[i]) + '=0'
            i+=1
        print(resultString)

# 1. Формируем список коэффициентов 10 штук ф-ия
# 2. Формируем строку , первый К всегда положительный, следующие
# добавляют себе знак, если к =0 пропуск элемента.
# 3. Ф-ия формирующая знак.