import numpy as np

arr = np.array([[1,2,3,4,5],
               [6,7,8,9,10],
               [11,12,13,14,15],
               [16,17,18,19,20],
               [21,22,23,24,25]])

ukuran_array = np.size(arr)

print(ukuran_array)

def hitung_genap_ganjil():
    jumlah_genap = 0
    jumlah_ganjil = 0
    for i in range (5):
        for j in range(5):
            if arr[i][j] % 2 == 1:
                jumlah_ganjil += 1
            elif arr[i][j] % 2 == 0:
                jumlah_genap  += 1
    print("Jumlah Bil. Genap  : ", jumlah_genap)
    print("Jumlah Bil. Ganjil : ", jumlah_ganjil)

def hitung_bil_besar():
    bil_besar = np.sum(arr > 50)
    print(bil_besar)
    sum_bil = np.sum(arr[arr>50])
    print("jumlah sumbil: ", sum_bil)

def hitung_kolom():
    for i in range(0,5,2):
        print(sum(arr[:,i]))

hitung_genap_ganjil()
hitung_bil_besar()
hitung_kolom()