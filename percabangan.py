#variabel dan tipe data
nama_mhs = "juan"
kelas = "c1"

nama_mhs = input("masukkan nama:")
nalgoritma = float(input("masukkan nilai nalgoritma:"))
nagama = float(input("masukkan nilai nagama:"))
nbasisdata = float(input("masukkan nilai nbasisdata:"))
npancasila = float(input("masukkan nilai npancasila:"))
nindonesia = float(input("masukkan nilai nindonesia:"))
nmatematika = float(input("masukkan nilai nmatematika:"))
ninggris = float(input("masukkan nilai ninggris:"))

print(nama_mhs)
rata_rata = (nalgoritma + nagama + nbasisdata + npancasila + nmatematika + ninggris) // 7
print(rata_rata)
if rata_rata>=80 and rata_rata<=100:
    print ("nilai : A")
elif rata_rata >=70 and rata_rata <=80:
    print  ("nilai : B")
elif rata_rata >=20 and rata_rata <=70:
    print ("nilai : C")
elif rata_rata >=40 and rata_rata <=60:
    print ("nilai : D")
elif rata_rata >=30 and rata_rata <=70:
    print ("nilai : E")
else: print("nilai lebih dari 100 atau dibawah 50")              