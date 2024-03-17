gajiPokok = float(input("Masukkan gaji pokok anda :"))
uangTransport = float(input("Masukkan uang transport harian :"))
uangMakan = float(input("Masukkan uang makan harian :"))
tunjanganJabatan = float(input("Masukkan gaji Tunjangan jabatan anda :"))

honor_Lembur_jam_pertama = 1 * 1.5 * 1/173 * gajiPokok
honor_Lembur_jam_selanjutnya = 9 * 2 * 1/173 * gajiPokok
total_honor_lembur = honor_Lembur_jam_pertama + honor_Lembur_jam_selanjutnya

print("Total honor lembur anda : %.0f"% total_honor_lembur)

elemenGaji = gajiPokok + uangTransport + uangMakan + tunjanganJabatan + total_honor_lembur

print("Total Gaji keseluruhan anda : %.0f"% elemenGaji)