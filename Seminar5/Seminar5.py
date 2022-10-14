from random import sample


def CheckInputInt(testInput):
    try:
        return int(testInput)
    except ValueError as Err:
        print(f'Incorrect data entry -> {Err}')
        return None


def Generate_List_Random_Worlds(count_w: int, text: str = 'абв'):
    Random_world_list = []
    for i in range(count_w):
        world = sample(text, len(text))
        Random_world_list.append("".join(world))
    return " ".join(Random_world_list)


def Replase_String(inString, baseString: str = 'абв'):
    result = inString.replace(" " + baseString, "")
    result = result.replace(baseString + " ", "")
    return result

def WritingFile(nameFile,printString):
    nameFile=open(nameFile, "a")
    nameFile.write(printString + '\n')
    nameFile.close

def SetCryptoFiles(inSeparateStringNameFiles):
    arrString = inSeparateStringNameFiles.split()
    fileList=[]
    for i in range(0, len(arrString)):
        fileList.append(arrString[i]) #  Name files - 0 - fileInText, 1- fileCryptText, 2 - file DeCryptText
    return fileList

def InStringsToFile(nameFile):
    numString =  input("Enter number string for input text_worlds.txt -> (Enter - 0 string)")
    if numString.isdigit():
        for i in range(0,int(numString)):
            insertStrFileIn = input("Enter text for file Task2 Seminar5 text for coding text_worlds.txt -> ")
            WritingFile(nameFile,insertStrFileIn)

def PrintstringInFile(nameFile):
    with open(nameFile, "r") as fileForRead:
        contents = fileForRead.readlines()
        for i in range(0, len(contents)):
            print(contents[i],end='')

def CodingOneString(textString):
    inText = textString.strip()
    lstr = list(inText)
    my_dict = {}.fromkeys(lstr, 0)
    for i in lstr:
        my_dict[i] += 1
    crypt_str = ''
    for j in my_dict:
        crypt_str += str(my_dict[j]) + j
    return crypt_str

def DecodingOneString(codeString):
    inText = codeString.strip()
    dc_list = list(inText)
    key_list = []
    val_list = []
    i=0
    while i <  len(dc_list):
        temp_value=''
        if dc_list[i].isdigit():
            while dc_list[i].isdigit():
                temp_value+=dc_list[i]
                i+=1
            val_list.append(int(temp_value))
        else:
            key_list.append(dc_list[i])
            i+=1

    dec_dict = dict(zip(key_list, val_list))
    dec_str = ''
    for k in dec_dict:
        dec_str += dec_dict[k] * k
    return dec_str

def CodingTextFiles(textFile,codeFiles):
    with open(textFile, "r") as fileT:
        contentsText = fileT.readlines()
    with open(codeFiles, "w") as fileC:
        for i in range(0, len(contentsText)):
            WritingFile(codeFiles,CodingOneString(contentsText[i]))

def DecodingFile(codeFile,resultFile):
    with open(codeFile, "r") as fileC:
        contentsCode = fileC.readlines()
    with open(resultFile, "w") as fileT:
        for i in range(0, len(contentsCode)):
            WritingFile(resultFile, DecodingOneString(contentsCode[i]))




print('Task1 Seminar N5')
insertNumberWorlds = CheckInputInt(input('Enter number rendom worlds for task N1: '))
insertFierstRandomString = input('Enter start rendom string for task N1:(Enter default - абв) ')
if insertNumberWorlds != None:
    if insertFierstRandomString == '':
        result_generate_string = Generate_List_Random_Worlds(insertNumberWorlds)
        print(result_generate_string)
        print(Replase_String(result_generate_string))
    else:
        result_generate_string = Generate_List_Random_Worlds(insertNumberWorlds, insertFierstRandomString)
        print(result_generate_string)
        print(Replase_String(result_generate_string, insertFierstRandomString))



print('Task2 Seminar N5')
fileNameList = []
print('Введите имена файлов исходного текста, кодирования и декодирования, разделенные пробелом text_worlds.txt ->')
print('Или нажмите ввод если вас устраивают файлы по умолчанию')
fileNameList = SetCryptoFiles(input("text_words.txt text_code_words.txt text_decode_words.txt "))
if len(fileNameList)==0:
    fileNameList = SetCryptoFiles('text_words.txt text_code_words.txt text_decode_words.txt')
InStringsToFile(fileNameList[0])
print(f'Out in File - > {fileNameList[0]}')
PrintstringInFile(fileNameList[0])
CodingTextFiles(fileNameList[0],fileNameList[1])
print(f'Coding File - > {fileNameList[1]}')
PrintstringInFile(fileNameList[1])
DecodingFile(fileNameList[1],fileNameList[2])
print(f'DeCoding File - > {fileNameList[2]}')
PrintstringInFile(fileNameList[2])