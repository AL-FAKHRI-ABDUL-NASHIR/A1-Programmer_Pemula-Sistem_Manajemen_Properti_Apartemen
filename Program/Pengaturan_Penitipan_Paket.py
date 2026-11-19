#Pesan untuk gw di masa depan, Ganti nama penerima soalnya yang ngakses admin bukan tenant
import os
import inquirer

from Data import Data_Paket 

list_paket = []

def Tampilkan_data_paket():
    size = len(Data_Paket)
    if size == 0:
        print ("Paket tidak ada!")
        return
    try:
        print ('=' * 55, "\n", ' ' * 20,
                "List Paket")
        for i in range (1, size+1):
            list_paket.append(str("Paket #" + str(i) + " "))
            print ("PAKET #", i, "\nNama Penerima    :", Data_Paket[i]['Nama Penerima'],
                                 "\nNama Paket       :", Data_Paket[i]['Nama Paket'],
                                 "\nStatus Paket     :", Data_Paket[i]['Status Paket'])
    except KeyError:
        print ("Tidak ada paket untuk saat ini")
        return False
    return True

def Pengaturan_Penitipan_Paket():
    Go_Back_Pengaturan_Penitipan_Paket = False
    while not Go_Back_Pengaturan_Penitipan_Paket:
        os.system("cls")
        Pilihan = list_paket
        if Tampilkan_data_paket() == False:
            Pilihan = ["Kembali"]
        else:
            Pilihan.append("Kembali")
            input ("Tekan 'Enter' untuk lanjut")
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
        else:
            break

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
            break
        elif Hasil_Opsi == "Kembali":
            break
    # else tidak ada paket
    print('=' * 40)

Pengaturan_Penitipan_Paket()