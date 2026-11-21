import os
import inquirer

#OTW TO BE FIXED

def Fitur_Pembayaran_Sewa(Nama_Lengkap, Daftar_Kamar, Data_Admin):
    Unit = None
    for Nomor_Kamar, Data_Kamar in Daftar_Kamar.items():
        if Data_Kamar["Nama Penghuni"] == Nama_Lengkap:
            Unit = Data_Kamar
            break

    # Apakah unit penyewa ditemukan?
    if Unit is None:
        print("Anda belum menyewa unit apa pun")
        print('=' * 40)
        input("Tekan Enter Untuk Kembali")
        return

    Tagihan_Sewa = Unit["Harga Unit"]

    Go_Back_Fitur_Pembayaran_Sewa = False
    while not Go_Back_Fitur_Pembayaran_Sewa:
        os.system('cls' if os.name == 'nt' else 'clear')

        # Tampilkan tagihan sewa
        print('=' * 40)
        print("PEMBAYARAN SEWA")
        print('=' * 40)
        print(f"Tagihan Sewa : Rp{Tagihan_Sewa:,}")
        print(f"Status Bayar : {Unit['Status Bayar Sewa']}")
        print('=' * 40)

        opsi = [
            inquirer.List("Opsi Pilih Bayar Sewa", message="Pilih Opsi", choices=["Bayar Sewa", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban is None:  # Ctrl+C
            break
        Hasil_Opsi = jawaban["Opsi Pilih Bayar Sewa"]

        if Hasil_Opsi == "Bayar Sewa":
            try:
                Uang_Bayar = int(input("Masukkan Uang Bayar : Rp"))
            except ValueError:
                Uang_Bayar = 0  # input bukan angka dianggap pembayaran gagal

            if Uang_Bayar >= Tagihan_Sewa:
                # Uang sewa masuk ke simpanan uang admin
                Data_Admin["Simpanan Uang"] += Tagihan_Sewa
                Unit["Status Bayar Sewa"] = "Sudah Bayar"
                print("Pembayaran berhasil")
                print('=' * 40)
                kembali = input("Tekan Enter Untuk Kembali")
            else:
                print("Pembayaran gagal")
                print('=' * 40)
                kembali = input("Tekan Enter Untuk Kembali")
        elif Hasil_Opsi == "Kembali":
            Go_Back_Fitur_Pembayaran_Sewa = True

