text = "Aku Cinta Indonesia"
r = 3

for i in range(r):
    print(text)

print()

a = 2
b = 2

for i in range(6):
    print(a)
    a += b
    b += 1

print()

z = 1
y = 1

for i in range(3):
    result = z * y
    print(f"{z} x {y} = {result}")
    y += 1

print()

baris = 3
kolom = 4

for i in range(baris):
    for j in range(kolom):
        print("*", end= " ")
    print()

print()

angka = 1

for i in range(3):
    for j in range(4):
        print(angka, end= " ")
    print()
    angka += 1

print()

a = 1
b = 1
temp = 1

for i in range(10):
    a = b
    b = temp
    temp = a + b
    print(a, end= " ")

print()

a = 1
b = 2
c = 3
print(a, end= " ")
print(b, end= " ")
print(c, end= " ")

for i in range(10):
    next_angka = a + b + c 
    print(next_angka, end= " ")
    a = b
    b = c
    c = next_angka

print()

length = 4

for i in range(4):
    for j in range(length):
        print("1", end= " ")
    length -= 1
    print()

print()

length = 5
for i in range(5):
    for j in range(length):
        if i % 2 == 0:
            if j % 2 == 0:
                print("2", end= " ")
            else:
                print("3", end= " ")
        else:
            if j % 2 == 1:
                print("2", end= " ")
            else:
                print("3", end= " ")
    print()
    length -=1