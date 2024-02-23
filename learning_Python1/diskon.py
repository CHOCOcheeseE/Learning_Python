uangbelanja = float(input("masukan jumlah uang yang dibawa:"))
totalbelanja = float(input("masukan total belanja disini:"))

if totalbelanja > 70000:
    diskon = totalbelanja * (10/100)
else : diskon = 0

print(f"anda mendapatkan diskon sebesar : {diskon:.0f}")

setelahdiskon = totalbelanja - diskon
kembalian = uangbelanja - setelahdiskon

print(f"total kembalian : {kembalian:.0f}")