print("==================================================")
print("          APLIKASI KASIR RESTORAN                 ")
print("==================================================")

# 1. Inisialisasi variabel total
total_belanja = 0

# Data menu (Dictionary)
menu = {
    1: {"nama": "Nasi Goreng", "harga": 25000},
    2: {"nama": "Mie Ayam", "harga": 15000},
    3: {"nama": "Ayam Geprek", "harga": 20000},
    4: {"nama": "Sate Ayam", "harga": 30000},
    5: {"nama": "Bakso", "harga": 18000}
}

# 2. Perulangan untuk menampilkan menu & 3. Proses Pemesanan
while True:
    print("\n--- DAFTAR MENU MAKANAN ---")
    for key, item in menu.items():
        # Cara lama (ribet)
     print(str(key) + ". " + item['nama'] + " - rp" + str(item['harga'])) 
    print("0. Selesai Memilih")
    
    # Input pilihan
    try:
        pilihan = int(input("\nMasukkan pilihan menu (0-5): "))
        
        # 4. Apakah Pilihan 0?
        if pilihan == 0:
            break # Keluar dari perulangan jika pilih 0
        
        elif pilihan in menu:
            jumlah = int(input("masukkan jumlah " + menu[pilihan]['nama'] + ":"))
            subtotal = menu[pilihan]['harga'] * jumlah
            total_belanja += subtotal
            print("pesanan ditambahkan:" + str(jumlah)+" "+menu[pilihan]['nama']+ " ke pesanan.")
        else:
            print("Pilihan tidak valid. Silakan pilih 0-5.")
            
    except ValueError:
        print("Input harus berupa angka!")

# 5. Hitung Diskon
print("\n--- PROSES PEMBAYARAN ---")
if total_belanja > 200000:
    diskon_persen = 20
    potongan = total_belanja * 0.20
else:
    diskon_persen = 0
    potongan = 0

total_bayar = total_belanja - potongan

# 6. Tampilkan Struk Pembayaran
print("\n" + "="*50)  # cetak garis atas
print("             STRUK PEMBAYARAN             ")
print("="*50)
print("total belanja: RP{:,}".format(total_belanja).replace(",","."))
print("diskon:{}%".format(diskon_persen))
print("potongan:RP{:,}".format(potongan).replace(",","."))
print("-" * 50)
print("total bayar : RP {:,}".format(total_bayar).replace(",","."))
print("="*50)
print("               TERIMA KASIH               ")
print("="*50)


                    
    