import os
import inquirer

from Data import Data_Paket 

def Tampilkan_data_paket(Nama_Penerima):
    size = len(Data_Paket)
    print ('=' * 40, "\n", ' ' * 20,
           "List Paket")
    try:
        for i in range (1, size+1):
            index_paket = str(Nama_Penerima + "_" + str(i))
            print ("Paket #", i, "\nNama Paket       :", Data_Paket[index_paket]['Nama Paket'],
                                "\nStatus Paket     :", Data_Paket[index_paket]['Status Paket'])
    except KeyError:
        print ("Tidak ada paket untuk anda")
        return False
    return True

def Pengaturan_Penitipan_Paket(Nama_Penerima):
    Go_Back_Pengaturan_Penitipan_Paket = False
    while not Go_Back_Pengaturan_Penitipan_Paket:
        os.system("cls")
        Pilihan = ["Pilih Paket", "Kembali"]
        if not Tampilkan_data_paket(Nama_Penerima):
            Pilihan.pop(0)
        opsi = [
                inquirer.List("Opsi Pilih Pengaturan Penitipan Paket", message="Pilih Opsi", choices=Pilihan)
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
    print('=' * 40)

Pengaturan_Penitipan_Paket("RafaxCode")