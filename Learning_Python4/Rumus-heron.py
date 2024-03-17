sisiA = float(input("Masukkan sisi A :"))
sisiB = float(input("Masukkan sisi B :"))
sisiC = float(input("Masukkan sisi C :"))

s = (sisiA + sisiB + sisiC) / 2
area = (s * (s - sisiA) * (s - sisiB) * (s - sisiC)) ** 0.5

print(f"Luas segitiga adalah {area:.2f}" )

keliling = sisiA + sisiB + sisiC

print(f"Keliling segitiga adalah {keliling:.0f}")