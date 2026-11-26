import os
import inquirer

import Fitur_Unit
import Fitur_Penitipan_Paket
import Fitur_Pembayaran_Sewa
import Fitur_Kelola_Akun

def Menu_Utama_Penyewa(Username_Log_In, Kontak_User):
    while True:
        os.system("cls")
        print("=" * 110)
        print("MENU UTAMA PENYEWA".center(110))
        print("=" * 110)
        opsi = [
            inquirer.List("Opsi Pilih Menu Utama Penyewa", message="Pilih Opsi", choices=["Daftar Unit", "Penitipan Paket", "Pembayaran Sewa", "Kelola Akun", "Log Out"])
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban is None:
            return
        Hasil_Opsi = jawaban["Opsi Pilih Menu Utama Penyewa"]
        if Hasil_Opsi == "Daftar Unit":
            Fitur_Unit.Fitur_Unit(Username_Log_In, Kontak_User)
        elif Hasil_Opsi == "Penitipan Paket":
            Fitur_Penitipan_Paket.Fitur_Penitipan_Paket(Username_Log_In)
        elif Hasil_Opsi == "Pembayaran Sewa":
            Fitur_Pembayaran_Sewa.Fitur_Pembayaran_Sewa(Username_Log_In)
        elif Hasil_Opsi == "Kelola Akun":
            Fitur_Kelola_Akun.Fitur_Kelola_Akun(Username_Log_In)
        elif Hasil_Opsi == "Log Out":
            break