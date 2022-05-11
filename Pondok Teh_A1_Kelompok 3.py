from prettytable import PrettyTable
import pwinput
import csv
import os
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""                                   
   ___                                
  / _ \   _   _    ___   _   _    ___ 
 | | | | | | | |  / _ \ | | | |  / _ \
 | |_| | | |_| | |  __/ | |_| | |  __/
  \__\_\  \__,_|  \___|  \__,_|  \___|
                                                                   
"""
class Queue: 
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        if self.head == None:
            self.head = data
        else:
            dataTerakhir = self.head
            while dataTerakhir.next is not None:
                dataTerakhir = dataTerakhir.next
            dataTerakhir.next = data

    def dequeue(self):
        if self.head == None:
            pass
        else:
            self.head = self.head.next

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
            
    def isExist(self,data):
        temp = self.head
        while temp != None:
            if (data == temp.data):
                return True
            temp = temp.next
        return False

    def displayData(self,dataExcept = None):
        if self.head is None:
            print("====================")
            print("Antrian Kosong")
            print("====================")
        else:
            tabelDisplay.clear()
            # Header tabel
            tabelDisplay.field_names = list(self.head.data.keys())
            # Menghapus jenis yang tidak ingin ditampilkan pada tabel
            if dataExcept != None:
                for i in dataExcept:
                    if i in list(self.head.data.keys()):
                        tabelDisplay.field_names.remove(i)
            temp = self.head
            while (temp != None):
                if dataExcept != None:
                    # menambahkan data kecuali jenis yang tidak ingin ditampilkan pada tabel
                    data = []
                    for key in temp.data.keys():
                        if key not in dataExcept:
                            data.append(temp.data[key])
                    tabelDisplay.add_row(data)
                    data.clear()
                else : # jika tidak jenis yang di ban, maka
                    tabelDisplay.add_row(list(temp.data.values()))
                temp = temp.next
            print(tabelDisplay)                                           
"""
  _       _           _                 _     _       _         _   
 | |     (_)  _ __   | | __   ___    __| |   | |     (_)  ___  | |_ 
 | |     | | | '_ \  | |/ /  / _ \  / _` |   | |     | | / __| | __|
 | |___  | | | | | | |   <  |  __/ | (_| |   | |___  | | \__ \ | |_ 
 |_____| |_| |_| |_| |_|\_\  \___|  \__,_|   |_____| |_| |___/  \__|
                                                                    
"""                                                            
                                                                            
class LinkedList:
    def __init__(self,nama):
        self.head = None
        self.nama = nama

    def inputData(self,data,jenisPrimary = None, jenisSpesial = None, dataJenisSpesial = None):
        for index in data.keys():
            while True:
                if type(data[index]) == str: # jika string
                    databaru = input(f"Masukan {index} : ").title()
                    # Check pengkondisian
                    if not jenisPrimary == None and index == jenisPrimary:
                        if self.isExist(databaru,index):
                            print("Data sudah ada")
                            continue
                    if jenisSpesial == index:
                        if databaru not in dataJenisSpesial:
                            print(f"Hanya menerima {jenisSpesial} = {dataJenisSpesial}")
                            continue
                    
                    if databaru.isnumeric() == True or databaru.find("-") != -1 :
                        print("Tidak boleh menggunakan angka")
                        continue
                elif type(data[index]) == int: # jika int
                    while True:
                        try:
                            databaru = int(input(f"Masukan {index} : "))
                            if databaru < 0:
                                print("Tidak boleh kurang dari nol")
                                continue
                            else :
                                break
                        except ValueError:
                            print("Hanya menerima inputan berupa angka")
                # Update datanya
                data[index] = databaru
                break
        return data

    def addData(self, template,jenisPrimary = None, jenisSpesial = None, dataJenisSpesial = None ):
        self.inputData(template,jenisPrimary,jenisSpesial,dataJenisSpesial)
        self.addLast(Node(template))
        
    def addLast(self, dataBaru):
        if self.head == None:
            self.head = dataBaru
        else:
            dataTerakhir = self.head
            while dataTerakhir.next != None:
                dataTerakhir = dataTerakhir.next
            dataTerakhir.next = dataBaru
    
    def updateData(self):
        try:
            self.displayData()
            # Jika kosong
            if self.head == None:
                return
            # Jika tidak kosong
            kunci = list(self.head.data.keys())[0] # ambil keys pertama pada dict
            target = input(f"Masukan {kunci} yang ingin diubah : ").title() # input target ignore case sensitive
            temp = self.head
            while temp != None:
                if (temp.data[kunci] == target):
                    print("Masukan data baru")
                    self.inputData(temp.data)
                    print("Data berhasil diubah")
                    return
                temp = temp.next # menuju node selanjutnya
            print("Data tidak ditemukan")
        except ValueError:
            print("Data tidak ditemukan")

    def deleteData(self):
        if self.head == None:
            print("Linked List Kosong")
        elif self.head.next is None: # kalau node sisa 1
            self.head = None
            print("Data berhasil dihapus")
        else: # jika lebih dari 1
            self.displayData()
            kunci = list(self.head.data.keys())[0] # ambil keys pertama pada dict
            target = input(f"Masukan {kunci} yang ingin dihapus : ").title() # input target ignore case sensitive
            if (self.head.data[kunci] == target):
                self.head = self.head.next
                print("Data berhasil dihapus")
                return
            temp = self.head
            while temp.next != None:
                if (temp.next.data[kunci] == target):
                    dataDelete = temp.next
                    temp.next = dataDelete.next
                    del dataDelete
                    print("Data berhasil dihapus")
                    return
                temp = temp.next # menuju node selanjutnya
            print("Data tidak ditemukan")

    def clearData(self):
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            del temp

    def displayData(self,dataExcept = None):
        if self.head is None:
            print("Linked List Kosong")
        else:
            tabelDisplay.clear()
            # Header tabel
            tabelDisplay.field_names = list(self.head.data.keys())
            # Menghapus jenis yang tidak ingin ditampilkan pada tabel
            if dataExcept != None:
                for i in dataExcept:
                    if i in list(self.head.data.keys()):
                        tabelDisplay.field_names.remove(i)
            temp = self.head
            while (temp != None):
                if dataExcept != None:
                    # menambahkan data kecuali jenis yang tidak ingin ditampilkan pada tabel
                    data = []
                    for key in temp.data.keys():
                        if key not in dataExcept:
                            data.append(temp.data[key])
                    tabelDisplay.add_row(data)
                    data.clear()
                else : # jika tidak jenis yang di ban, maka
                    tabelDisplay.add_row(list(temp.data.values()))
                temp = temp.next
            print(tabelDisplay)

    def isExist(self,target,jenis):
        temp = self.head
        while temp != None:
            if (target == temp.data[jenis]):
                return True
            temp = temp.next
        return False

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def setData(self,target,jenis,dataBaru):
        temp = self.head
        while temp != None:
            if (target == temp.data[jenis]):
                temp.data = dataBaru
                return
            temp = temp.next

    def getData(self,target,jenis):
        temp = self.head
        while temp != None:
            if (target == temp.data[jenis]):
                return temp.data
            temp = temp.next
        return False

    def addRow(self, row):
        dataBaru = {}
        for key,value in row.items():
            if value.isnumeric(): # jika value nya angka kita konversi ke int
                dataBaru[key] = int(value)
            else:
                dataBaru[key] = value
        self.addLast(Node(dataBaru))

    def readCSV(self):
        with open(self.nama+".csv",mode="r",  newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.addRow(row)

    def writeCSV(self):
        if self.head != None:
            with open(self.nama+".csv", mode="w", newline='') as csv_file:
                fieldnames = list(self.head.data.keys())
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                temp = self.head
                while(temp != None):
                    writer.writerow(temp.data)  # menulis ke csv
                    temp = temp.next  # traversal

# Inisialisasi Awal 
dataUser = LinkedList("user")
dataBarang = LinkedList("barang")
totalPesanan = LinkedList("totalPesanan")
dataRiwayatPembelian = LinkedList("riwayatPembelian")
dataAntrian = Queue()
tabelDisplay = PrettyTable()


""" __                                 _                     _                                       _ 
   / _|  _   _   _ __     __ _   ___  (_)    _   _   _ __   (_) __   __   ___   _ __   ___    __ _  | |
  | |_  | | | | | '_ \   / _` | / __| | |   | | | | | '_ \  | | \ \ / /  / _ \ | '__| / __|  / _` | | |
  |  _| | |_| | | | | | | (_| | \__ \ | |   | |_| | | | | | | |  \ V /  |  __/ | |    \__ \ | (_| | | |
  |_|    \__,_| |_| |_|  \__, | |___/ |_|    \__,_| |_| |_| |_|   \_/    \___| |_|    |___/  \__,_| |_|
                         |___/                                                                         
"""

def blink(kata,repeat = 3,second = 0.5):
    os.system('cls')
    for i in range(repeat):
        print("=======================================")
        print( "         ",kata)
        print("=======================================")
        time.sleep(second)
        os.system('cls')
        time.sleep(second)

def displayTable(data):
    tabelDisplay.clear()
    tabelDisplay.field_names = list(data.keys())
    tabelDisplay.add_row(list(data.values()))
    print(tabelDisplay)

def menuPilihan(judul,menu):
    while True:
        print("==============================")
        print("        ",judul)
        print("==============================")
        angka = []
        for i,x in enumerate(menu):
            print(f"|{i+1}. {x} ")
            angka.append(str(i+1))
        print("==============================")
        pilih = input("Masukkan pilihan : ")
        if pilih in angka:
            return int(pilih)
        else :
            print("Pilihan tidak ada")

def login():
        # try:
        kesempatan = 3
        while (kesempatan  > 0):
            # time.sleep(0.5)
            #os.system('cls')
            print("====  Portal Login  ====")
            username = input("Username : ").title()
            password = pwinput.pwinput(prompt="Password : ").title()
            temp = dataUser.head
            while temp != None:
                if (username == temp.data["username"] and password == temp.data["password"]):
                    # jika customer login dan antriannya sedang kosong maka langsung masuk
                    if temp.data["status"] == "Customer":
                        if dataAntrian.isEmpty():
                            dataAntrian.enqueue(Node({"Antrian":username}))
                        if username != dataAntrian.head.data["Antrian"]: # jika bukan data pertama
                            print("Sekarang bukan antrian anda, silahkan mengantri dulu")
                            # jika username tidak ada didalam antrian maka di tambahkan
                            if not dataAntrian.isExist(username):
                                dataAntrian.enqueue(Node({"Antrian":username}))
                            return
                        menuPembeli(username)
                        dataAntrian.dequeue()
                    #blink("login berhasil")
                    elif temp.data["status"] == "Admin":
                        menuAdmin()
                    return          
                temp = temp.next
            print("Login gagal, akun anda tidak terdaftar")
            kesempatan -=1
        print("Kesempatan anda login telah habis")
        # except :
        #     print("Terjadi Error")

"""                    _     _                 
  ___    ___    _ __  | |_  (_)  _ __     __ _ 
 / __|  / _ \  | '__| | __| | | | '_ \   / _` |
 \__ \ | (_) | | |    | |_  | | | | | | | (_| |
 |___/  \___/  |_|     \__| |_| |_| |_|  \__, |
                                         |___/ 
"""
def mergeSort(dataDict,jenis,tipe):
    if len(dataDict) > 1:
        r = round(len(dataDict)/2)#buat mecah sublistnya
        L = dataDict[:r] #sisi kiri
        R = dataDict[r:] #sisi kanan
        mergeSort(L,jenis,tipe)#buat sisi kiri
        mergeSort(R,jenis,tipe)#buat sisi kanan 
        i = j = k = 0

        #setelah elemennya habis lanjut ditaro di tempatnya 
        while i < len(L) and j < len(R):
            if tipe == 1:
                if L[i][jenis] < R[j][jenis]: #ascending
                    dataDict[k] = L[i]
                    i += 1
                else:
                    dataDict[k] = R[j] #descending
                    j += 1
            elif tipe == 2:
                if L[i][jenis] > R[j][jenis]:
                    dataDict[k] = L[i]
                    i += 1
                else:
                    dataDict[k] = R[j]
                    j += 1
            k += 1

        #kalo ada sisanya, lanjut ambil sisa elemennya terus taro diujung
        while i < len(L):
            dataDict[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            dataDict[k] = R[j]
            j += 1
            k += 1


def sortingLinkedList(linkedList,jenis,tipe):
    temp = linkedList.head
    dataDict = []
    # memasukan data linked list ke list
    while temp != None:
        dataDict.append(temp.data)
        temp = temp.next
    mergeSort(dataDict,jenis,tipe)
    # memasukan list ke linked list
    temp = linkedList.head
    for i in dataDict:
        temp.data = i
        temp = temp.next

def sortingMenu(linkedList,tipeSorting):
    try:
        pilih = menuPilihan("Pilihan Sorting",list(linkedList.head.data.keys()))
        jenis = list(linkedList.head.data.keys())[pilih-1]
        sortingLinkedList(linkedList,jenis,tipeSorting)
        linkedList.displayData()
        input("Tekan apa saja untuk melanjutkan")
    except ValueError:
        print("Masukkan dengan angka") 

def sortingData(linkedList):
    menu =  menuPilihan("Pilihan Sorting",["Ascending","Descending","Exit"])
    if menu == 1 or menu == 2:
        sortingMenu(linkedList,menu)
    elif menu == 3:
        return
            
"""
                                     _       _                 
  ___    ___    __ _   _ __    ___  | |__   (_)  _ __     __ _ 
 / __|  / _ \  / _` | | '__|  / __| | '_ \  | | | '_ \   / _` |
 \__ \ |  __/ | (_| | | |    | (__  | | | | | | | | | | | (_| |
 |___/  \___|  \__,_| |_|     \___| |_| |_| |_| |_| |_|  \__, |
                                                         |___/ 
"""
def fibMonaccianSearch(arr,jenis, x, n):
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1
    while (fibM > 1):
        i = min(offset+fibMMm2, n-1)
        if (arr[i][jenis] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i][jenis] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i
    # comparing the last element with x */
    if(fibMMm1 and arr[n-1][jenis] == x):
        return n-1
    # element not found. return -1
    return -1

def searchingData(linkedList):
    temp = linkedList.head
    dataDict = []
    # memasukan data linked list ke list
    while temp != None:
        dataDict.append(temp.data)
        temp = temp.next
    jenis = list(linkedList.head.data.keys())[0]
    target = input(f"Masukkan {jenis} yang ingin dicari: ").title()
    mergeSort(dataDict,jenis,1)
    find = fibMonaccianSearch(dataDict,jenis,target,len(dataDict))
    if find != -1:
        print("Data ditemukan")
        displayTable(dataDict[find])
    else:
        print("Data tidak ditemukan")


""" 
              _               _               
   __ _    __| |  _ __ ___   (_)  _ __     
  / _` |  / _` | | '_ ` _ \  | | | '_ \   
 | (_| | | (_| | | | | | | | | | | | | | 
  \__,_|  \__,_| |_| |_| |_| |_| |_| |_| 
"""                                                
def riwayatPembelian():
    if dataRiwayatPembelian.isEmpty():
        print("Belum ada riwayat pembelian")
        return
    temp = dataRiwayatPembelian.head
    total = 0
    while (temp != None):
        total = total + temp.data["data pembayaran"]
        temp = temp.next
    dataRiwayatPembelian.displayData()
    print(f"Total pendapatan anda : {total}")
    input("Tekan apa saja untuk melanjutkan")

def menuAdmin():
    while True:
        menu = menuPilihan("Menu Admin",["Data User","Data Barang","Exit"])
        if menu == 1:
            adminUser()
        elif menu == 2:
            adminBarang()
        elif menu == 3:
            break  

def adminUser():
    while True:
        menu = menuPilihan("Kelola User",["Tambah User","Tampilkan Data User","Ubah Data User","Hapus Data User","Sorting Data User","Cari Data User","Riwayat Pembelian","Kembali Ke Menu Sebelumnya"])
        if menu == 1:
            dataUser.addData({"username":"","password":"","status":"Customer"},"username","status",["Customer","Admin"])
        elif menu == 2:
            dataUser.displayData()
        elif menu == 3:
            dataUser.updateData()
        elif menu == 4:
            dataUser.deleteData()
        elif menu == 5:
            sortingData(dataUser)
        elif menu == 6:
            searchingData(dataUser)
        elif menu == 7:
            riwayatPembelian()
        elif menu == 8:
            break

def adminBarang():
    while True:
        menu = menuPilihan("Kelola Barang",["Tambah Barang Baru","Tampilkan Data Barang","Ubah Data Barang","Hapus Data Barang","Sorting Data Barang","Cari Data Barang","Kembali Ke Menu Sebelumnya"])
        if menu == 1:
            dataBarang.addData({"nama":"","jenis":"","stock":0,"harga":0},"nama")
        elif menu == 2:
            dataBarang.displayData()
        elif menu == 3:
            dataBarang.updateData()
        elif menu == 4:
            dataBarang.deleteData()
        elif menu == 5:
            sortingData(dataBarang)
        elif menu == 6:
            searchingData(dataBarang)
        elif menu == 7:
            print("Terima Kasih")
            break 


"""
                       _                                     
   ___   _   _   ___  | |_    ___    _ __ ___     ___   _ __ 
  / __| | | | | / __| | __|  / _ \  | '_ ` _ \   / _ \ | '__|
 | (__  | |_| | \__ \ | |_  | (_) | | | | | | | |  __/ | |   
  \___|  \__,_| |___/  \__|  \___/  |_| |_| |_|  \___| |_|   
"""                                                            

def register():
    try:
        while True:
            # time.sleep(0.5)
            # os.system('cls')
            print("Portal Registrasi")
            username = input("Masukkan username : ").title()
            if dataUser.isExist(username,"username"):
                print("username sudah ada")
            elif username.isnumeric() == True :
                print("username tidak boleh angka")
            else:
                password = input("Masukkan password : ").title()
                dataUser.addLast(Node({"username":username,"password":password,"status":"Customer"}))
                dataAntrian.enqueue(Node({"Antrian":username}))
                print("Registrasi berhasil")
                break
    except ValueError:
        print("Terjadi Eror")



def tambahPesanan():
    while True:
        nama = input("Masukan nama pesanan : ").title()
        if dataBarang.isExist(nama,"nama"):
            while True:
                try:
                    jumlah = int(input("Masukan jumlah pesanan : "))
                    if jumlah > dataBarang.getData(nama,"nama")["stock"]:
                        print("Stok tidak cukup")
                        continue
                    elif jumlah < 1:
                        print("Pesan minimal 1 minuman")
                        continue
                    else:
                        totalPesanan.addLast(Node({"nama":nama,"jumlah":jumlah,"harga":dataBarang.getData(nama,"nama")["harga"] * jumlah}))
                        return
                except ValueError:
                    print("Inputan hanya menerima berupa angka")
        else:
            print("Maaf pesanan tidak tersedia")

def konfirmasiPesanan(userLogin):
    if totalPesanan.isEmpty():
        print("Anda belum melakukan pemesanan")
        return
    temp = totalPesanan.head
    total = 0
    while (temp != None):
        total = total + temp.data["harga"]
        temp = temp.next
    totalPesanan.displayData()
    print(f"Total pesanan anda : {total}")
    while True:
        pilihan = menuPilihan("Ingin membayar pesanan ini ?",["Iya","Belum"])
        if pilihan == 1:
                bayarPesanan = int(input("Masukan nominal uang anda : "))
                if bayarPesanan < total:
                    print("Uang anda tidak cukup")
                    continue
                else:
                    print("Pembayaran berhasil")
                    uangKembalian = bayarPesanan - total
                    temp = totalPesanan.head
                    while temp != None:
                        dataUpdate = dataBarang.getData(temp.data["nama"],"nama")
                        dataUpdate["stock"] = dataUpdate["stock"] - temp.data["jumlah"]
                        dataBarang.setData(temp.data["nama"],"nama",dataUpdate)
                        temp = temp.next
                    print(f"Uang kembalian anda : {uangKembalian}")
                    dataRiwayatPembelian.addLast(Node({"nama pembeli":userLogin,"data pembayaran":total}))
                    totalPesanan.clearData()
                    return
        if pilihan == 2:
            break

def menuPembeli(userLogin):
    while True:
        #time.sleep(0.5)
        os.system('cls')
        print("____________________________________________")
        print("|==========================================|")
        print("|* * * * * * * * * * * * * * * * * * * * * |")
        print("|                Pondok Teh                |")
        print("|            JL. Jalan Jalan No.1          |")
        print("|                Samarinda                 |")
        print("|* * * * * * * * * * * * * * * * * * * * * |")
        print("|==========================================|")
        dataBarang.displayData(["stock"])
        menu = menuPilihan("Menu Pembeli",["Tambah Pesanan","Hapus Pesanan","Lihat Pesanan","Konfirmasi Pesanan","Exit"])
        if menu == 1:
            tambahPesanan()
        elif menu == 2:
            totalPesanan.deleteData()
        elif menu == 3:
            totalPesanan.displayData()
            input("Tekan apa saja untuk melanjutkan")
        elif menu == 4:
            konfirmasiPesanan(userLogin)
        elif menu == 5:
            print("Exit")
            break

"""
                      _                                              
  _ __ ___     __ _  (_)  _ __      _ __ ___     ___   _ __    _   _ 
 | '_ ` _ \   / _` | | | | '_ \    | '_ ` _ \   / _ \ | '_ \  | | | |
 | | | | | | | (_| | | | | | | |   | | | | | | |  __/ | | | | | |_| |
 |_| |_| |_|  \__,_| |_| |_| |_|   |_| |_| |_|  \___| |_| |_|  \__,_|
"""                                                                    

def menuAwal():
    # time.sleep(0.5)
    # os.system('cls')
    dataUser.readCSV()
    dataBarang.readCSV()
    dataRiwayatPembelian.readCSV()
    while True :
        dataAntrian.displayData()
        menu = menuPilihan("Menu Utama",["Login","Register","Exit"])
        if menu == 1:
            login()  
        elif menu == 2:
            register()
        elif menu == 3:
            break
    dataUser.writeCSV()
    dataBarang.writeCSV()
    dataRiwayatPembelian.writeCSV()

if __name__ == "__main__":
    menuAwal()  