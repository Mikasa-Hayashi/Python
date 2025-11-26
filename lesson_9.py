# Задача: определить, является ли комбинация трех входных числел
# диагональню, строчкой или столбцом для игры в крестики-нолики.

# 1 2 3
# 4 5 6
# 7 8 9

# Входные данные: n1, n2, n3 (n1 < n2 < n3)
# Выходные данные: Выигрышная или проигрышная комбинация


# Input data
n1 = int(input('Enter n1: '))
n2 = int(input('Enter n2: '))
n3 = int(input('Enter n3: '))

# Validate data
if not (n1 < n2 < n3):
    print('Invalid data: must be: n1 < n2 < n3')
    exit()
if n1 < 1 or n3 > 9:
    print('Invalid data: must be: 1 < n1, n2, n3 < 9')
    exit()

# Main calculations

# Check rows
row_for_1 = (n1 - 1) // 3 + 1
row_for_2 = (n2 - 1) // 3 + 1
row_for_3 = (n3 - 1) // 3 + 1

# Check cols
col_for_1 = (n1 - 1) % 3 + 1
col_for_2 = (n2 - 1) % 3 + 1
col_for_3 = (n3 - 1) % 3 + 1

# Check win combination
if row_for_1 == row_for_2 == row_for_3:
    print('WIN: same row')
elif col_for_1 == col_for_2 == col_for_3:
    print('WIN: same col')
elif (n1, n2, n3) == (1, 5, 9) or (n1, n2, n3) == (3, 5, 7):
    print('WIN: same diagonal')
else:
    print('Not win')


# Test cases
# 1 2 3 - win
# 1 2 4 - not win
# 1 5 9 - win
# 2 5 8 - win
# 2 5 1 - error
# -1 2 4 - error
