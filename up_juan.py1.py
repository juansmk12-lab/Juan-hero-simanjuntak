print("======================================")
print("  APLIKASI PEMESANAN TIKET BIOSKOP")
print("======================================")

while True:
    nama = input("\nmasukkan nama pelanggan:")

    print("\njenis tiket:")
    print("1. regular - rp35.000")
    print("2. VIP    - rp50.000")
    print("3. premium - rp75.000")

    jenis = input("pilih jenis tiket(1/2/3):")

    if jenis == "1":
        nama_tiket = "regular"
        harga = 35000
    elif jenis == "2":
        nama_tiket = "VIP"
    elif jenis == "3":
        nama_tiket = "premium"
        harga = 75000 
    else:
        print("pilihan tiket tidak tersedia!")
        continue

    jumlah = int(input("masukkan jumlah tiket: "))

    total = harga * jumlah

    if jumlah > 3:
        diskon = total * 10 / 100
    else:
        diskon = 0

    pembayaran = total - diskon

    print("/n========== STRUK PEMESANAN ===========")
    print("nama pelanggan :", nama)
    print("jenis tiket   :", nama_tiket)
    print("jumlah tiket  :", jumlah)
    print("harga tiket   :", harga)
    print("total harga   :", total)
    print("diskon        :", diskon) 
    print("total bayar   :", pembayaran)
    print("========================================")  

    ulang = input("\napakah ingin melayani pelanggan lain? (y/t):")

    if ulang.lower() !="y":
        print("\nterima kasih telah menggunakan aplikasi!")
        break      