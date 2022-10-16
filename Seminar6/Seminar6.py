from random import sample

def CheckInputInt(testInput):
    try:
        return int(testInput)
    except ValueError as Err:
        print(f'Incorrect data entry -> {Err}')
        return None

def GenerateAndChekListTask1(inNum):
    genList = sample(range(inNum*2), inNum )
    print(f'Generate random list -> {genList}')
    return  [genList[i+1] for i in range(len(genList)-1) if genList[i]<genList[i+1]]

def ChekForTask2(inNum):
    return [i for i in range(20,inNum+1) if i%20 == 0 or i%21==0]

def GetDictTask3(inString):
    inList = inString.split()
    sortList = sorted(inList)
    m_dict = {}
    for i in sortList:
        simbol = i[0]
        if simbol not in m_dict:
            m_dict[simbol] = [i]
        else:
            m_dict[simbol] += [i]
    return m_dict

print('Task4 Seminar N4')
insertString = input("Enter number digit in the list, for Task №1 Seminar6 -> ")
if insertString.isdigit():
    print(f'Result chek list Task1 - > {GenerateAndChekListTask1(int(insertString))}')
else:
    print('Not correct entering!')

print('Task2 Seminar N6')
insertString = input("Enter digit for Task №2 Seminar6 -> ")
if insertString.isdigit():
    print(f'Chek result Task №2 -> {ChekForTask2(int(insertString))}')
else:
    print('Not correct entering!')

print('Task3 Seminar N6')
#3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
#ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся
# соответствующей буквы.
insertString = input("Enter names separated by spaces -> Иван Мария Петр Илья Марина Петр Алина Бибочка.. as default - enter")
if len(insertString)==0:
    insertString = "Иван Мария Петр Илья Марина Петр Алина Бибочка"
print(f'Result - > {GetDictTask3(insertString)}')