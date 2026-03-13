# Sistem Perhitungan Nilai Mahasiswa
# Menggunakan minimal 7 jenis operator dan 10 variabel

print("=== SISTEM PERHITUNGAN NILAI MAHASISWA ===\n")

# Operator Penugasan: menyimpan input ke variabel
nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))
bonus = float(input("Masukkan nilai bonus (jika ada, jika tidak isi 0): "))

# Operator Aritmatika: menghitung nilai akhir
nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

# Operator Penugasan: menambahkan bonus
nilai_akhir += bonus

# Operator Perbandingan: menentukan kelulusan
lulus = nilai_akhir >= 75
status_kelulusan = "LULUS" if lulus else "TIDAK LULUS"

# Operator Logika: cek kelulusan sempurna
lulus_sempurna = (nilai_akhir >= 75) and (uas >= 70)
status_sempurna = "LULUS SEMPURNA" if lulus_sempurna else "TIDAK LULUS SEMPURNA"

# Operator Identitas: memeriksa apakah nilai_asli dan nilai_backup merujuk ke objek yang sama
nilai_asli = nilai_akhir
nilai_backup = nilai_asli
referensi_sama = nilai_asli is nilai_backup

# Operator Keanggotaan: daftar peserta ujian
daftar_peserta = ["Andi", "Budi", "Citra", "Dina"]
terdaftar = nama in daftar_peserta
status_daftar = "TERDAFTAR" if terdaftar else "TIDAK TERDAFTAR"

# Operator Bitwise: simulasi operasi bit
a = 5
b = 3
bit_and = a & b
bit_or = a | b
bit_xor = a ^ b
shift_kiri = a << 1
shift_kanan = a >> 1

# Menampilkan hasil analisis
print("\n=== HASIL ANALISIS ===")
print(f"Nama Mahasiswa: {nama}")
print(f"Nilai Tugas: {tugas}, UTS: {uts}, UAS: {uas}, Bonus: {bonus}")
print(f"Nilai Akhir: {nilai_akhir:.2f}")
print(f"Status Kelulusan: {status_kelulusan}")
print(f"Status Lulus Sempurna: {status_sempurna}")
print(f"Apakah nilai_asli dan nilai_backup merujuk ke objek yang sama? {referensi_sama}")
print(f"Status Pendaftaran: {status_daftar}")

print("\n=== SIMULASI BITWISE ===")
print(f"a = {a}, b = {b}")
print(f"a & b = {bit_and}")
print(f"a | b = {bit_or}")
print(f"a ^ b = {bit_xor}")
print(f"a << 1 = {shift_kiri}")
print(f"a >> 1 = {shift_kanan}")