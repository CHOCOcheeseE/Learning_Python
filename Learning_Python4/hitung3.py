angka1 = int(input("masukukan bilangan pertama : "))
angka2 = int(input("masukukan bilangan kedua : "))
angka3 = int(input("masukukan bilangan ketiga : "))

if angka2 < angka1 and angka3 < angka1:
    print (f"bilangan {angka1}, lebih besar dari bilangan {angka2} dan bilangan {angka3}")
elif angka1 < angka2 and angka3 < angka2:
    print (f"bilangan {angka2}, lebih besar dari bilangan {angka1} dan bilangan {angka3}")
elif angka2 < angka3 and angka1 < angka3:
    print (f"bilangan {angka3}, lebih besar dari bilangan {angka1} dan bilangan {angka2}")
elif angka1 == angka2 and angka1 and angka2 > angka3:
    print (f"bilangan A {angka1} sama dengan bilangan B {angka2} dan dua bilangan tersebut lebih besar dari bilangan C {angka3}")
elif angka1 == angka3 and angka1 and angka3 > angka2:
    print (f"bilangan A {angka1} sama dengan bilangan C {angka3} dan dua bilangan tersebut lebih besar dari bilangan B {angka2}")
elif angka2 == angka3 and angka2 and angka3 > angka1:
    print (f"bilangan B {angka2} sama dengan bilangan C {angka3} dan dua bilangan tersebut lebih besar dari bilangan A {angka1}")
else:
    print (f"bilangan A {angka1} bilangan B {angka2} bilangan C {angka3} sama besar")