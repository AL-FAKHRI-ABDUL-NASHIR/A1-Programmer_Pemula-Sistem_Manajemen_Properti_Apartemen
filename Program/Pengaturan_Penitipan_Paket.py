# Catatan: kolom "Nama Penerima" tetap ada, tapi yang mengakses adalah admin (bukan tenant)
import os
import time
import inquirer
from prettytable import PrettyTable
import json

with open("Program/Data.json", "r") as file:
    Data = json.load(file)

def Simpan_Data():
    with open("Program/Data.json", "w") as file:
        json.dump(Data, file, indent=4)

def susun_ulang_data_paket():
    list_paket = [Data["Data Paket"][k] for k in sorted(Data["Data Paket"])]
    Data["Data Paket"].clear()
    for nomor, paket in enumerate(list_paket, start=1):
        Data["Data Paket"][nomor] = paket


def Tampilkan_data_paket():
    print("=" * 110)
    print("LIST PAKET".center(110))
    print("=" * 110)
    if len(Data["Data Paket"]) == 0:
        print("Belum Ada Paket Yang Dititipkan")
        return False
    tabelPaket = PrettyTable()
    tabelPaket.field_names = ["No Paket", "Nama Penerima", "Nama Paket", "Status Paket"]
    for nomor, paket in sorted(Data["Data Paket"].items()):
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
            print('-------------------------------')
            input('Tekan Enter Untuk Kembali')
            break

        # pilih paket (label, nilai): nilai = nomor paket, None = kembali
        Pilihan = [("Paket #" + str(nomor), nomor) for nomor in sorted(Data["Data Paket"])]
        Pilihan.append(("Kembali", None))
        opsi = [
            inquirer.List("Pilih Paket", message="Pilih Paket", choices=Pilihan)
        ]
        jawaban = inquirer.prompt(opsi)
        Nomor_Paket = jawaban["Pilih Paket"]
        if Nomor_Paket is None:
            break

        # tampilkan paket yang dipilih
        paket = Data["Data Paket"][Nomor_Paket]
        os.system("cls")
        print("=" * 110)
        print("DETAIL PAKET".center(110))
        print("=" * 110)
        tabelPaket = PrettyTable()
        tabelPaket.add_column("Keterangan", ["No Paket", "Nama Penerima", "Nama Paket", "Status Paket"])
        tabelPaket.add_column("Informasi", [Nomor_Paket, paket['Nama Penerima'], paket['Nama Paket'], paket['Status Paket']])
        tabelPaket.align = "l"
        tabelPaket.hrules = 1
        print(tabelPaket)
        print('=' * 110)

        # ubah status sampai / belum
        opsi = [
            inquirer.List("Sampai", message="Apakah paket sudah sampai?", choices=["Ya", "Tidak", "Batal"])
        ]
        jawaban = inquirer.prompt(opsi)
        Hasil = jawaban["Sampai"]

        if Hasil == "Batal":
            continue
        elif Hasil == "Tidak":
            os.system("cls")
            paket['Status Paket'] = "Belum Sampai"
            print("Status Paket Diubah Menjadi Belum Sampai")
            print('----------------------------------------')
            input('Tekan Enter Untuk Kembali')
            continue
        elif Hasil == "Ya":
            os.system("cls")
            paket['Status Paket'] = "Sudah Sampai"

            # konfirmasi paket sudah diterima pemesan
            print("=" * 110)
            print("DETAIL PAKET".center(110))
            print("=" * 110)
            tabelPaket = PrettyTable()
            tabelPaket.add_column("Keterangan", ["No Paket", "Nama Penerima", "Nama Paket", "Status Paket"])
            tabelPaket.add_column("Informasi", [Nomor_Paket, paket['Nama Penerima'], paket['Nama Paket'], paket['Status Paket']])
            tabelPaket.align = "l"
            tabelPaket.hrules = 1
            print(tabelPaket)
            print('=' * 110)
            opsi = [
                inquirer.List("Diterima", message="Apakah paket sudah diterima oleh pemesan?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            if jawaban["Diterima"] == "Ya":
                os.system("cls")
                print("Menghapus Form...")
                time.sleep(2)
                del Data["Data Paket"][Nomor_Paket]
                os.system("cls")
                susun_ulang_data_paket()
                print("Paket Telah Diterima, Form Berhasil Dihapus")
                print('-------------------------------------------')
            else:
                print("Status Sampai Tersimpan, Paket Belum Diterima Pemesan")
                print('-----------------------------------------------------')
            input('Tekan Enter Untuk Kembali')