

nama = input("Masukkan nama mahasiswa: ")
target = int(input("Masukkan target nilai: "))

percobaan = 0

while percobaan < 3:
    nilai = int(input("Masukkan nilai : "))
    percobaan += 1

    if nilai >= target:
        print("Selamat", nama)
        print("Anda berhasil lulus!")
        break
    else:
        print("Nilai belum mencapai target.")
        print("Silakan ulangi.")

if nilai < target and percobaan == 3:
    print("Maaf", nama)
    print("Anda dinyatakan tidak lulus.")