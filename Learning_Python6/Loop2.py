rows = 5
col = 9

for i in range(rows):
    for j in range(i+1):
        print(col, end=' ')
        col -= 1
    print()
    col += i
print()

rows = 5

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
print()

rows = 5
start_col = 1
increment = 2

for i in range(1, rows + 1):
    col = start_col
    for j in range(1, rows + 1):
        print(col, end=' ')
        col += increment
    start_col += 1
    print()
print()

rows = 5

for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
print()

rows = 5

for i in range(rows, 0, -1):
    for j in range(1, i):
        print("_", end=' ')
    for k in range(i, rows + 1):
        print(k, end=' ')
    print()
print()

rows = 4
chars = ['A', 'B']

for i in range(rows):
    start_char = chars[i % 2]
    for j in range(rows + 1):
        print(start_char, end=' ')
        start_char = chars[(chars.index(start_char) + 1) % 2]
    print()
print()

rows = 5
chars = ['S', 'O']

for i in range(rows):
    start_char = chars[i % 2]
    for j in range(rows - i):
        print(start_char, end=' ')
        start_char = chars[(chars.index(start_char) + 1) % 2]
    print()
print()

rows = 5
chars = ['S', 'O']

for i in range(rows):
    start_char = chars[i % 2]
    for j in range(rows - i):
        print(start_char, end=' ')
        start_char = chars[(chars.index(start_char) + 1) % 2]
    print()
print()

rows = 5

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        print(i * j, end=' ')
    print()
print()

rows = 7

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == j or i + j == rows + 1:
            print("1", end=' ')
        else:
            print("+", end=' ')
    print()
print()

