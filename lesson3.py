# f-строки - способ вставлять переменные прямо внутрь строки
# Экранирование - использование \ для вставки спецсимволов
# Конкатенация - склеивание строк с помощью +
# Многострочные строки - создаются с помощью тройных кавычек

# f-строки
name = 'Ivan'
print(f'Hello, {name}')
print(f'5 + 5 = {5+5}')

age = '20'
print(f'His name is {name} and he is {age} years old')

# Экранирование
fruit = 'Apple'
print(f'It\'s {fruit}')

# Конкатенация
print('His name is ' + name + ' and he is ' + age + ' years old')

# Многострочные строки
greet = ('Hello, \n' 
                        'dear friend, \t'
'how are you doing?')

greet_2 = '''Hello,\n
    dear friend, \n
    how are you doing?'''

greet_3 = 'Hello, \
dear friend, \
how are you doing?'

print(greet)
print(greet_2)
print(greet_3)