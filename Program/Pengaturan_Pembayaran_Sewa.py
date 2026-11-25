import os
import time
import inquirer
from prettytable import PrettyTable

from Data import Daftar_Unit

def Pengaturan_Pembayaran_Sewa():
    while True:
        os.system("cls")
        print("=========================================================================================")
        print("                                PENGATURAN PEMBAYARAN SEWA                               ")
        print("=========================================================================================")

        tabelUnit = PrettyTable()
        tabelUnit.field_names = ["Nomor Unit", "Nama Penghuni", "Nomor Kontak", "Harga Unit", "Status Pembayaran"]
        for Nomor_Unit, dataUnit in Daftar_Unit.items():
            if dataUnit['Status Unit'] == "Terisi":
                tabelUnit.add_row([Nomor_Unit,
                                   dataUnit['Nama Penghuni'],
                                   dataUnit['Nomor Kontak'],
                                   dataUnit['Harga Unit'],
                                   dataUnit['Status Bayar Sewa']
                                   ])
        print(tabelUnit)
        print("Masukkan 0 Untuk Kembali")

        try:
            Nomor_Unit = input("Masukkan Nomor Unit Penyewa: ")
            if Nomor_Unit == "0":
                break
            if Nomor_Unit not in Daftar_Unit:
                os.system("cls")
                print("Nomor Unit Tidak Ada Di Dalam Daftar")
                time.sleep(1)
                continue
            elif Daftar_Unit[Nomor_Unit]['Status Unit'] != "Terisi":
                os.system("cls")
                print("Unit Tersebut Tidak Memiliki Penyewa")
                time.sleep(1)
                continue
            else:
                dataUnit = Daftar_Unit[Nomor_Unit]
                dataUnit["Status Bayar Sewa"] = Daftar_Unit(Nomor_Unit, "Belum")
                os.system("cls")
                print("Nomor Unit        :", Nomor_Unit)
                print("Tipe Unit         :", dataUnit['Tipe Unit'])
                print("Harga Unit        :", dataUnit['Harga Unit'])
                print("Nama Penghuni     :", dataUnit['Nama Penghuni'])
                print("Nomor Kontak      :", dataUnit['Nomor Kontak'])
                print("Status Pembayaran :", dataUnit["Status Bayar Sewa"])
                print('=' * 40)

                if dataUnit["Status Bayar Sewa"] == "Sudah Bayar":
                    print("Pembayaran sewa telah lunas")
                    print('=' * 40)
                    input('Tekan Enter Untuk Kembali')
                    break
                else:
                    opsi = [
                        inquirer.List("Opsi Pilih Pesan Pengingat", message="Pilih Opsi", choices=["Kirim Pesan Pengingat", "Kembali"])
                    ]
                    jawaban = inquirer.prompt(opsi)
                    Hasil_Opsi = jawaban["Opsi Pilih Pesan Pengingat"]
                    if Hasil_Opsi == "Kirim Pesan Pengingat":
                        input("Masukkan Pesan Pengingat: ")
                        opsi = [
                            inquirer.List("Opsi Pilih Konfirmasi", message="Kirim pesan pengingat ke penyewa?", choices=["Ya", "Tidak"])
                        ]
                        jawaban = inquirer.prompt(opsi)
                        Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
                        if Hasil_Opsi == "Ya":
                            # di sini program mengirim pesan ke penyewa
                            print("Pesan berhasil terkirim")
                            print('=' * 40)
                            input('Tekan Enter Untuk Kembali')
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
        except KeyboardInterrupt:
            print("\n" + "=" * 80 + "\nProgram dihentikan!")
            break

