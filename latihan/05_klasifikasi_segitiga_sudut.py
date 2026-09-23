print("PROGRAM KLASIFIKASI SEGITIGA BERDASARKAN SUDUT")
print("=" * 45)

sudut1 = float(input("Masukkan sudut 1: "))
sudut2 = float(input("Masukkan sudut 2: "))
sudut3 = float(input("Masukkan sudut 3: "))

if sudut1 <= 0 or sudut2 <= 0 or sudut3 <= 0:
    print("Segitiga tidak valid: semua sudut harus lebih dari 0.")

elif sudut1 + sudut2 + sudut3 != 180:
    print("Segitiga tidak valid: jumlah ketiga sudut harus 180 derajat.")

elif sudut1 == 90 or sudut2 == 90 or sudut3 == 90:
    print("Klasifikasi: Segitiga siku-siku.")

elif sudut1 > 90 or sudut2 > 90 or sudut3 > 90:
    print("Klasifikasi: Segitiga tumpul.")

else:
    print("Klasifikasi: Segitiga lancip.")