# Добавление / Удаление / Редактирование записей БД
import sqlite3

def seq(nameTable):
    connect = sqlite3.connect('barbershop.db')
    cursor = connect.cursor()
    cursor.execute("SELECT max(id) FROM {0};".format(nameTable))
    maxId = cursor.fetchone()
    seq= maxId[0]
    connect.commit()
    if seq==None: return 1
    else:
        return seq+1

def insertTable(nameTable,inData):
    connect = sqlite3.connect('barbershop.db')
    cursor = connect.cursor()
    if nameTable == 'users' or 'records' or 'orders':
        cursor.execute("INSERT INTO {0} VALUES(?, ?, ?, ?, ?);".format(nameTable), inData)
    elif nameTable == 'service':
        cursor.execute("INSERT INTO {0} VALUES(?, ?, ?);".format(nameTable), inData)
    connect.commit()

def insertUsers():
    print('Ввод информации о клиентах, мастерахЖ:')
    print('Введите информацию о клиенте разделенную запятыми в формате:')
    inData = input('Имя, Отчество - необязательно, телефон, клиент или мастер -> 1 или 0: ').split(',')
    if len(inData) == 4 and inData[3].isdigit():
        inData.insert(0, str(seq('users')))
        inData = tuple(inData)
        insertTable('users',inData)
        print(inData)
    else:
        print('Введены некорректные данные!')


print(seq('users'))
print(seq('records'))
print(seq('service'))
print(seq('orders'))
insertUsers()
#print('Введите информацию о клиенте разделенную запятыми в формате:')
# inData=input('Имя, Отчество - необязательно, телефон, клиент или мастер -> 1 или 0: ').split(',')
# if len(inData)==4 and inData[3].isdigit():
#     inData.insert(0,str(seq('users')))
#     inData=tuple(inData)
#     print(inData)
# else:
#     print('Введены некорректные данные!')