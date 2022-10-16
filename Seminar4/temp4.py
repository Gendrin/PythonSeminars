from random import randint
from random import sample
from random import choice

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

def WritingFile(nameFile,printString):
    nameFile=open(nameFile, "a")
    nameFile.write(printString + '\n')
    nameFile.close

def ConcatePolyStr(inPolyStr1,inPolyStr2):
    result = inPolyStr1.replace('=0', '+')
    result = result.replace('\n', '')
    result+= inPolyStr2.replace('\n', '')
    return result

def ConcatePolyFiles(inSeparateString):
    arrString = inSeparateString.split()
    for j in range(0, len(arrString)):
        poly1 = arrString[0]
        poly2 = arrString[1]
    with open(poly1, "r") as file1:
        contents1 = file1.readlines()
    with open(poly2, "r") as file2:
        contents2 = file2.readlines()
    if len(contents1) == len(contents2):
        # print('Result')
        insertStrFileResult = input("Enter names files result Task5 polyRez.txt -> ")
        for i in range(0, len(contents1)):
            concateStr = ConcatePolyStr(contents1[i], contents2[i])
            WritingFile(insertStrFileResult, concateStr)
            print(concateStr)
    else:
        print('The contents of the files do not match!')


# print('Task4 Seminar N4 Fun')
# insertString = input("Enter numbers separated by spaces -> ")
# insertStringNameFile = input("Enter name file for writing 'Task4.txt' 'Poly1.txt'-> ")
# arrString=insertString.split()
# for j in range(0,len(arrString)):
#     inNumTsk5=CheckInputInt(arrString[j])
#     resultString=CreateStringPoly(inNumTsk5)
#     WritingFile(insertStringNameFile,resultString)
#     print('writing in file Task4.txt -->' + resultString)

# print('Task4 Seminar N5 ')
# insertString = input("Enter names files number1 and number2 separated by spaces poly1.txt and poly2.txt -> ")
# ConcatePolyFiles(insertString)

# num_list = range(0,10)
# for i in range(10,1,-1):
#     #value = choice(num_list)
#     #value = choice(range(0,10))
#     value = choice('0123456789')
#     print(value,end="")
def Generate_List_Random_Worlds(count_w:int, text:str='абв'):
    Random_world_list=[]
    for i in range(count_w):
        world=sample(text,3)
        Random_world_list.append("".join(world))
    return " ".join(Random_world_list)

def GenerateAndChekListTask1(inNum):
    genList = sample(range(inNum*2,inNum))
    print(f'Generate random list -> {genList}')
    return  [genList[i+1] for i in range(len(genList)-1) if genList[i]<genList[i+1]]

print('Task1 Seminar N6')
mList=CreateRandomList(1,20,10)
mLi = sample(range(20),10)
print(mList)
print(f'mLi - > {mLi}')
#rList = [n for n in mList if mList[n]>mList[n+1] and n<len(mList)]
indList = [n+1 for n in range(len(mList)-1) if mList[n]<mList[n+1]]
print(indList)
#resList = [mList[i] for i in range(len(mList)) if mList[i]>mList[i-1]]
resList = [mList[i+1] for i in range(len(mList)-1) if mList[i]<mList[i+1]]
#i=0
#resList = [i for indList[i] in mList]
#resList=[i for i in mList(indList)]
print(resList)
#rList = [n for n in mList if 4 > ind > 0]
