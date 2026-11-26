import os
import inquirer
import time
from prettytable import PrettyTable
import json

with open("Program/Data.json", "r") as file:
    Data = json.load(file)

def Simpan_Data():
    with open("Program/Data.json", "w") as file:
        json.dump(Data, file, indent=4)

def Pengaturan_Unit():
    while True:
        os.system("cls")
        print("=" * 110)
        print("PENGATURAN UNIT".center(110))
        print("=" * 110)
        opsi = [
            inquirer.List("Opsi Pilih Pengaturan Unit", message="Pilih Opsi", choices=["Daftar Unit", "Tambah Unit", "Ubah Unit", "Hapus Unit", "Kembali"])
        ]
        jawaban = inquirer.prompt(opsi)
        Pilihan_Menu = jawaban["Opsi Pilih Pengaturan Unit"]
        if Pilihan_Menu == "Daftar Unit":
            Lihat_Unit()
        elif Pilihan_Menu == "Tambah Unit":
            Tambah_Unit()
        elif Pilihan_Menu == "Ubah Unit":
            Ubah_Unit()
        elif Pilihan_Menu == "Hapus Unit":
            Hapus_Unit()
        elif Pilihan_Menu == "Kembali":
            break

def Lihat_Unit():
    os.system("cls")
    print("=" * 110)
    print("DAFTAR SELURUH UNIT".center(110))
    print("=" * 110)
    if not Data["Daftar Unit"]:
        print("Belum Ada Data Unit Di Dalam Daftar")
        input("Tekan Enter Untuk Kembali")
    else:
        Tabel_Unit = PrettyTable()
        Tabel_Unit.field_names = ["Nomor Unit", "Tipe Unit", "Harga Unit", "Status Unit", "Nama Penghuni", "Status Bayar Sewa", "Nomor Kontak"]

        for Nomor_Unit, Data_Unit in sorted(Data["Daftar Unit"].items()):
            Tabel_Unit.add_row([Nomor_Unit,
                                Data_Unit['Tipe Unit'],
                                Data_Unit['Harga Unit'],
                                Data_Unit['Status Unit'],
                                Data_Unit['Nama Penghuni'],
                                Data_Unit['Status Bayar Sewa'],
                                Data_Unit['Nomor Kontak']
                                ])
        print(Tabel_Unit)  
    print("=" * 110)
    input("Tekan Enter Untuk Kembali")

def Tambah_Unit():
    while True:
        os.system("cls")
        print("=" * 110)
        print("MENAMBAHKAN UNIT".center(110))
        print("=" * 110)
        print("Contoh Format Nomor Unit : 315")
        print("3 untuk Lantai dan 15 untuk Nomor Kamar")
        print("Lantai : Min. 1 dan Max. 5")
        print("Nomor Kamar : Min. 1 dan Max. 15")
        print("-" * 110)
        print("Masukkan 0 Jika Ingin Kembali")
        print("Masukkan 1 Jika Ingin Melihat Unit Yang Telah Terdaftar")
        print("-" * 110)
        try:
            Nomor_Unit = int(input("Masukkan Nomor Unit: "))
        except ValueError:
            os.system("cls")
            print("=====Harap Masukkan Nomor Yang Valid=====")
            time.sleep(1)
            continue
        if Nomor_Unit < 0:
            os.system("cls")
            print("=====Harap Masukkan Nomor Yang Valid=====")
            time.sleep(1)
            continue
        elif Nomor_Unit == 0:
            break
        elif Nomor_Unit == 1:
            os.system("cls")
            if not Data["Daftar Unit"]:
                print("Belum ada nomor unit yang dibuat")
                print("--------------------------------")
                input("Tekan Enter Untuk Kembali")
            else:
                print("Nomor Unit Yang Sudah Ada :")
                for Lantai in range(1, 6):
                    print(f"Lantai {Lantai} : ", end=" ")
                    for Nomor in sorted(Data["Daftar Unit"]):
                        if int(Nomor) // 100 == Lantai:
                            print(Nomor, end=" ")
                        else:
                            print("-", end=" ")
                    print()
                input("Tekan Enter Untuk Kembali")
        else:
            Lantai = Nomor_Unit // 100
            Nomor_Kamar = Nomor_Unit % 100
            if Lantai < 1 or Lantai > 5 or Nomor_Kamar < 1 or Nomor_Kamar > 15:
                os.system("cls")
                print("=====Lantai atau Nomor Kamar Tidak Sesuai Ketentuan!=====")
                time.sleep(2)
                continue
            elif Nomor_Unit in Data["Daftar Unit"]:
                os.system("cls")
                print("=====Nomor Tersebut Telah Ada Di Dalam Daftar=====")
                time.sleep(2)
                continue
            else:
                os.system("cls")
                print("=" * 110)
                print("MENAMBAHKAN UNIT".center(110))
                print("=" * 110)
                opsi = [
                    inquirer.List("Opsi Pilih Tipe Unit", message="Silahkan Pilih Tipe Unit Yang Ingin Ditambahkan", choices=["Studio", "1BR", "2BR"])
                ]
                jawaban = inquirer.prompt(opsi)
                Hasil_Opsi = jawaban["Opsi Pilih Tipe Unit"]
                if Hasil_Opsi == "Studio":
                    Tipe_Unit = "Studio"
                    Harga_Unit = 2000000
                elif Hasil_Opsi == "1BR":
                    Tipe_Unit = "1BR"
                    Harga_Unit = 3000000
                elif Hasil_Opsi == "2BR":
                    Tipe_Unit = "2BR"
                    Harga_Unit = 4500000
                os.system("cls")
                print("=" * 110)
                print("MENAMBAHKAN UNIT".center(110))
                print("=" * 110)
                print(f"Nomor Unit : {Nomor_Unit}")
                print(f"Tipe Unit : {Tipe_Unit}")
                print(f"Harga Unit : {Harga_Unit}")
                print("Status Unit : Kosong")
                print("Nama Penghuni : -")
                print("Status Bayar Sewa : -")
                print("Nomor Kontak : -")
                opsi = [
                    inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menambahkan unit ini?", choices=["Ya", "Tidak"])
                ]
                jawaban = inquirer.prompt(opsi)
                Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
                if Hasil_Opsi == "Ya":
                    os.system("cls")
                    Unit_Baru = {
                        'Tipe Unit': Tipe_Unit,
                        'Harga Unit': Harga_Unit,
                        'Status Unit': "Kosong",
                        'Nama Penghuni': "-",
                        'Status Bayar Sewa' : "-",
                        'Nomor Kontak': "-"
                    }
                    Nomor_Unit = str(Nomor_Unit)
                    Data["Daftar Unit"][Nomor_Unit] = Unit_Baru
                    Simpan_Data()
                    print("Berhasil!, Unit No", Nomor_Unit, "Telah Ditambahkan")
                    print("---------------------------------------------------")
                    input('Tekan Enter Untuk Kembali')
                    break
                elif Hasil_Opsi == "Tidak":
                    break

def Ubah_Unit():
    while True:
        os.system("cls")
        print("=" * 110)
        print("MENGUBAH UNIT".center(110))
        print("=" * 110)
        if not Data["Daftar Unit"]:
            print("Belum ada data unit di dalam daftar")
            print('-----------------------------------')
            input('Tekan Enter Untuk Kembali')
            break
        else:
            print("Masukkan 0 Jika Ingin Kembali")
            print("Masukkan 1 Jika Ingin Melihat Unit Yang Telah Terdaftar")
            print("-" * 110)
            try:
                Nomor_Tujuan = int(input("Masukkan Nomor Unit Yang Ingin Diubah: "))
            except ValueError:
                print("=====Harap Masukkan Nomor Unit Yang Valid!=====")
                time.sleep(1)
                continue
            if Nomor_Tujuan == 0:
                break
            elif Nomor_Tujuan == 1:
                os.system("cls")
                print("Nomor Unit Yang Sudah Ada :")
                for Lantai in range(1, 6):
                    print(f"Lantai {Lantai} :", end=" ")
                    for Nomor in sorted(Data["Daftar Unit"]):
                        if int(Nomor) // 100 == Lantai:
                            print(f"Nomor, ({Data["Daftar Unit"][Nomor]["Status Unit"]})", end=" ")
                        else:
                            print("-")
                print("-------------------------")
                input("Tekan Enter Untuk Kembali")
                continue
            elif Nomor_Tujuan not in Data["Daftar Unit"]:
                print("=====Nomor Tersebut Tidak Ditemukan Di Dalam Daftar=====")
                time.sleep(1)
                continue

            Unit = Data["Daftar Unit"][Nomor_Tujuan]

            if Unit['Status Unit'] == "Terisi":
                os.system("cls")
                print("=====Unit Terisi Tidak Bisa Diubah!=====")
                time.sleep(1)
            else:
                while True:
                    os.system("cls")
                    print("=" * 110)
                    print("MENGUBAH UNIT".center(110))
                    print("=" * 110)
                    print("Nomor Unit Yang Ingin Diubah :", Nomor_Tujuan)
                    print("Tipe Unit Saat Ini :", Unit['Tipe Unit'])
                    print("Harga Unit Saat Ini :", Unit['Harga Unit'])
                    opsi = [
                        inquirer.List("Opsi Pilih Tipe Unit", message="Silahkan Pilih Tipe Unit Yang Baru", choices=["Studio", "1BR", "2BR"])
                    ]
                    jawaban = inquirer.prompt(opsi)
                    Hasil_Opsi = jawaban["Opsi Pilih Tipe Unit"]
                    if Hasil_Opsi == Unit['Tipe Unit']:
                        print("=====Pilihan Tipe Harus Berbeda!=====")
                        time.sleep(1)
                        continue
                    else:
                        if jawaban["Tipe Unit"] == "Studio":
                            Tipe_Unit = "Studio"
                            Harga_Unit = 2000000
                        elif jawaban["Tipe Unit"] == "1BR":
                            Tipe_Unit = "1BR"
                            Harga_Unit = 3000000
                        elif jawaban["Tipe Unit"] == "2BR":
                            Tipe_Unit = "2BR"
                            Harga_Unit = 4500000
                    opsi = [
                        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda Ingin Mengubah Tipe Unit Ini?", choices=["Ya", "Tidak"])
                    ]
                    jawaban = inquirer.prompt(opsi)
                    Hasil_Opsi == jawaban["Opsi Pilih Konfirmasi"]
                    if Hasil_Opsi == "Ya":
                        Unit['Tipe Unit'] = Tipe_Unit
                        Unit['Harga Unit'] = Harga_Unit
                        Simpan_Data()
                        print(f"Nomor Unit : {Nomor_Tujuan}")
                        print(f"Tipe Unit : {Tipe_Unit}")
                        print(f"Harga Unit : {Harga_Unit}")
                        print("Tipe Unit Berhasil Diubah!")
                        print("--------------------------")
                        input('Tekan Enter Untuk Kembali')
                        break
                    else:
                       break
                break
        
def Hapus_Unit():
    while True:
        os.system("cls")
        print("=" * 110)
        print("MENGHAPUS UNIT" * 110)
        print("=" * 110)
        if not Data["Daftar Unit"]:
            print("Belum Ada Data Unit Di Dalam Daftar")
            print("-----------------------------------")
            input('Tekan Enter Untuk Kembali')
            break
        print("Masukkan 0 Jika Ingin Kembali")
        print("Masukkan 1 Jika Ingin Melihat Unit Yang Telah Terdaftar")
        print("-" * 110)
        try:
            Nomor_Hapus = int(input("Masukkan Nomor Unit Yang Ingin Dihapus: "))
        except ValueError:
            print("=====Harap Masukkan Nomor Unit Yang Valid!=====")
            time.sleep(2)
            continue
        if Nomor_Hapus == 0:
            break
        elif Nomor_Hapus == 1:
            os.system("cls")
            print("Nomor Unit Yang Sudah Ada :")
            for Lantai in range(1, 6):
                print("Lantai", Lantai, ":", end=" ")
                for Nomor in sorted(Data["Daftar Unit"]):
                    if int(Nomor) // 100 == Lantai:
                        print(f"Nomor, ({Data["Daftar Unit"][Nomor]["Status Unit"]})", end=" ")
                    else:
                        print("-")
            print("-------------------------")
            input("Tekan Enter Untuk Kembali")
            continue
        elif Nomor_Hapus not in Data["Daftar Unit"]:
            print("=====Nomor Tersebut Tidak Ditemukan Di Dalam Daftar=====")
            time.sleep(2)
            continue

        Unit = Data["Daftar Unit"][Nomor_Hapus]

        if Unit['Status Unit'] == "Terisi":
            os.system("cls")
            print("Unit Terisi Tidak Bisa Dihapus!")
            time.sleep(1)
        else:
            os.system("cls")
            print("=" * 110)
            print("MENGHAPUS UNIT" * 110)
            print("=" * 110)
            print(f"Tipe Unit : {Unit['Tipe Unit']}")
            print(f"Harga Unit : {Unit['Harga Unit']}")
            opsi = [
                inquirer.List("Pilihan1", message="Apakah Anda Ingin Menghapus Unit Ini?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            if jawaban["Pilihan1"] == "Ya":
                del Data["Daftar Unit"][Nomor_Hapus]
                Simpan_Data()
                print(f"Berhasil!, Unit No {Nomor_Hapus} Telah Dihapus Dari Daftar")
                print("-----------------------------------------------------------")
                input("Tekan Enter Untuk Kembali")
                break
            else:
                break