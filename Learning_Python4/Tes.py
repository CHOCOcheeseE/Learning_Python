anggotatubuhcacat = input("Apakah anda memmiliki anggota tubuh cacat? ")

jeniskelamin = input("Masukkan jenis kelamin :")
beratbadan = int(input("Masukkan berat badan :"))
tinggibadan = int(input("Masukkan tinggi badan :"))
tahunlahir = int(input("Masukkan tahun lahir :"))
tahunsekarang = 2024
usia = tahunsekarang - tahunlahir
nilaiakademis = int(input("Masukkan nilai akademis :"))
kemampuan = input("Masukkan Skill :")

if anggotatubuhcacat == "ya":
  print(f"Anda tidak memenuhi kriteria karena memilik anggota tubuh cacat")
else:
  if jeniskelamin == "perempuan" and beratbadan >= 45:
    if beratbadan <= 50 and tinggibadan >= 165 and usia <= 20:
      print(f"Anda memenuhi kriteria 1")
    else:
      print(f"Anda tidak memenuhi kriteria 1")
  elif jeniskelamin == "laki laki" and beratbadan <= 70:
    if tinggibadan >= 170 and usia <= 30:
      print(f"Anda memenuhi kriteria 2")
    else:
      print(f"Anda tidak memenuhi kriteria 2")
  if jeniskelamin == "laki laki" or jeniskelamin == "perempuan":
    if nilaiakademis >= 90 and usia <= 30:
      print(f"Anda memnuhi kriteria 3")
    else:
      print(f"Anda tidak memenuhi kriteria 3")
  if jeniskelamin == "laki laki" or jeniskelamin == "perempuan":
    if kemampuan == "menembak" or kemampuan == "memanah" or kemampuan == "berkuda":
      print(f"Anda memenuhi kriteria 4")
    else:
      print(f"anda tidak memenuhi kriteria 4")