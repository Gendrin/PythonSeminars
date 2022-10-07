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
def CreateStringPoly(inNum):
    if inNum!=None and inNum!=0 and inNum > 0:
        fierstList = CreateRandomList(0,9,inNum+1)
        print(f'Creating random List -> {fierstList}')
        i = 0
        resultString=''
        saveInNum=inNum
        inNum+=1
        flagZnak=False
        while i < len(fierstList):
            if fierstList[i]!=0 and i < saveInNum:
                inNum=inNum-1
                if flagZnak:
                    resultString += CreateRandomSign()+str(fierstList[i]) + '*x^' + str(inNum)
                else:
                    resultString += str(fierstList[i]) + '*x^' + str(inNum)
                    flagZnak=True
            else:
                inNum = inNum - 1
            if i == saveInNum:
                if fierstList[i]==0:
                    resultString +='=0'
                else:
                    resultString += CreateRandomSign()+str(fierstList[i]) + '=0'
            i+=1
        return resultString



print('Task4 Seminar N4 Fun')
insertString = input("Enter numbers separated by spaces -> ")
arrString=insertString.split()
for j in range(0,len(arrString)):
    inNumTsk5=CheckInputInt(arrString[j])
    resultString=CreateStringPoly(inNumTsk5)
    task4File = open("Task4.txt", "a")
    task4File.write(resultString + '\n')
    task4File.close
    print('writing in file Task4.txt -->' + resultString)

print('Task4 Seminar N5 ')
insertString = input("Enter names files number1 and number2 separated by spaces poly1.txt and poly2.txt -> ")
arrString=insertString.split()
for j in range(0,len(arrString)):
    poly1 = arrString[0]
    poly2 = arrString[1]

#readlines(): считывает все строки файла в список

# 1. Формируем список коэффициентов 10 штук ф-ия
# 2. Формируем строку , первый К всегда положительный, следующие
# добавляют себе знак, если к =0 пропуск элемента.
# 3. Ф-ия формирующая знак.