
import exception as exp

def importFile(nameFile):
    with open(nameFile, 'r', encoding='utf-8') as impFile:
        importData=impFile.readlines()
        impFile.close()
    return importData

listImpString = importFile('usersImp.csv')
#print(len(result))
#a = len(result)
# Проверка импортируемых данных -
# 1. количество передаваемых значений - id
# 2. проверка цифрового поля
# 3. Проверка логического поля
listTuple=[]
if listImpString!=None:
    for i in range(len(listImpString)):
         str=listImpString[i].strip()
         str=tuple(str.split(';'))
         if exp.ChekDigitColumnTable('users',str):
             if exp.CheckColValue('users', str):
                 if exp.CheckBoolColumnTable('users', str):
                     listTuple.append(str)
                     print(str, len(str))
                 else: print(f'В имортируемой строке введены не верно булевое значение 1/0, отказано в импорте -> {str}')
             else: print(f'В имортируемой строке введены не верно числовые значения, отказано в импорте -> {str}')
         else: print(f'Срока с некорректным количеством значений, отказано в импорте -> {str}')

print()
print(listTuple)


