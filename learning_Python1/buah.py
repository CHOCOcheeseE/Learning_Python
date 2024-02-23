jerukdibeli = int(input("berapa kilo jeruk yang akan dibeli:"))
apeldibeli = int(input("berapa kilo apel yang akan dibeli:"))
manggadibeli = int(input("berapa kilo mangga yang akan dibeli:"))
manggisdibeli = int(input("berapa kilo manggis yang akan dibeli:"))
duriandibeli = int(input("berapa kilo durian yang akan dibeli:"))

# Harga jeruk perkilo 

hargajeruk = 15.000
hargaapel = 30.000
hargamangga = 20.000
hargamanggis = 7.000
hargadurian = 50.000

jumlahharga = (jerukdibeli * hargajeruk) + (apeldibeli * hargaapel) + (manggadibeli * hargamangga) + (manggisdibeli * hargamanggis) + (duriandibeli * hargadurian)

print (f"total uang yang dikeluarkan untuk membayar semua buah ayang telah dibeli adalah : {jumlahharga:.3f}")