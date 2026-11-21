import os
import inquirer

from Data import Data_Paket

def Tampilkan_data_paket(Nama_Penerima):
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
            if Nama_Penerima == paket['Nama Penerima']:
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

def proses_pembuatan_form(Nama_Penerima):
    while True:
        try:
            nama_paket = input("Masukkan Nama Paket: ")
            temporary_paket = {"Nama Penerima" : Nama_Penerima,
                            "Nama Paket"    : nama_paket,
                            "Status Paket"  : "Belum Sampai"}
            if nama_paket == "":
                print ("Nama Paket Tidak Boleh Kosong!")
            elif nama_paket == "n":
                print("Aksi Dibatalkan")
                input('Tekan Enter Untuk Kembali') 
                break
            #Kondisi jika user mo kluar tambahin OM
            else:
                print("Form telah dibuat")
                print('=' * 40)
                input('Tekan Enter Untuk Kembali') 
                break
        except KeyError:
            print("Something Went Wrong")
    Data_Paket[len(Data_Paket)] = temporary_paket

def Fitur_Penitipan_Paket(Nama_User):
    while True:
        os.system("cls")
#       # di sini tampilkan judul
#       # di sini program menampilkan daftar form dari semua form paket yang telah dibuat
        opsi = [
            inquirer.List("Opsi Pilih Fitur Penitipan Paket", message="Pilih Opsi", choices=["Buat Form", "Status Paket", "Hapus Form", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Fitur Penitipan Paket"]
        if Hasil_Opsi == "Buat Form":
            Buat_Form(Nama_User)
        elif Hasil_Opsi == "Status Paket":
            Status_Paket(Nama_User)
        elif Hasil_Opsi == "Hapus Form":
            Hapus_Form(Nama_User)
        elif Hasil_Opsi == "Kembali":
            break

def Buat_Form(Nama_User):
    # di sini program input form
    opsi = [
        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin membuat form ini?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)
    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
    if Hasil_Opsi == "Ya":
#       # di sini program simpan form ke Data_Paket
        proses_pembuatan_form(Nama_User) 
    elif Hasil_Opsi == "Tidak":
        pass

def Status_Paket(Nama_User):
    try:
        Tampilkan_data_paket(Nama_User)
        print('=' * 40)
        input('Tekan Enter Untuk Kembali')
    except ValueError:
        print("ValueError") 

def proses_penghapusan_paket(Nama_User):
    try:
        opsi = [
            
        ]
        jawaban = inquirer.prompt(opsi)
        jawaban = jawaban["Opsi Pilih Paket Diterima"]
        print("Menghapus Form...")
        time.sleep(1.5)
        os.system("cls")
        # di sini program menghapus form penitipan paket
        del Data_Paket[kunci_data_paket]
        susun_ulang_data_paket()
        print("Form telah dihapus")
        print('=' * 40)
        input('Tekan Enter Untuk Kembali')
        print('=' * 40)
        os.system("cls")
    except KeyError:
        print ("Somethin wenr wrong")


def Hapus_Form(Nama_User):
    while True:
        form = True
        if form == False:        
                print("Belum ada form yang dibuat")
                print('=' * 40)
                input('Tekan Enter Untuk Kembali')
                break
        opsi = [
            inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menghapus form ini?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
        if Hasil_Opsi == "Ya":
            proses_penghapusan_paket(Nama_User)
            print("Form berhasil Dihapus")
        elif Hasil_Opsi == "Tidak":
            print("Aksi Dibatalkan.")
        print('=' * 40)
        input('Tekan Enter Untuk Kembali')  
        break
    
