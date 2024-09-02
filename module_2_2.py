first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
if first == second == third:
    print ('3')
elif first == second != third:
    print ('2')
elif first == third != second:
    print('2')
elif second == third != first:
    print('2')
else:
    print ('0')