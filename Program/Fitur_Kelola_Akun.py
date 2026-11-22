import os
import inquirer
import time

import Data

def Fitur_Kelola_Akun(Username_Log_In):
    Go_Back_Pengaturan_Kelola_Akun = False
    while not Go_Back_Pengaturan_Kelola_Akun:
        os.system("cls")
        print("=" * 40)
        print("KELOLA AKUN".center(40))
        print('=' * 40)
        for i in Data.Data_Akun:
            if Username_Log_In == Data.Data_Akun[i]["Username"]:
                print(f'Username : {Data.Data_Akun[i]["Username"]}')
                print(f"Nama Lengkap : {Data.Data_Akun[i]["Nama Lengkap"]}")
                print(f"No. Hp : {Data.Data_Akun[i]["No. Hp"]}")
                print(f"Unit Sewa : {Data.Data_Akun[i]["Unit Sewa"]}")
                print(f"Status Bayar Sewa : {Data.Data_Akun[i]["Status Bayar Sewa"]}")
        print("=" * 40)
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
                    if Username_Baru == Data.Data_Akun[i]["Username"] or Username_Baru == Data.Username_Admin:
                        os.system("cls")
                        print("=====Input tidak boleh kosong=====")
                        time.sleep(1)
                        break
                    elif not Username_Baru:
                        os.system("cls")
                        print("=====Input tidak boleh kosong=====")
                        time.sleep(1)
                        break
                    else:
                        if Username_Log_In == Data.Data_Akun[i]["Username"]:
                            Data.Data_Akun[i]["Username"] = Username_Baru
                            Username_Log_In = Username_Baru
                            print("Username berhasil diganti!")
                            print('=' * 40)
                            Kembali = input("Tekan Enter Untuk Kembali")
                            break
            elif Hasil_Opsi == "Tidak":
                pass

        if Hasil_Opsi == "Ubah Password":
            Verifikasi_Password = input("Masukkan password akun anda sekarang : ")
            for i in Data.Data_Akun:
                if Username_Log_In == Data.Data_Akun[i]["Username"]:
                    if Verifikasi_Password == Data.Data_Akun[i]["Password"]:
                        Password_Baru = input("Masukkan Password Baru : ").strip()
                        opsi = [
                            inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengganti dengan password ini?", choices=["Ya", "Tidak"])
                        ]
                        jawaban = inquirer.prompt(opsi)
                        Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
                        if Hasil_Opsi == "Ya":
                            for i in Data.Data_Akun:
                                if not Password_Baru:
                                    os.system("cls")
                                    print("=====Input tidak boleh kosong=====")
                                    time.sleep(1)
                                    break
                                else:
                                    if Username_Log_In == Data.Data_Akun[i]["Username"]:
                                        Data.Data_Akun[i]["Password"] = Password_Baru
                                        print("Password telah diganti")
                                        print('=' * 40)
                                        Kembali = input("Tekan Enter Untuk Kembali")
                                        break
                        elif Hasil_Opsi == "Tidak":
                            pass
                    else:
                        os.system("cls")
                        print("=====Password salah. Akses ditolak=====")
                        time.sleep(1)

        elif Hasil_Opsi == "Kembali":
            Go_Back_Pengaturan_Kelola_Akun = True