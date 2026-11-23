import os
import inquirer

import Data

def Fitur_Pembayaran_Sewa(Nama_Lengkap):
    Unit = None
    for i, Data_Kamar in Data.Data_Unit.items():
        if Data_Kamar['Nama Penghuni'] == Nama_Lengkap:
            Unit = Data_Kamar

    # Apakah unit penyewa ditemukan?
    if Unit is None:
        print("Anda belum menyewa unit apa pun")
        print('=' * 40)
        input("Tekan Enter Untuk Kembali")
        return

    Tagihan_Sewa = int(Unit["Harga"])

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        # Tampilkan tagihan sewa
        print('=' * 40)
        print("PEMBAYARAN SEWA")
        print('=' * 40)
        print(f"Tagihan Sewa : Rp{Tagihan_Sewa}")
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
            if Unit["Status Bayar Sewa"] == "Sudah Bayar":
                print("Anda Sudah Bayar Sewa Bulan Ini!")
                print('=' * 40)
                input("Tekan Enter Untuk Kembali")
                break
            try:
                Uang_Bayar = int(input("Masukkan Uang Bayar : Rp"))
            except ValueError:
                Uang_Bayar = 0  # input bukan angka dianggap pembayaran gagal

            if Uang_Bayar >= Tagihan_Sewa:
                kembalian = Uang_Bayar - Tagihan_Sewa
                Data.Simpanan_Uang_Admin += Tagihan_Sewa
                Unit["Status Bayar Sewa"] = "Sudah Bayar"
                print("Pembayaran berhasil")
                print(f"Kembalian anda ialah Rp.{kembalian}")
                print('=' * 40)
                input("Tekan Enter Untuk Kembali")
            else:
                print("Pembayaran gagal, Uang Anda Tidak Cukup!")
                print('=' * 40)
                input("Tekan Enter Untuk Kembali")
        elif Hasil_Opsi == "Kembali":
            break