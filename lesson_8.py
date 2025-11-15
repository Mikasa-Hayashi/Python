# Логические операторы позволяют объединять условия или менять 
# их смысл. Они управляют логикой ветвлений.

# Основные операторы
# and — оба условия должны быть True
# or — хотя бы одно условие должно быть True
# not — инвертирует значение (True → False, False → True)

# age = int(input())

# if age < 0 or age > 120:
#     print('Incorrect')
# else:
#     print(age)

# x = -1

# if x == 1 or x == 2:
#     print('OK')

# num = int(input())

# if num % 2 and num > 30:
#     print('Odd > 30')
# elif num % 2:
#     print('Odd')
# else:
#     print('Even')

x = False

if not x:
    print('OK')

# if not is_done:
    # do smth
