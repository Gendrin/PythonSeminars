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

print('Task4 Seminar N4')
insertString = input("Enter number digit in the list, for Task №1 Seminar6 -> ")
if insertString.isdigit():
    print(f'Result chek list Task1 - > {GenerateAndChekListTask1(int(insertString))}')