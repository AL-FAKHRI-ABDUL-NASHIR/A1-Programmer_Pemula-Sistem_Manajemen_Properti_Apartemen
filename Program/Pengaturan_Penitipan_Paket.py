import os
import inquirer

from Data import Data_Paket 

def Tampilkan_data_paket():
    size = len(Data_Paket)
    print(size)

def Pengaturan_Penitipan_Paket(Nama_Penerima):
    Go_Back_Pengaturan_Penitipan_Paket = False
    while not Go_Back_Pengaturan_Penitipan_Paket:
        os.system("cls")
        Tampilkan_data_paket()
        paket = True
        opsi = [
            inquirer.List("Opsi Pilih Pengaturan Penitipan Paket", message="Pilih Opsi", choices=["Pilih Paket", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Pengaturan Penitipan Paket"]
        if Hasil_Opsi == "Pilih Paket":
            print("Pilihan Paket")
        elif Hasil_Opsi == "Kembali":
            break
        opsi = [
            inquirer.List("Opsi Pilih Paket Sampai", message="Apakah paket sudah sampai?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Paket Sampai"]
        if Hasil_Opsi == "Ya":
            print("Kondisi Paket")
        opsi = [
            inquirer.List("Opsi Pilih Paket Diterima", message="Apakah paket sudah diterima?", choices=["Ya", "Tidak"])
            ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Paket Diterima"]
        if Hasil_Opsi == "Ya":
            # di sini program menghapus form penitipan paket
            print("Form telah dihapus")
            print('=' * 40)
            kembali = input('Tekan Enter Untuk Kembali')  
            Go_Back_Pengaturan_Penitipan_Paket = True
        elif Hasil_Opsi == "Kembali":
            Go_Back_Pengaturan_Penitipan_Paket = True
    # else tidak ada paket
    print("Unit berhasil ditambahkan")
    print('=' * 40)
    input('Tekan Enter Untuk Kembali') #rafa: Menghapus Variabel keluar

Pengaturan_Penitipan_Paket("Om anton pelari kalcer")       