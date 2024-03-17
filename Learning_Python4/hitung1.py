angka1 = int(input("masukan angka yang akan dibandingkan :"))
angka2 = int(input("masukan angka yang akan dibandingkan :"))

if angka1 > angka2:
    print(f"{angka1} lebih besar dari {angka2}")
elif angka2 > angka1:
    print(f"{angka2} lebih besar dari {angka1}")
else:
    print(f"{angka1} sama besar dengan {angka2}")