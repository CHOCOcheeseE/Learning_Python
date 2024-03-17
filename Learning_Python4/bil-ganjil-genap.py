a = int(input("Masukkan Bilangan :"))

if a > 0 and a %2 == 0:
  print(f"{a} adalah bilangan Positif dan genap")
elif a > 0 and a %2 == 1:
  print(f"{a} adalah bilangan Positif dan ganjil")
elif a < 0 and a %2 == 0:
  print(f"{a} adalah bilangan Negatif dan genap")
elif a < 0 and a %2 == 1:
  print(f"{a} adalah bilangan Negatif dan ganjil")
else:
  print(f"{a} adalah bilangan Netral")