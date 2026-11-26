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
        if jawaban is None:
            return
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
        tabelUnit = PrettyTable()
        tabelUnit.field_names = ["Nomor Unit", "Tipe Unit", "Harga Unit", "Status Unit", "Nama Penghuni", "Status Bayar Sewa", "Nomor Kontak"]

        for Nomor_Unit, dataUnit in sorted(Data["Daftar Unit"].items()):
            tabelUnit.add_row([Nomor_Unit,
                                dataUnit['Tipe Unit'],
                                dataUnit['Harga Unit'],
                                dataUnit['Status Unit'],
                                dataUnit['Nama Penghuni'],
                                dataUnit['Status Bayar Sewa'],
                                dataUnit['Nomor Kontak']
                                ])
        tabelUnit.hrules = 1
        print(tabelUnit)  
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
                    print()
                input("Tekan Enter Untuk Kembali")
        else:
            Lantai = Nomor_Unit // 100
            Nomor_Kamar = Nomor_Unit % 100
            if Lantai < 1 or Lantai > 5 or Nomor_Kamar < 1 or Nomor_Kamar > 15:
                os.system("cls")
                print("=====Lantai atau Nomor Kamar Tidak Sesuai Ketentuan!=====")
                time.sleep(1)
                continue
            elif str(Nomor_Unit) in Data["Daftar Unit"]:
                os.system("cls")
                print("=====Nomor Tersebut Telah Ada Di Dalam Daftar=====")
                time.sleep(1)
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
                if jawaban is None:
                    return
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
                print(f"Tipe Unit  : {Tipe_Unit}")
                print(f"Harga Unit : {Harga_Unit}")
                opsi = [
                    inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menambahkan unit ini?", choices=["Ya", "Tidak"])
                ]
                jawaban = inquirer.prompt(opsi)
                if jawaban is None:
                    return
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
                os.system("cls")
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
                            print(f"{Nomor}<{Data["Daftar Unit"][Nomor]["Status Unit"]}>".replace("Kosong" , "K").replace("Terisi" , "T"), end=" ")
                    print(" ")
                print("Keterangan : K = Kosong, T = Terisi")
                print("-----------------------------------")
                input("Tekan Enter Untuk Kembali")
                continue
            elif str(Nomor_Tujuan) not in Data["Daftar Unit"]:
                os.system("cls")
                print("=====Nomor Tersebut Tidak Ditemukan Di Dalam Daftar=====")
                time.sleep(1)
                continue

            Unit = Data["Daftar Unit"][str(Nomor_Tujuan)]

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
                    print("Nomor Unit :", Nomor_Tujuan)
                    print("Tipe Unit  :", Unit['Tipe Unit'])
                    print("Harga Unit :", Unit['Harga Unit'])
                    opsi = [
                        inquirer.List("Opsi Pilih Tipe Unit", message="Silahkan Pilih Tipe Unit Yang Baru", choices=["Studio", "1BR", "2BR"])
                    ]
                    jawaban = inquirer.prompt(opsi)
                    if jawaban is None:
                        return
                    Hasil_Opsi = jawaban["Opsi Pilih Tipe Unit"]
                    if Hasil_Opsi == Unit['Tipe Unit']:
                        print("=====Pilihan Tipe Harus Berbeda!=====")
                        time.sleep(1)
                        continue
                    elif Hasil_Opsi == "Studio":
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
                    print("MENGUBAH UNIT".center(110))
                    print("=" * 110)
                    print("Nomor Unit :", Nomor_Tujuan)
                    print("Tipe Unit  :", Unit['Tipe Unit'])
                    print("Harga Unit :", Unit['Harga Unit'])
                    opsi = [
                        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda Ingin Mengubah Tipe Unit Ini?", choices=["Ya", "Tidak"])
                    ]
                    jawaban = inquirer.prompt(opsi)
                    if jawaban is None:
                        return
                    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
                    if Hasil_Opsi == "Ya":
                        os.system("cls")
                        Unit['Tipe Unit'] = Tipe_Unit
                        Unit['Harga Unit'] = Harga_Unit
                        Simpan_Data()
                        print(f"Nomor Unit : {Nomor_Tujuan}")
                        print(f"Tipe Unit  : {Tipe_Unit}")
                        print(f"Harga Unit : {Harga_Unit}")
                        print(" ")
                        print("Tipe Unit Berhasil Diubah!")
                        print("--------------------------")
                        input('Tekan Enter Untuk Kembali')
                        break
                    elif Hasil_Opsi == "Tidak":
                        break
                break
        
def Hapus_Unit():
    while True:
        os.system("cls")
        print("=" * 110)
        print("MENGHAPUS UNIT".center(110))
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
            os.system("cls")
            print("=====Harap Masukkan Nomor Unit Yang Valid!=====")
            time.sleep(1)
            continue
        if Nomor_Hapus == 0:
            break
        elif Nomor_Hapus == 1:
            os.system("cls")
            print("Nomor Unit Yang Sudah Ada :")
            for Lantai in range(1, 6):
                print(f"Lantai {Lantai} :", end=" ")
                for Nomor in sorted(Data["Daftar Unit"]):
                    if int(Nomor) // 100 == Lantai:
                        print(f"{Nomor}<{Data["Daftar Unit"][Nomor]["Status Unit"]}>".replace("Kosong" , "K").replace("Terisi" , "T"), end=" ")
                print(" ")
            print("Keterangan : K = Kosong, T = Terisi")
            print("-----------------------------------")
            input("Tekan Enter Untuk Kembali")
            continue
        elif str(Nomor_Hapus) not in Data["Daftar Unit"]:
            os.system("cls")
            print("=====Nomor Tersebut Tidak Ditemukan Di Dalam Daftar=====")
            time.sleep(1)
            continue

        Unit = Data["Daftar Unit"][str(Nomor_Hapus)]

        if Unit['Status Unit'] == "Terisi":
            os.system("cls")
            print("Unit Terisi Tidak Bisa Dihapus!")
            time.sleep(1)
        else:
            os.system("cls")
            print("=" * 110)
            print("MENGHAPUS UNIT".center(110))
            print("=" * 110)
            print(f"Nomor Unit : {Nomor_Hapus}")
            print(f"Tipe Unit  : {Unit['Tipe Unit']}")
            print(f"Harga Unit : {Unit['Harga Unit']}")
            opsi = [
                inquirer.List("Pilihan1", message="Apakah Anda Ingin Menghapus Unit Ini?", choices=["Ya", "Tidak"])
            ]
            jawaban = inquirer.prompt(opsi)
            if jawaban is None:
                return
            Hasil_Opsi = jawaban["Pilihan1"]
            if Hasil_Opsi == "Ya":
                os.system("cls")
                del Data["Daftar Unit"][str(Nomor_Hapus)]
                Simpan_Data()
                print(f"Berhasil!, Unit No {Nomor_Hapus} Telah Dihapus Dari Daftar")
                print("-----------------------------------------------------------")
                input("Tekan Enter Untuk Kembali")
                break
            else:
                break
