algoritma = int(input("Masukkan nilai Algoritma: "))
perancangan_objek = int(input("Masukkan nilai Perancangan Objek: "))
kalkulus = int(input("Masukkan nilai Kalkulus: "))
etika_profesi = int(input("Masukkan nilai Etika Profesi: "))
database = int(input("Masukkan nilai Database: "))
english = int(input("Masukkan nilai Bahasa Inggris: "))

kreditpermatkul = 3

def skor_bobot(skor):
    if skor >= 90:
        return 4
    elif skor >= 85:
        return 3.75
    elif skor >= 80:
        return 3.5
    elif skor >= 75:
        return 3.25
    elif skor >= 70:
        return 3
    elif skor >= 65:
        return 2.75
    elif skor >= 60:
        return 2.5
    elif skor >= 55:
        return 2.25
    elif skor >= 50:
        return 2
    elif skor >= 45:
        return 1.75
    elif skor >= 40:
        return 1.5
    elif skor >= 35:
        return 1.25
    elif skor >= 30:
        return 1
    elif skor < 30:
        return 0, 'E'
    else:
        return None, "Invalid Score"
    
totalalgoritma = kreditpermatkul * skor_bobot(algoritma)
totalperancanganobjek  = kreditpermatkul * skor_bobot(perancangan_objek)
totalkalkulus = kreditpermatkul * skor_bobot(kalkulus)
totaletikaprofesi = kreditpermatkul * skor_bobot(etika_profesi)
totaldatabase = kreditpermatkul * skor_bobot(database)
totalenglish = kreditpermatkul * skor_bobot(english)

totalkredit = kreditpermatkul * 6

totalipk = (totalalgoritma + totalperancanganobjek + totalkalkulus + totaletikaprofesi + totaldatabase + totalenglish) / totalkredit

print(f"Indeks Prestasi Kumulatif (IPK) Anda adalah: {totalipk:.2f}")