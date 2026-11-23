# Catatan: kolom "Nama Penerima" tetap ada, tapi yang mengakses adalah admin (bukan tenant)
import os
import time
import inquirer
from prettytable import PrettyTable

from Data import Data_Paket


def susun_ulang_data_paket():
    list_paket = [Data_Paket[k] for k in sorted(Data_Paket)]
    Data_Paket.clear()
    for nomor, paket in enumerate(list_paket, start=1):
        Data_Paket[nomor] = paket


def Tampilkan_data_paket():
    print("=========================================================")
    print("                      LIST PAKET                         ")
    print("=========================================================")
    if len(Data_Paket) == 0:
        print("Belum Ada Paket Yang Dititipkan")
        return False
    tabelPaket = PrettyTable()
    tabelPaket.field_names = ["No Paket", "Nama Penerima", "Nama Paket", "Status Paket"]
    for nomor, paket in sorted(Data_Paket.items()):
        tabelPaket.add_row([nomor,
                            paket['Nama Penerima'],
                            paket['Nama Paket'],
                            paket['Status Paket']])
    print(tabelPaket)
    return True


def Pengaturan_Penitipan_Paket():
    while True:
        os.system("cls")
        Ada_Paket = Tampilkan_data_paket()

        if not Ada_Paket:
            print('=' * 40)
            input('Tekan Enter Untuk Kembali')
            break

        # pilih paket (label, nilai): nilai = nomor paket, None = kembali
        Pilihan = [("Paket #" + str(nomor), nomor) for nomor in sorted(Data_Paket)]
        Pilihan.append(("Kembali", None))
        opsi = [
            inquirer.List("Pilih Paket", message="Pilih Paket", choices=Pilihan)
        ]
        jawaban = inquirer.prompt(opsi)
        Nomor_Paket = jawaban["Pilih Paket"]
        if Nomor_Paket is None:
            break

        # tampilkan paket yang dipilih
        paket = Data_Paket[Nomor_Paket]
        os.system("cls")
        print("=========================================================")
        print("                    DETAIL PAKET                         ")
        print("=========================================================")
        print("No Paket       :", Nomor_Paket)
        print("Nama Penerima  :", paket['Nama Penerima'])
        print("Nama Paket     :", paket['Nama Paket'])
        print("Status Paket   :", paket['Status Paket'])
        print('=' * 40)

        # ubah status sampai / belum
        opsi = [
            inquirer.List("Sampai", message="Apakah paket sudah sampai?", choices=["Ya", "Tidak", "Batal"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil = jawaban["Sampai"]

        if Hasil == "Batal":
            continue
        elif Hasil == "Tidak":
            paket['Status Paket'] = "Belum Sampai"
            print("Status Paket Diubah Menjadi Belum Sampai")
            print('=' * 40)
            input('Tekan Enter Untuk Kembali')
            continue

        # Hasil == "Ya"
        paket['Status Paket'] = "Sudah Sampai"

        # konfirmasi paket sudah diterima pemesan
        opsi = [
            inquirer.List("Diterima", message="Apakah paket sudah diterima oleh pemesan?", choices=["Ya", "Tidak"])
        ]
        jawaban = inquirer.prompt(opsi)
        if jawaban["Diterima"] == "Ya":
            print("Menghapus Form...")
            time.sleep(1.5)
            del Data_Paket[Nomor_Paket]
            susun_ulang_data_paket()
            print("Paket Telah Diterima, Form Berhasil Dihapus")
        else:
            print("Status Sampai Tersimpan, Paket Belum Diterima Pemesan")
        print('=' * 40)
        input('Tekan Enter Untuk Kembali')