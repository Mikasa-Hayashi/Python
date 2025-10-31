# Приведение типов - это преобразование значения из одного типа данных в другой.

# Неявное (implicit) — Python делает сам, автоматически

# Явное (explicit) — мы делаем вручную с помощью специальных функций 

# Функции для приведения типов:
# int()
# float()
# str()
# bool()


# Неявное приведение
a = 5      # int
b = 2.5    # float
result = a + b
print(result)
print(type(result))

print(a==5)
print(type(a==6))


# Явное приведение
age = '20'
age = int(age)
print(type(age))
print(age + 5)

temperature = 36.6
print('temperature is ' + str(temperature))

a = True # 1
b = 2
c = False # 0
print(a + b + c)