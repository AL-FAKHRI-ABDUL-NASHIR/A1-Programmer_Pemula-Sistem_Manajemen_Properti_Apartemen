import os
import inquirer
import time

import Data

def Pengaturan_Kelola_Akun():
    Go_Back_Pengaturan_Kelola_Akun = False
    while not Go_Back_Pengaturan_Kelola_Akun:
        os.system("cls")
        print("=" * 40)
        print("KELOLA AKUN".center(40))
        print('=' * 40)
        print(f'Username : {Data.Username_Admin}')
        print(f'Simpanan Uang : Rp{Data.Simpanan_Uang_Admin:,}'.replace("," , "X").replace("." , ",").replace("X" , "."))
        opsi = [
            inquirer.List("Opsi Pilih Pengaturan Kelola Akun", message="Pilih Opsi", choices=["Ubah Username", "Ubah Password", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Pengaturan Kelola Akun"]

        if Hasil_Opsi == "Ubah Username":
            Username_Baru = input("Masukkan Username Baru : ").strip()
            opsi = [
                inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengganti dengan username ini?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
            if Hasil_Opsi == "Ya":
                for i in Data.Data_Akun:
                    if Username_Baru == Data.Data_Akun[i]["Username"]:
                        os.system("cls")
                        print("=====Username sudah digunakan=====")
                        time.sleep(1)
                        break
                    elif not Username_Baru:
                        os.system("cls")
                        print("=====Input tidak boleh kosong=====")
                        time.sleep(1)
                        break
                    else:
                        Data.Username_Admin = Username_Baru
                        print("Username berhasil diganti!")
                        print('=' * 40)
                        kembali = input("Tekan Enter Untuk Kembali")
            elif Hasil_Opsi == "Tidak":
                pass
                
        elif Hasil_Opsi == "Ubah Password":
            Verifikasi_Password = input("Masukkan password akun anda sekarang : ")
            if Verifikasi_Password == Data.Password_Admin:
                Password_Baru = input("Masukkan Password Baru : ").strip()
                opsi = [
                    inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengganti dengan password ini?", choices=["Ya", "Tidak"])
                ]
                jawaban = inquirer.prompt(opsi)
                Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
                if Hasil_Opsi == "Ya":
                    if not Password_Baru:
                        os.system("cls")
                        print("=====Input tidak boleh kosong=====")
                        time.sleep(1)
                        break
                    else:
                        Data.Password_Admin = Username_Baru
                        print("Password berhasil diganti!")
                        print('=' * 40)
                        kembali = input("Tekan Enter Untuk Kembali")
                elif Hasil_Opsi == "Tidak":
                    pass

        elif Hasil_Opsi == "Kembali":
            Go_Back_Pengaturan_Kelola_Akun = True