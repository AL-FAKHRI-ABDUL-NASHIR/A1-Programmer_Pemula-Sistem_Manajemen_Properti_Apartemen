import os
import time
import inquirer
from prettytable import PrettyTable

from Data import Data_Unit
from Data import Daftar_Pembayaran

def Pengaturan_Pembayaran_Sewa():
    while True:
        os.system("cls")
        print("=========================================================================================")
        print("                                PENGATURAN PEMBAYARAN SEWA                               ")
        print("=========================================================================================")

        tabelUnit = PrettyTable()
        tabelUnit.field_names = ["Nomor Unit", "Nama Penghuni", "Nomor Kontak", "Harga Unit", "Status Pembayaran"]
        for Nomor_Unit, dataUnit in Data_Unit.items():
            if dataUnit['Status Unit'] == "Terisi":
                Status_Bayar = Daftar_Pembayaran.get(Nomor_Unit, "Belum")
                tabelUnit.add_row([Nomor_Unit,
                                   dataUnit['Nama Penghuni'],
                                   dataUnit['Nomor Kontak'],
                                   dataUnit['Harga Unit'],
                                   Status_Bayar
                                   ])
        print(tabelUnit)
        print("Masukkan 0 Untuk Kembali")

        try:
            Nomor_Unit = input("Masukkan Nomor Unit Penyewa: ")
            if Nomor_Unit == "0":
                break
            if Nomor_Unit not in Data_Unit:
                os.system("cls")
                print("Nomor Unit Tidak Ada Di Dalam Daftar")
                time.sleep(1)
                continue
            elif Data_Unit[Nomor_Unit]['Status Unit'] != "Terisi":
                os.system("cls")
                print("Unit Tersebut Tidak Memiliki Penyewa")
                time.sleep(1)
                continue
            else:
                dataUnit = Data_Unit[Nomor_Unit]
                Status_Bayar = Daftar_Pembayaran.get(Nomor_Unit, "Belum")
                os.system("cls")
                print("Nomor Unit        :", Nomor_Unit)
                print("Tipe Unit         :", dataUnit['Tipe Unit'])
                print("Harga Unit        :", dataUnit['Harga Unit'])
                print("Nama Penghuni     :", dataUnit['Nama Penghuni'])
                print("Nomor Kontak      :", dataUnit['Nomor Kontak'])
                print("Status Pembayaran :", Status_Bayar)
                print('=' * 40)

                if Status_Bayar == "Sudah":
                    print("Pembayaran sewa telah lunas")
                    print('=' * 40)
                    kembali = input('Tekan Enter Untuk Kembali')
                    break
                else:
                    opsi = [
                        inquirer.List("Opsi Pilih Pesan Pengingat", message="Pilih Opsi", choices=["Kirim Pesan Pengingat", "Kembali"])
                    ]
                    jawaban = inquirer.prompt(opsi)
                    Hasil_Opsi = jawaban["Opsi Pilih Pesan Pengingat"]
                    if Hasil_Opsi == "Kirim Pesan Pengingat":
                        Pesan = input("Masukkan Pesan Pengingat: ")
                        opsi = [
                            inquirer.List("Opsi Pilih Konfirmasi", message="Kirim pesan pengingat ke penyewa?", choices=["Ya", "Tidak"])
                        ]
                        jawaban = inquirer.prompt(opsi)
                        Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
                        if Hasil_Opsi == "Ya":
                            # di sini program mengirim pesan ke penyewa
                            print("Pesan berhasil terkirim")
                            print('=' * 40)
                            kembali = input('Tekan Enter Untuk Kembali')
                            break
                        else:
                            break
                    else:
                        break
        except ValueError:
            os.system("cls")
            print("Harap Masukkan Nomor Yang Valid")
            time.sleep(1)
            continue
