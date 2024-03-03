Nama = input("masukan nama :")
Tempatlahir = input("masukan tempat lahir : ")
tanggallahir = float(input("masukan tanggal lahir : "))
tahunlahir = float(input("masukan tahun lahir : "))
jeniskelamin = input("masukan jenis kelamin : ")
nilaimatapelajaranInggris = float(input("masukan nilai pelajaran Inggris : "))
nilaimatapelajaranmatematika = float(input("masukan nilai pelajaran matematika : "))
nilaimatapelajaranIndonesia = float(input("masukan nilai pelajaran Indonesia : "))
tahunsaatini = 2024

umur = tahunsaatini - tahunlahir
rataratanilai = (nilaimatapelajaranInggris + nilaimatapelajaranmatematika + nilaimatapelajaranIndonesia) / 3

if umur > 25 :
    print("Umur anda melebihi persyaratan Universitas")
elif rataratanilai > 80 and jeniskelamin == "laki laki" :
    print(f"Dengan nilai rata rata : {rataratanilai} dan jenis kelamin {jeniskelamin}, disarankan untuk masuk jurusan Teknik Informatika")
elif rataratanilai > 80 and jeniskelamin == "perempuan" :
    print(f"Dengan nilai rata rata : {rataratanilai} dan jenis kelamin {jeniskelamin}, disarankan untuk masuk jurusan Sistem Informasi")
else :
    print(f"Dengan nilai rata rata : {rataratanilai} dan jenis kelamin {jeniskelamin}, disarankan untuk masuk jurusan DKV")