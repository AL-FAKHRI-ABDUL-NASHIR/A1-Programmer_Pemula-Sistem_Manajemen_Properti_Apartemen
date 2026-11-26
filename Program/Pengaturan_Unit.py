import os
import inquirer
import time
import Data
from prettytable import PrettyTable

def Pengaturan_Unit():
    Go_Back_Pengaturan_Unit = False
    while not Go_Back_Pengaturan_Unit:
        try:
            os.system("cls")
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
                Go_Back_Pengaturan_Unit = True
        except KeyboardInterrupt:
            break    

def Lihat_Unit():
    try:
        os.system("cls")
        print("=========================================================================================")
        print("                                   DAFTAR SELURUH UNIT                                   ")
        print("=========================================================================================")
        if len(Data.Daftar_Unit) == 0:
            print("Belum Ada Data Unit Di Dalam Daftar")
            print()
        else:
            tabelUnit = PrettyTable()
            tabelUnit.field_names = ["Nomor Unit", "Tipe Unit", "Harga Unit", "Status Unit", "Nama Penghuni", "Nomor Kontak"]
                    
            for Nomor_Unit, dataUnit in sorted(Data.Daftar_Unit.items()):
                tabelUnit.add_row([Nomor_Unit,
                                    dataUnit['Tipe Unit'],
                                    dataUnit['Harga Unit'],
                                    dataUnit['Status Unit'],
                                    dataUnit['Nama Penghuni'],
                                    dataUnit['Nomor Kontak']
                                    ])
            print(tabelUnit)
        print()  
        print("=========================")
        input("Tekan Enter Untuk Kembali ")
    except KeyboardInterrupt:
        pass

def Tambah_Unit():
    os.system("cls")
    print("=========================================================================================")
    print("                                   MENAMBAHKAN UNIT                                      ")
    print("=========================================================================================")
    opsi = [
        inquirer.List("Opsi Pilih Konfirmasi", message="Apakah Anda ingin menambahkan unit?", choices=["Ya", "Tidak"])
    ]
    jawaban = inquirer.prompt(opsi)

    if jawaban is None:
        return
    
    Hasil_Opsi = jawaban["Opsi Pilih Konfirmasi"]
    if Hasil_Opsi == "Ya":
        while True:
            try: #Ctrl+C error handling
                os.system("cls")
                print(Data.Daftar_Unit)
                print("=========================================================================================")
                print("                                   MENAMBAHKAN UNIT                                      ")
                print("=========================================================================================")
                print("Contoh Format Nomor Unit : 315")
                print("3 untuk Lantai dan 15 untuk Nomor Kamar")
                print("Lantai : Min. 1 dan Max. 5")
                print("Nomor Kamar : Min. 1 dan Max. 15")
                print("---------------------------------------")
                print()
                print("Masukkan 0 Jika Ingin Kembali")
                print("Masukkan 1 Jika Ingin Melihat Unit Yang Telah Terdaftar")
                try:
                    Nomor_Unit = int(input("Masukkan Nomor Unit: "))
                except ValueError:
                    os.system("cls")
                    print("Harap Masukkan Nomor Yang Valid")
                    time.sleep(1)
                    continue
                except KeyboardInterrupt:
                    print("\n" + "=" * 80 + "\nAksi Dibatalkan!")
                    break
                if Nomor_Unit < 0:
                    os.system("cls")
                    print("Harap Masukkan Nomor Yang Valid")
                    time.sleep(1)
                    continue
                elif Nomor_Unit == 0:
                    break
                elif Nomor_Unit == 1:
                    os.system("cls")
                    print("Nomor Unit Yang Sudah Ada :")
                    if len(Data.Daftar_Unit) == 0:
                        print("Belum ada")
                        input("Tekan Enter Untuk Kembali")
                    else:
                        for Lantai in range(1, 6):
                            print("Lantai", Lantai, ":", end=" ")
                            for Nomor in sorted(Data.Daftar_Unit):
                                if Nomor // 100 == Lantai:
                                    print(Nomor, end=" ")
                            print()
                        input("Tekan Enter Untuk Kembali")
                else:
                    Lantai = Nomor_Unit // 100
                    Nomor_Kamar = Nomor_Unit % 100
                    if Lantai < 1 or Lantai > 5 or Nomor_Kamar < 1 or Nomor_Kamar > 15:
                        os.system("cls")
                        print("Lantai atau Nomor Kamar Tidak Sesuai Ketentuan!")
                        time.sleep(1)
                        continue
                    elif Nomor_Unit in Data.Daftar_Unit:
                        os.system("cls")
                        print("Nomor Tersebut Telah Ada Di Dalam Daftar")
                        time.sleep(1)
                        continue
                    else:
                        opsi = [
                            inquirer.List("Pilihan Tipe Unit", message="Silahkan Pilih Tipe Unit Yang Ingin Ditambahkan", choices=["Studio", "1BR", "2BR", "Batal"])
                        ]
                        jawaban = inquirer.prompt(opsi)

                        if jawaban is None:
                            print("Aksi Dibatalkan!")
                            input("Ketik 'Enter' untuk kembali ")
                            break

                        Hasil_Opsi = jawaban["Pilihan Tipe Unit"]
                        if Hasil_Opsi == "Studio":
                            Tipe_Unit = "Studio"
                            Harga_Unit = 2000000
                        elif Hasil_Opsi == "1BR":
                            Tipe_Unit = "1BR"
                            Harga_Unit = 3000000
                        elif Hasil_Opsi == "2BR":
                            Tipe_Unit = "2BR"
                            Harga_Unit = 4500000
                        else:
                            break

                        Unit_Baru = {
                            'Tipe Unit': Tipe_Unit,
                            'Harga Unit': Harga_Unit,
                            'Status Unit': "Kosong",
                            'Nama Penghuni': "-",
                            'Nomor Kontak': "-"
                        } 
                        Data.Daftar_Unit[Nomor_Unit] = Unit_Baru
                        print("Berhasil!, Unit No", Nomor_Unit, "Telah Ditambahkan")
                        print('=' * 40)
                        input('Tekan Enter Untuk Kembali')
                        break 
            except KeyboardInterrupt:
                print("Aksi Dibatalkan!")
                break


def Ubah_Unit():
    Balik_Menu_Utama = False
    while True:
        try:
            os.system("cls")
            print("=========================================================================================")
            print("                                      MENGUBAH UNIT                                      ")
            print("=========================================================================================")
            if len(Data.Daftar_Unit) == 0:
                print("Belum Ada Data Unit Di Dalam Daftar")
                print()
                print('=' * 40)
                input('Tekan Enter Untuk Kembali')
                break
            print("Masukkan 0 Jika Ingin Kembali")
            print("Masukkan 1 Jika Ingin Melihat Unit Yang Telah Terdaftar")
            try:
                Nomor_Tujuan = int(input("Masukkan Nomor Unit Yang Ingin Diubah: "))
            except ValueError:
                print("Harap Masukkan Nomor Unit Yang Valid!")
                time.sleep(1)
                continue
            except KeyboardInterrupt:
                print("\n" + "=" * 80 + "\nAksi Dibatalkan!")
                break
            except EOFError:
                print("Aksi dibatalkan!")
                break

            if Nomor_Tujuan == 0:
                break
            elif Nomor_Tujuan == 1:
                os.system("cls")
                print("Nomor Unit Yang Sudah Ada :")
                for Lantai in range(1, 6):
                    print("Lantai", Lantai, ":", end=" ")
                    for Nomor in sorted(Data.Daftar_Unit):
                        if Nomor // 100 == Lantai:
                            print(Nomor, end=" ")
                    print()
                input("Tekan Enter Untuk Kembali")
                continue
            elif Nomor_Tujuan not in Data.Daftar_Unit:
                print("Nomor Tersebut Tidak Ditemukan Di Dalam Daftar")
                time.sleep(1)
                continue

            Unit = Data.Daftar_Unit[Nomor_Tujuan]

            if Unit['Status Unit'] == "Terisi":
                os.system("cls")
                print("Unit Terisi Tidak Bisa Diubah!")
                time.sleep(1)
            else:
                while True:
                    os.system("cls")
                    print("Nomor Unit Yang Ingin Diubah:", Nomor_Tujuan)
                    print("Tipe Unit Saat Ini:", Unit['Tipe Unit'])
                    print("Harga Unit Saat Ini:", Unit['Harga Unit'])
                    opsi = [
                        inquirer.List("Pilihan1", message="Apakah Anda Ingin Mengubah Tipe Unit Ini?", choices=["Ya", "Tidak"])
                    ]
                    jawaban = inquirer.prompt(opsi)
                    if jawaban is None:
                        break
                    if jawaban["Pilihan1"] == "Ya":
                        while True:
                            os.system("cls")
                            print("Nomor Unit Yang Ingin Diubah:", Nomor_Tujuan)
                            print("Tipe Unit Saat Ini:", Unit['Tipe Unit'])
                            print("Harga Unit Saat Ini:", Unit['Harga Unit'])
                            opsi = [
                                inquirer.List("Tipe Unit", message="Silahkan Pilih Tipe Unit Yang Baru", choices=["Studio", "1BR", "2BR", "Batal"])
                            ]
                            jawaban = inquirer.prompt(opsi)
                            if jawaban is None:
                                break
                            if jawaban["Tipe Unit"] == Unit['Tipe Unit']:
                                print("Pilih Tipe Yang Berbeda!")
                                time.sleep(1)
                                continue
                            else:
                                if jawaban["Tipe Unit"] == "Studio":
                                    Unit['Tipe Unit'] = "Studio"
                                    Unit['Harga Unit'] = 2000000
                                elif jawaban["Tipe Unit"] == "1BR":
                                    Unit['Tipe Unit'] = "1BR"
                                    Unit['Harga Unit'] = 3000000
                                elif jawaban["Tipe Unit"] == "2BR":
                                    Unit['Tipe Unit'] = "2BR"
                                    Unit['Harga Unit'] = 4500000
                                else:
                                    break
                                print("Berhasil!, Tipe Unit No", Nomor_Tujuan, "Telah Berhasil Diubah")
                                time.sleep(2)
                                Balik_Menu_Utama = True
                                break
                        break
                    else:
                        break
            if Balik_Menu_Utama:
                break
        except KeyboardInterrupt:
            break
                       
        
def Hapus_Unit():
    Balik_Menu_Utama = False
    while True:
        try:
            os.system("cls")
            print("=========================================================================================")
            print("                                      MENGHAPUS UNIT                                     ")
            print("=========================================================================================")
            if len(Data.Daftar_Unit) == 0:
                print("Belum Ada Data Unit Di Dalam Daftar")
                print()
                print('=' * 40)
                input('Tekan Enter Untuk Kembali')
                break
            print("Masukkan 0 Jika Ingin Kembali")
            print("Masukkan 1 Jika Ingin Melihat Unit Yang Telah Terdaftar")
            try:
                Nomor_Hapus = int(input("Masukkan Nomor Unit Yang Ingin Dihapus: "))
            except ValueError:
                print("Harap Masukkan Nomor Unit Yang Valid!")
                time.sleep(1)
                continue
            except KeyboardInterrupt:
                break
            except EOFError:
                break
            if Nomor_Hapus == 0:
                break
            elif Nomor_Hapus == 1:
                os.system("cls")
                print("Nomor Unit Yang Sudah Ada :")
                for Lantai in range(1, 6):
                    print("Lantai", Lantai, ":", end=" ")
                    for Nomor in sorted(Data.Daftar_Unit):
                        if Nomor // 100 == Lantai:
                            print(Nomor, end=" ")
                    print()
                try:
                    input("Tekan Enter Untuk Kembali")
                    continue
                except EOFError:
                    break
            elif Nomor_Hapus not in Data.Daftar_Unit:
                print("Nomor Tersebut Tidak Ditemukan Di Dalam Daftar")
                time.sleep(1)
                continue

            Unit = Data.Daftar_Unit[Nomor_Hapus]

            if Unit['Status Unit'] == "Terisi":
                os.system("cls")
                print("Unit Terisi Tidak Bisa Dihapus!")
                time.sleep(1)
            else:
                while True:
                    print("Tipe Unit :", Unit['Tipe Unit'])
                    print("Harga Unit:", Unit['Harga Unit'])
                    opsi = [
                        inquirer.List("Pilihan1", message="Apakah Anda Ingin Menghapus Unit Ini?", choices=["Ya", "Tidak"])
                    ]
                    jawaban = inquirer.prompt(opsi)
                    if jawaban is None:
                        break
                    if jawaban["Pilihan1"] == "Ya":
                        del Data.Daftar_Unit[Nomor_Hapus]
                        print("Berhasil!, Unit No", Nomor_Hapus, "Telah Dihapus Dari Daftar")
                        time.sleep(2)
                        Balik_Menu_Utama = True
                        break
                    else:
                        break
            if Balik_Menu_Utama:
                break
        except KeyboardInterrupt:
            break

