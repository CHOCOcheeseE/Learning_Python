HargaLaptop = int(input("Masukan Harga Laptop :"))
NilaiSisa = int(input("Masukan Nilai Sisa :"))
NilaiAset = int(input("Masukan Nilai Aset :"))

SusutTahunan = (HargaLaptop - NilaiSisa)/ 7
MasaPakai = (SusutTahunan * 3)
NilaiAsetTersisa = HargaLaptop - MasaPakai

print("Hasil dari susut tahunan adalah : ",SusutTahunan)