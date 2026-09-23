print("VALIDASI DAN KLASIFIKASI NILAI")
print("=" * 35)

ujian = input("Nilai ujian (0-100): ")
tugas = input("Nilai tugas (0-100): ")
hadir = input("Kehadiran persen (0-100): ")

try:
    ujian = float(ujian)
    tugas = float(tugas)
    hadir = float(hadir)

except ValueError:
    print("Masukan ditolak: seluruh data harus berupa angka.")

else:
    # Validasi rentang
    if not (0 <= ujian <= 100):
        print("Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.")

    elif not (0 <= tugas <= 100):
        print("Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.")

    elif not (0 <= hadir <= 100):
        print("Masukan ditolak: kehadiran di luar rentang 0 sampai 100.")

    else:
        # Menghitung nilai akhir
        nilai_akhir = (0.6 * ujian) + (0.4 * tugas)

        print()
        print(f"Nilai akhir = {nilai_akhir:.2f}")

        # Validasi kehadiran
        if hadir < 80:
            print("Status: Tidak memenuhi syarat kehadiran.")

        else:
            # Klasifikasi nilai
            if nilai_akhir >= 85:
                predikat = "A"
            elif nilai_akhir >= 70:
                predikat = "B"
            elif nilai_akhir >= 60:
                predikat = "C"
            elif nilai_akhir >= 50:
                predikat = "D"
            else:
                predikat = "E"

            # Menentukan status
            if predikat in ("A", "B", "C"):
                status = "Lulus"
            else:
                status = "Belum lulus"

            print(f"Predikat: {predikat}")
            print(f"Status: {status}")