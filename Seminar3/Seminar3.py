def CheckInputInt(testInput):
    try:
        return int(testInput)
    except ValueError:
        print('Incorrect data entry')
        return None


# ������� ������ �� ���������� �����. �������� ���������, ������� ����� ����� ��������� ������, ������� �� �������� �������.
print('Seminar3 Task N1')
insertString = input("Enter numbers list separated by spaces -> ")
arrString = insertString.split()
arrIntDigits = []
# check input variable
flagInsertData = True
for numI in arrString:
    if CheckInputInt(numI) == None:
        flagInsertData = False
    else:
        arrIntDigits.append(CheckInputInt(numI))
sumNechetDigitList = 0
if flagInsertData:
    for i in range(len(arrIntDigits)):
        if i % 2 != 0:
            sumNechetDigitList += arrIntDigits[i]
    print(f'{arrIntDigits} -> {sumNechetDigitList}')

# �������� ���������, ������� ����� ������������ ��� ����� ������. ����� ������� ������ � ��������� �������, ������
# � ������������� � �.�.
print('Seminar3 Task N2')

# ������� ������ �� ������������ �����. �������� ���������, ������� ����� ������� ����� ������������ � �����������
# ��������� ������� ����� ���������.
# �������� �������� ������������ ������ ������
print('Seminar3 Task N3')
lst = [1.1, 1.2, 3.1, 5, 10.01]

new_lst = [round(i%1.0,2) for i in lst if i%1!=0]
print(new_lst, '=>', max(new_lst) - min(new_lst))

# �������� ���������, ������� ����� ��������������� ���������� ����� � ��������.
print('Seminar3 Task N4')

# ������� �����. ��������� ������ ����� ���������, � ��� ����� ��� ������������� ��������.
print('Seminar3 Task N5')