first = input('Введите первое число: ')
second = input ('Введите второе число: ')
third = input('Введите третье число: ')
if int(first) == int(second) and int(second) == int(third):
    print(3)
elif int(first) == int(second) or int(first) == int(third) or int(third) == int(second):
    print(2)
else:
    print(0)