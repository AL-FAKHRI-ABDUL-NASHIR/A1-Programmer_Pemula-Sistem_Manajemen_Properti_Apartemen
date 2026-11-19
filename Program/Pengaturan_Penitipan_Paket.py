#Pesan untuk gw di masa depan, Ganti nama penerima soalnya yang ngakses admin bukan tenant
import os
import inquirer

from Data import Data_Paket 

def Tampilkan_data_paket():
    size = len(Data_Paket)
    if size == 0:
        print ("Paket tidak ada!")
        return
    try:
        print ('=' * 55, "\n", ' ' * 20,
                "List Paket")
        for i in range (1, size+1):
            print ("PAKET #", i, "\nNama Penerima    :", Data_Paket[i]['Nama Penerima'],
                                 "\nNama Paket       :", Data_Paket[i]['Nama Paket'],
                                 "\nStatus Paket     :", Data_Paket[i]['Status Paket'])
    except KeyError:
        print ("Terjadi Kesalahan! Silahkan Coba Lagi!")
        return False
    return True

def Pengaturan_Penitipan_Paket():
    while True:
        Pilihan = [f"Paket #{i} " for i in Data_Paket]
        os.system("cls")
        if Tampilkan_data_paket() == False:
            Pilihan = ["Kembali"]
        else:
            Pilihan.append("Kembali")
            input ("Tekan 'Enter' untuk lanjut")
        
        opsi = [
                inquirer.List("Opsi Pilih Pengaturan Penitipan Paket", message="Pilih Opsi", choices=Pilihan)
            ]
        jawaban = inquirer.prompt(opsi)
        jawaban = jawaban["Opsi Pilih Pengaturan Penitipan Paket"]
        pilihan_paket = ""
        if jawaban == "Kembali":
            os.system("cls")
            break
        for i in range(len(Pilihan) - 1):
            if Pilihan[i] == jawaban:
                pilihan_paket = jawaban
                print(pilihan_paket)
                input()
                break

        os.system("cls")

        #Ubah Status Paket
        opsi = [
            inquirer.List("Opsi Pilih Paket Sampai", message="Apakah paket sudah sampai?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        jawaban = jawaban["Opsi Pilih Paket Sampai"]

        if jawaban == "Ya":
            print(Data_Paket[2]['Status Paket'])
            input()
        else:
            break
        os.system("cls")

        #Hapus Form Jika Paket sudah diterima
        opsi = [
            inquirer.List("Opsi Pilih Paket Diterima", message="Apakah paket sudah diterima?", choices=["Ya", "Tidak"])
            ]
        
        jawaban = inquirer.prompt(opsi)
        jawaban = jawaban["Opsi Pilih Paket Diterima"]
        if jawaban == "Ya":
            # di sini program menghapus form penitipan paket
            print("Form telah dihapus")
            print('=' * 40)
            input('Tekan Enter Untuk Kembali')
        elif jawaban == "Tidak":
            print("Silahkan Menunggu Kedatangan Paket Anda!")
            print('=' * 40)
            input('Tekan Enter Untuk Kembali')
    # else tidak ada paket
    print('=' * 40)
    os.system("cls")

Pengaturan_Penitipan_Paket()