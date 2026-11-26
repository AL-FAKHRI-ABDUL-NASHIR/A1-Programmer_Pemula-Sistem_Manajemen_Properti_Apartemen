import os
import inquirer

import Data
from prettytable import PrettyTable

def Fitur_Unit():
    os.system("cls")
    while True:
        opsi = [
            inquirer.List("Opsi Pilih Fitur Unit", message="Pilih Opsi", choices=["Daftar Unit", "Unit Sewa Anda", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Fitur Unit"]
        if Hasil_Opsi == "Daftar Unit":
            Daftar_Unit()
        elif Hasil_Opsi == "Unit Sewa Anda":
            Unit_Sewa()
        elif Hasil_Opsi == "Kembali":
            return

def cek_ketersediaan_unit():
    list_kunci = []
    for keys, values in sorted(Data.Daftar_Unit.items()):
        if values["Status Unit"] != "Terisi":
            list_kunci.append(keys)
    if list_kunci is None:
        return None
    else:
        return list_kunci

def Lihat_Unit():
    try:
        os.system("cls")
        print("=========================================================================================")
        print("                       DAFTAR SELURUH UNIT YANG TERSEDIA                                 ")
        print("=========================================================================================")
        kunci = cek_ketersediaan_unit()
        print(kunci)
        input()
        if len(Data.Daftar_Unit) == 0:
            print("Belum Ada Data Unit Di Dalam Daftar")
            print()
        else:
            tabelUnit = PrettyTable()
            tabelUnit.field_names = ["Nomor Unit", "Tipe Unit", "Harga Unit", "Status Unit", "Nama Penghuni", "Nomor Kontak"]
                    
            for Nomor_Unit, dataUnit in sorted(Data.Daftar_Unit.items()):
                for isi in kunci:
                    if isi != Nomor_Unit:
                        continue
                    tabelUnit.add_row([Nomor_Unit,
                                        dataUnit['Tipe Unit'],
                                        dataUnit['Harga Unit'],
                                        dataUnit['Status Unit'],
                                        dataUnit['Nama Penghuni'],
                                        dataUnit['Nomor Kontak']
                                        ])
            print(tabelUnit)
        print()  
        print("=========================")
        input("Tekan Enter Untuk Kembali ")
    except KeyboardInterrupt:
        return

def Daftar_Unit():
    os.system("cls")
#   # di sini tampilkan daftar unit
    opsi = [
        inquirer.List("Opsi Pilih Informasi Unit", message="Apakah Anda ingin melihat informasi unit?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    if jawaban is None:
        return
    Hasil_Opsi = jawaban["Opsi Pilih Informasi Unit"]

    if Hasil_Opsi == "Tidak":
        os.system("cls")
        return
    os.system("cls")
    Lihat_Unit()
    opsi = [
        inquirer.List("Opsi Pilih Sewa Unit", message="Apakah Anda ingin memilih unit ini?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Sewa Unit"] if jawaban["Opsi Pilih Sewa Unit"] != 0 else 1
    
    if Hasil_Opsi == "Tidak":
        print("Aksi Dibatalkan")
        input("Tekan 'Enter' Untuk Kembali! ")
        os.system("cls")
        return
    os.system("cls")
    # di sini penyewa memilih unit
    opsi = [
        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menyewa unit ini?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
    if Hasil_Opsi == "Tidak":
        print("Aksi Dibatalkan")
        input("Tekan 'Enter' Untuk Kembali! ")
        os.system("cls")
        return
    os.system("cls")
    # di sini program input data penyewa yang akan di simpan di Data_Penyewa
    # di sini program bayar sewa awal bagi penyewa
    print("Unit berhasil disewa")
    print('=' * 40)
    input("Tekan Enter Untuk Kembali")
    os.system("cls")


def Unit_Sewa():
    os.system("cls")
    # di sini tampilkan daftar unit yang telah disewa
    # di sini penyewa memilih unit
    # di sini program menampilkan informasi dari Data_Unit berdasarkan unit yang telah dipilih
    opsi = [
        inquirer.List("Opsi Pilih Unit Sewa", message="Pilih Opsi", choices=["Batalkan Sewa", "Kembali"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Unit Sewa"]
    if Hasil_Opsi == "Kembali":
        os.system("cls")
    Hasil_Opsi = jawaban["Opsi Pilih Unit Sewa"]
    if Hasil_Opsi == "Batalkan Sewa":
        os.system("cls")
        opsi = [
            inquirer.List("Opsi Pilih Batalkan Sewa", message="Apakah Anda ingin membatalkan sewa unit ini?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Batalkan Sewa"]
    if Hasil_Opsi == "Ya":
        # di sini program membatalkan sewa (menghapus unit dari daftar unit sewa anda, mengubah informasi unit pada Data_Unit dari statusnya penuh menjadi tersedia)
        print("Sewa Unit berhasil dibatalkan")
        print('=' * 40)
        input("Tekan Enter Untuk Kembali")
        os.system("cls")
    elif Hasil_Opsi == "Tidak":
        print("Aksi Dibatalkan")
        input("Tekan 'Enter' Untuk Kembali! ")
        os.system("cls")