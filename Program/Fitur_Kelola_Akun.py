import os
import inquirer
import time
import json

with open("Program/Data.json", "r") as file:
    Data = json.load(file)

def Simpan_Data():
    with open("Program/Data.json", "w") as file:
        json.dump(Data, file, indent=4)

def Setup_Username_Baru_Penyewa():
    for i in Data["Data Akun"]:
        if Username_Baru == Data["Data Akun"][i]["Username"] or Username_Baru == Data["Username Admin"]:
            return "Username Sudah Ada"
    if not Username_Baru:
        return "Username Kosong"

def Setup_Password_Baru_Penyewa():
    if not Password_Baru:
        return "Password Kosong"

def Fitur_Kelola_Akun(Username_Log_In):
    global Username_Baru, Password_Baru
    while True:
        os.system("cls")
        print("=" * 40)
        print("KELOLA AKUN".center(40))
        print('=' * 40)
        for i in Data["Data Akun"]:
            if Username_Log_In == Data["Data Akun"][i]["Username"]:
                print(f'Username : {Data["Data Akun"][i]["Username"]}')
                print(f"Nama Lengkap : {Data["Data Akun"][i]["Nama Lengkap"]}")
                print(f"No. Hp : {Data["Data Akun"][i]["No. Hp"]}")
                print(f"Unit Sewa : {Data["Data Akun"][i]["Unit Sewa"]}")
                print(f"Status Bayar Sewa : {Data["Data Akun"][i]["Status Bayar Sewa"]}")
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
                if Setup_Username_Baru_Penyewa() == "Username Sudah Ada":
                    os.system("cls")
                    print("=====Username sudah digunakan=====")
                    time.sleep(1)
                    break
                elif Setup_Username_Baru_Penyewa() == "Username Kosong":
                    os.system("cls")
                    print("=====Input tidak boleh kosong=====")
                    time.sleep(1)
                    break
                else:
                    for i in Data["Data Akun"]:
                        if Username_Log_In == Data["Data Akun"][i]["Username"]:
                            Data["Data Akun"][i]["Username"] = Username_Baru
                            Username_Log_In = Username_Baru
                            Simpan_Data()
                            print("Username berhasil diganti!")
                            print('=' * 40)
                            input("Tekan Enter Untuk Kembali")
                            break
            elif Hasil_Opsi == "Tidak":
                pass

        if Hasil_Opsi == "Ubah Password":
            Verifikasi_Password = input("Masukkan password akun anda sekarang : ")
            for i in Data["Data Akun"]:
                if Username_Log_In == Data["Data Akun"][i]["Username"]:
                    if Verifikasi_Password == Data["Data Akun"][i]["Password"]:
                        Password_Baru = input("Masukkan Password Baru : ").strip()
                        opsi = [
                            inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengganti dengan password ini?", choices=["Ya", "Tidak"])
                        ]
                        jawaban = inquirer.prompt(opsi)
                        Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
                        if Hasil_Opsi == "Ya":
                            if Setup_Password_Baru_Penyewa() == "Password Kosong":
                                os.system("cls")
                                print("=====Input tidak boleh kosong=====")
                                time.sleep(1)
                                break
                            else:
                                for i in Data["Data Akun"]:
                                    if Username_Log_In == Data["Data Akun"][i]["Username"]:
                                        Data["Data Akun"][i]["Password"] = Password_Baru
                                        Simpan_Data()
                                        print("Password telah diganti")
                                        print('=' * 40)
                                        input("Tekan Enter Untuk Kembali")
                                        break
                        elif Hasil_Opsi == "Tidak":
                            pass
                    else:
                        os.system("cls")
                        print("=====Password salah. Akses ditolak=====")
                        time.sleep(1)

        elif Hasil_Opsi == "Kembali":
            break