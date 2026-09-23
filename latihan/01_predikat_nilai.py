# Latihan 1: Predikat Nilai
# Input: Nilai akhir (float)
# Aturan: Mengonversi nilai ke predikat (A, B, C, D, E) menggunakan rantai elif
# Output: Predikat nilai

nilai = float(input("Nilai akhir (0-100): "))

if nilai >= 85:
    predikat = "A"
elif nilai >= 70:
    predikat = "B"
elif nilai >= 60:
    predikat = "C"
elif nilai >= 50:
    predikat = "D"
else:
    predikat = "E"

print(f"Nilai {nilai:.2f} memperoleh predikat {predikat}.")