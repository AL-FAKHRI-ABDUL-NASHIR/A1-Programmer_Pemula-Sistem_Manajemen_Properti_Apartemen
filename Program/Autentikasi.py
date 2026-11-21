import os
import inquirer
import time
import maskpass

import Data
import Menu_Utama_Admin
import Menu_Utama_Penyewa

def Setup_Log_In_Admin():
    if Username_Log_In == Data.Username_Admin and Password_Log_In == Data.Password_Admin:
        return True

def Setup_Log_In_Penyewa():
    for i in Data.Data_Akun:
        if Username_Log_In == Data.Data_Akun[i]["Username"] and Password_Log_In == Data.Data_Akun[i]["Password"]:
            return True

def Menu_Autentikasi():
    Go_Back_Autentikasi = False
    while not Go_Back_Autentikasi:
        os.system("cls")
        opsi = [
            inquirer.List("Opsi Pilih Menu Autentikasi", message="Pilih Opsi", choices=["Log In", "Sign In", "Keluar"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Menu Autentikasi"]
        if Hasil_Opsi == "Log In":
            Menu_Log_In()
        elif Hasil_Opsi == "Sign In":
            Menu_Sign_In()
        elif Hasil_Opsi == "Keluar":
            Go_Back_Autentikasi = True

def Menu_Log_In():
    global Username_Log_In, Password_Log_In
    print("=" * 40)
    print("LOG IN AKUN".center(40))
    print("=" * 40)
    Username_Log_In = input("Masukkan Username : ").strip()    
    print("Masukkan Password : ", end="")
    Password_Log_In = maskpass.advpass(prompt="", mask="*")
    os.system("cls")
    opsi = [
        inquirer.List("Opsi Pilih Menu Log In", message="Apakah Anda ingin masuk?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Menu Log In"]
    if Hasil_Opsi == "Ya":
        if Setup_Log_In_Admin():
            print("Login berhasil!")
            print('=' * 40)
            Lanjut = input("Tekan Enter Untuk Lanjut")
            Menu_Utama_Admin.Menu_Utama_Admin()
        elif Setup_Log_In_Penyewa():
            print("Login berhasil!")
            print('=' * 40)
            Lanjut = input("Tekan Enter Untuk Lanjut")
            Menu_Utama_Penyewa.Menu_Utama_Penyewa(Username_Log_In)
        else:
            os.system("cls")
            print("=====Login Gagal=====")
            time.sleep(1)
    elif Hasil_Opsi == "Tidak":
        pass

def Menu_Sign_In():
    os.system("cls")
    print("=" * 40)
    print("SIGN IN AKUN".center(40))
    print("=" * 40)
    Username_Sign_In = input("Masukkan Username : ").strip()    
    Password_Sign_In = input("Masukkan Password : ").strip()
    Nama_Lengkap = input("Masukkan Nama Lengkap : ").strip() 
    No_Hp = input("Masukkann Nomor Hp : ").strip()
    opsi = [
        inquirer.List("Opsi Pilih Menu Sign In", message="Simpan Akun?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Menu Sign In"]
    if Hasil_Opsi == "Ya":
        for i in Data.Data_Akun:
            if Username_Sign_In == Data.Data_Akun[i]["Username"] or Username_Sign_In == Data.Username_Admin:
                os.system("cls")
                print("=====Username sudah digunakan=====")
                time.sleep(1)
                break
            elif not Username_Sign_In or not Password_Sign_In or not Nama_Lengkap or not No_Hp:
                os.system("cls")
                print("=====Input tidak boleh kosong=====")
                time.sleep(1)
                break
            else:
                ID_Baru = next(reversed(Data.Data_Akun)) + 1
                Data.Data_Akun[ID_Baru] = {
                    "Username" : Username_Sign_In,
                    "Password" : Password_Sign_In,
                    "Nama Lengkap" : Nama_Lengkap,
                    "No. Hp" : No_Hp,
                    "Unit Sewa" : "-",
                    "Status Bayar Sewa" : "-"
                }
                print(Data.Data_Akun)
                input()
                break
    elif Hasil_Opsi == "Tidak":
        pass