def HelloWorld ():
    print ('Hello World!')
HelloWorld()
print()

def perkalian (f, g):
    return f * g
print(perkalian(3, 5))
print()

def luassegitiga (f, g):
    return 1/2 * f * g
print(luassegitiga(3, 5))
print()

def selamatdatang (nama):
    print(f"selamat datang, {nama}")
selamatdatang("Alice")
print()

def hitungpersegipanjang (p, l):
    keliling = 2 * (p + l)
    luas = p * l
    return keliling, luas
print(hitungpersegipanjang(5, 3))
print()

my_list = [1, 2, 3, 3, 4, 4, 5, 6, 6]
def unique(list_int:list):
    list_int = set(list_int)
    list_int = list(list_int)
    print(list_int)
    return len(list_int)
print(unique(my_list))
print()

def hitungkata(c:str):
    c_list = c.strip().split()
    return len(c_list)
print(hitungkata("Ini adalah Contoh kaliamat"))
print()

def sumlist(my_list):
    return sum(my_list)
my_list = [1, 2, 3, 4, 5]
result = sumlist(my_list)
print("hasil semua elemen list:", result)
print()

def is_palindrome(s):
    return s == s[::-1]

kata = "level"
if is_palindrome(kata):
    print(f'"{kata}"adalah palindrom')
else:
    print(f'"{kata}"bukan palindrom')
print()

def find_max(my_list):
    return max(my_list)

my_list = [10, 20, 5, 30, 15]
hasil = find_max(my_list)
print(f"bilangan terbesar dalam list diatas adalah: {hasil}")
print()

def urutkan(str):
    return ''.join(sorted(str))
string_input = "python"
hasil_urutan = urutkan(string_input)
print(hasil_urutan)
print()

def tes(kata1, kata2):
    return sorted(kata1) == sorted(kata2)
kata1 = "listen"
kata2 = "silent"

hasil = tes(kata1, kata2)
print(hasil)