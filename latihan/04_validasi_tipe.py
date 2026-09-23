print("PROGRAM VALIDASI TIPE")
print("=" * 30)

teks = input("Masukkan data: ")

try:
    nilai = float(teks)
    print("Data valid: input berupa angka.")

except ValueError:
    print("Data tidak valid: input bukan angka.")