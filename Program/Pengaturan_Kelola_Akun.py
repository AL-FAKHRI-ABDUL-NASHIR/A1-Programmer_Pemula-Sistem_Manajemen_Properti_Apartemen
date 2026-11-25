import os
import inquirer
import time
import json

with open("Program/Data.json", "r") as file:
    Data = json.load(file)

def Simpan_Data():
    with open("Program/Data.json", "w") as file:
        json.dump(Data, file, indent=4)

def Setup_Username_Baru_Admin():
    for i in Data["Data Akun"]:
        if Username_Baru == Data["Data Akun"][i]["Username"]:
            return "Username Sudah Ada"
    if not Username_Baru:
        return "Username Kosong"

def Setup_Password_Baru_Admin():
    if not Password_Baru:
        return "Password Kosong"

def Pengaturan_Kelola_Akun():
    global Username_Baru, Password_Baru
    while True:
        os.system("cls")
        print("=" * 40)
        print("KELOLA AKUN".center(40))
        print('=' * 40)
        print(f'Username : {Data["Username Admin"]}')
        print(f'Simpanan Uang : Rp{Data["Simpanan Uang Admin"]:,}'.replace("," , "X").replace("." , ",").replace("X" , "."))
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
                if Setup_Username_Baru_Admin() == "Username Sudah Ada":
                    os.system("cls")
                    print("=====Username sudah digunakan=====")
                    time.sleep(1)
                    break
                elif Setup_Username_Baru_Admin() == "Username Kosong":
                    os.system("cls")
                    print("=====Input tidak boleh kosong=====")
                    time.sleep(1)
                    break
                else:
                    Data["Username Admin"] = Username_Baru
                    Simpan_Data()
                    print("Username berhasil diganti!")
                    print('=' * 40)
                    input("Tekan Enter Untuk Kembali")
            elif Hasil_Opsi == "Tidak":
                pass
                
        elif Hasil_Opsi == "Ubah Password":
            Verifikasi_Password = input("Masukkan password akun anda sekarang : ")
            if Verifikasi_Password == Data["Password Admin"]:
                Password_Baru = input("Masukkan Password Baru : ").strip()
                opsi = [
                    inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin mengganti dengan password ini?", choices=["Ya", "Tidak"])
                ]
                jawaban = inquirer.prompt(opsi)
                Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
                if Hasil_Opsi == "Ya":
                    if Setup_Password_Baru_Admin() == "Password Kosong":
                        os.system("cls")
                        print("=====Input tidak boleh kosong=====")
                        time.sleep(1)
                        break
                    else:
                        Data["Password Admin"] = Username_Baru
                        Simpan_Data()
                        print("Password berhasil diganti!")
                        print('=' * 40)
                        input("Tekan Enter Untuk Kembali")
                elif Hasil_Opsi == "Tidak":
                    pass

        elif Hasil_Opsi == "Kembali":
            break