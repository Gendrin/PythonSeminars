#1. �������� ���������, ������� ��������� �� ���� �����, ������������ ���� ������, � ���������, �������� �� ���� ���� ��������.
#dayWeek = int(input('������� ����� ��������������� ��� ������'))

#Task number 1
dayWeek = int(input('Insert number for week day '))

if dayWeek == 6 or dayWeek == 7:
   print(f'- {dayWeek} -> yes')
elif dayWeek <= 0 or dayWeek < 6:
   print(f'- {dayWeek} -> no')
