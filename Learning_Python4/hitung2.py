angka1 = int(input("masukan bilangan pertama :"))
angka2 = int(input("masukan bilangan kedua :"))
angka3 = int(input("masukan bilangan ketiga :"))

if angka2 > angka1 and angka3 > angka1:
    print (f"bilangan {angka1}, lebih kecil dari bilangan {angka2} dan bilangan {angka3}")
elif angka1 > angka2 and angka3 > angka2:
    print (f"bilangan {angka2}, lebih kecil dari bilangan {angka1} dan bilangan {angka3}")
elif angka2 > angka3 and angka1 > angka2:
    print (f"bilangan {angka3}, lebih kecil dari bilangan {angka1} dan bilangan {angka2}")