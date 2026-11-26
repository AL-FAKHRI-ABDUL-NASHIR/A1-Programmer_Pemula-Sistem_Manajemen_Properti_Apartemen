import os
import time
import inquirer
import json

with open("Program/Data.json", "r") as file:
    Data = json.load(file)

def Simpan_Data():
    with open("Program/Data.json", "w") as file:
        json.dump(Data, file, indent=4)

def cari_id_user(Nama_Lengkap):
    for keys, value in Data["Data Akun"].items():
        if value['Username'] == Nama_Lengkap:
            return keys

def Fitur_Pembayaran_Sewa(Nama_Lengkap):
    while True:
        os.system("cls")
        print('=' * 110)
        print("PEMBAYARAN SEWA".center(110))
        print('=' * 110)
        Unit = None
        Unit_Keys = 0
        for i, Data_Kamar in Data["Daftar Unit"].items():
            if Data_Kamar['Nama Penghuni'] == Nama_Lengkap:
                Unit = Data_Kamar
                Unit_Keys = i

        # Apakah unit penyewa ditemukan?
        if Unit is None:
            print("Anda belum menyewa unit apa pun")
            print('-------------------------------')
            input("Tekan Enter Untuk Kembali")
            break
        else:
            Tagihan_Sewa = int(Unit["Harga Unit"])

            # Tampilkan tagihan sewa
            print(f"Tagihan Sewa : Rp{Tagihan_Sewa}")
            print(f"Status Bayar : {Unit['Status Bayar Sewa']}")
            print('=' * 110)

            opsi = [
                inquirer.List("Opsi Pilih Bayar Sewa", message="Pilih Opsi", choices=["Bayar Sewa", "Kembali"])
            ]
            jawaban = inquirer.prompt(opsi)
            if jawaban is None:
                break
            Hasil_Opsi = jawaban["Opsi Pilih Bayar Sewa"] 

            if Hasil_Opsi == "Bayar Sewa":
                if Unit["Status Bayar Sewa"] == "Sudah Bayar":
                    os.system("cls")
                    print("=====Anda Sudah Bayar Sewa Bulan Ini!=====")
                    time.sleep(1)
                try:
                    os.system("cls")
                    print('=' * 110)
                    print("PEMBAYARAN SEWA".center(110))
                    print('=' * 110)
                    print(f"Tagihan Sewa : Rp{Tagihan_Sewa}")
                    print(f"Status Bayar : {Unit['Status Bayar Sewa']}")
                    print('=' * 110)
                    Uang_Bayar = int(input("Masukkan Uang Bayar : Rp"))
                except ValueError:
                    Uang_Bayar = 0  # input bukan angka dianggap pembayaran gagal

                if Uang_Bayar >= Tagihan_Sewa:
                    os.system("cls")
                    kembalian = Uang_Bayar - Tagihan_Sewa
                    Data["Simpanan Uang Admin"] += Tagihan_Sewa
                    Data["Daftar Unit"][Unit_Keys]["Status Bayar Sewa"] = "Sudah Bayar"
                    kunci = cari_id_user(Nama_Lengkap)
                    Data["Data Akun"][kunci]["Status Bayar Sewa"] = "Sudah Bayar"
                    Data["Simpanan Uang Admin"] += Uang_Bayar
                    Simpan_Data()
                    print("Pembayaran berhasil")
                    print(f"Kembalian anda ialah Rp.{kembalian}")
                    print('------------------------------------')
                    input("Tekan Enter Untuk Kembali")
                else:
                    os.system("cls")
                    print("Pembayaran gagal, Uang Anda Tidak Cukup!")
                    time.sleep(1)
            elif Hasil_Opsi == "Kembali":
                break
