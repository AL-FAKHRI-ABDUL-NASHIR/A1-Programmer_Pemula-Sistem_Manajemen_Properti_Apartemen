import os
import inquirer
import time

from Data import Data_Paket

def cek_spesial(huruf):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if any(c in special_characters for c in huruf):
        return True
    else:
        return False
    # Response: yes

def susun_ulang_data_paket():
    list_paket = [Data_Paket[k] for k in sorted(Data_Paket)]
    Data_Paket.clear()
    for nomor, paket in enumerate(list_paket, start=1):
        Data_Paket[nomor] = paket

def Tampilkan_data_paket(Nama_User):
    size = len(Data_Paket)
    if size == 0:
        print ("Paket tidak ada!")
        return
    try:
        paket_personal_ada = False
        print ('=' * 55, "\n", ' ' * 20,
                "List Paket")
        #i = kunci, paket = DataPaket[i](kunci diksi dalam diksi)
        personal_paket_count = 0
        for i, paket in Data_Paket.items():
            if Nama_User == paket['Nama Penerima']:
                paket_personal_ada = True
                personal_paket_count += 1
                print ("PAKET #", personal_paket_count, 
                        "\nNama Penerima    :", paket['Nama Penerima'],
                        "\nNama Paket       :", paket['Nama Paket'],
                        "\nStatus Paket     :", paket['Status Paket'])
        if not paket_personal_ada:
            print("       Saat ini, anda tidak sedang menitipkan paket!")
        
    except KeyError:
        print ("Terjadi Kesalahan! Silahkan Coba Lagi!")

def Buat_Form(Nama_User):
    while True:
        try:
            nama_paket = input("Masukkan Nama Paket: ")
            if nama_paket is None or not nama_paket.strip():
                            print ("Nama Paket Tidak Boleh Kosong!")
                            input ("Silahkan Coba Lagi! ")
                            break
            elif cek_spesial(nama_paket):
                print("Nama Paket Tidak Boleh Selain Huruf Atau Angka!")
                input ("Silahkan Coba Lagi! ")
                break

            temporary_paket = {"Nama Penerima" : Nama_User,
                            "Nama Paket"    : nama_paket,
                            "Status Paket"  : "Belum Sampai"}

            opsi = [
                inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin membuat form dengan nama ini?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            jawaban = jawaban["Opsi Pilih Konfirmasi"]
            if jawaban == "Tidak":
                break
            
            
            elif nama_paket == "n":
                print("Aksi Dibatalkan")
                input('Tekan Enter Untuk Kembali') 
                break
            else:
                print("Form telah dibuat")
                print('=' * 40)
                input('Tekan Enter Untuk Kembali') 
                Data_Paket[len(Data_Paket) + 1] = temporary_paket
                break
        except KeyError:
            print("Something Went Wrong")

def Fitur_Penitipan_Paket(Nama_User):
    while True:
        os.system("cls")
        opsi = [
            inquirer.List("Opsi Pilih Fitur Penitipan Paket", message="Pilih Opsi", choices=["Buat Form", "Status Paket", "Hapus Form", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        jawaban = jawaban["Opsi Pilih Fitur Penitipan Paket"]
        if jawaban == "Buat Form":
            Buat_Form(Nama_User)
        elif jawaban == "Status Paket":
            Status_Paket(Nama_User)
        elif jawaban == "Hapus Form":
            Hapus_Form(Nama_User)
        elif jawaban == "Kembali":
            break


def Status_Paket(Nama_User):
    try:
        Tampilkan_data_paket(Nama_User)
        print('=' * 40)
        input('Tekan Enter Untuk Kembali')
    except ValueError:
        print("ValueError") 

def proses_penghapusan_paket(Nama_User):
    try:
        Tampilkan_data_paket(Nama_User)
        print (f"=" * 40)
        list_paket_user = []
        count = 0
        for value in Data_Paket:
            if Data_Paket[value]["Nama Penerima"] == Nama_User:
                count += 1
                list_paket_user.append(f"Paket # {count}")
        count = 0
                
        opsi = [
            inquirer.List("Opsi Paket Yang Ingin Dihapus", message="Pilih Form Paket Yang Ingin Dihapus", choices=list_paket_user)
        ]
        jawaban = inquirer.prompt(opsi)
        jawaban = jawaban["Opsi Paket Yang Ingin Dihapus"]
        kunci_data_paket = int(jawaban[7:])

        opsi = [
            inquirer.List("Konfirmasi Penghapusan", message="Apakah Anda Yakin Ingin Menghapus Form Ini?", choices=["Iya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        jawaban = jawaban["Konfirmasi Penghapusan"]

        if jawaban == "Tidak":
            print ("Aksi Dibatalkan")
            return False
        print("Menghapus Form...")
        del Data_Paket[kunci_data_paket]
        susun_ulang_data_paket()
        time.sleep(1.5)
        os.system("cls")
        print("Form Telah Dihapus")
        input('Tekan Enter Untuk Kembali')
    except KeyError:
        print ("Somethin went wrong")
        input('Tekan Enter Untuk Kembali')



def Hapus_Form(Nama_User):
    while True:
        form = True
        if form == False:        
                print("Belum ada form yang dibuat")
                print('=' * 40)
                input('Tekan Enter Untuk Kembali')
                break
        else:
            if proses_penghapusan_paket(Nama_User) == False:
                input('Tekan Enter Untuk Kembali')
                break
        break



