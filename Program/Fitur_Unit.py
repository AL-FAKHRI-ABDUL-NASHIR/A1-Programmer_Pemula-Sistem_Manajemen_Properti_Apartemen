import os
import inquirer

import Data
import time
from prettytable import PrettyTable

def Fitur_Unit():
    os.system("cls")
    try:
        while True:
            opsi = [
                inquirer.List("Opsi Pilih Fitur Unit", message="Pilih Opsi", choices=["Tampilkan Daftar Unit", "Unit Sewa Anda", "Kembali"])
            ]
            jawaban = inquirer.prompt(opsi)
            if jawaban is None:
                time.sleep(1.0)
                break
            Hasil_Opsi = jawaban["Opsi Pilih Fitur Unit"]
            if Hasil_Opsi == "Tampilkan Daftar Unit":
                Daftar_Unit()
            elif Hasil_Opsi == "Unit Sewa Anda":
                Unit_Sewa()
            elif Hasil_Opsi == "Kembali":
                return
    except KeyboardInterrupt:
        os.system("cls")
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
        if len(Data.Daftar_Unit) == 0 or kunci is None:
            print("Belum Ada Data Unit Di Dalam Daftar")
            input("Tekan 'Enter' untuk kembali")
            os.system("cls")
            return False
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
        print("=" * 89)
    except KeyboardInterrupt:
        os.system("cls")
        return False

def Daftar_Unit():
    try:
        os.system("cls")
        # di sini tampilkan daftar unit
        opsi = [
            inquirer.List("Opsi Pilih Informasi Unit", message="Apakah Anda ingin melihat informasi unit?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban is None:
            os.system("cls")
            return
        Hasil_Opsi = jawaban["Opsi Pilih Informasi Unit"]

        if Hasil_Opsi == "Tidak":
            os.system("cls")
            return
        os.system("cls")
        while True:
            if Lihat_Unit() == False:
                return
            try:
                Nomor_Unit = input("Masukkan Nomor Unit: ")
                Nomor_Unit = int(Nomor_Unit)
            except ValueError:
                os.system("cls")
                print("Harap masukkan nomor yang benar!")
                time.sleep(1.0)
            except KeyboardInterrupt:
                os.system("cls")
                return
            if not Nomor_Unit in Data.Daftar_Unit:
                os.system("cls")
                print("Nomor Unit tersebut tidak tersedia!")
                time.sleep(1.0)
            elif Nomor_Unit in Data.Daftar_Unit:
                os.system("cls")
                break
        os.system("cls")
        opsi = [
            inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menyewa unit ini?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban is None:
            time.sleep(1.0)
            os.system("cls")
            return
        Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
        if Hasil_Opsi == "Tidak":
            print("Aksi Dibatalkan")
            input("Tekan 'Enter' Untuk Kembali! ")
            os.system("cls")
            return
        os.system("cls")
        for nomorUnit, isi in sorted(Data.Daftar_Unit.items()):
            isi["Nama Penghuni"] 
            isi["Status Bayar Sewa"]
            isi["Nomor Kontak"]

        # di sini program bayar sewa awal bagi penyewa
        print("Unit berhasil disewa")
        print('=' * 40)
        input("Tekan Enter Untuk Kembali")
        os.system("cls")
    except KeyboardInterrupt:
        os.system("cls")
        return


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

Fitur_Unit()
