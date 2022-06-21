# ANCHOR Dictionary data pasien
dictPasien = {
    "P1": {
        "nama" : "Aldo",
        "usia" : "11",
        "kelamin" : "L",
        "telepon" : "48935786",
        "poli" : "Umum",
        "dokter" : "Surya"
    },
    "P2" : {
        "nama" : "Beni",
        "usia" : "22",
        "kelamin" : "L",
        "telepon" : "75246879",
        "poli" : "Mata",
        "dokter" : "Marni"
    },
    "P3" : {
        "nama" : "Cintya",
        "usia" : "33",
        "kelamin" : "P",
        "telepon" : "66843588",
        "poli" : "THT",
        "dokter" : "Damar"
    },
    "P4" : {
        "nama" : "Desi",
        "usia" : "44",
        "kelamin" : "P",
        "telepon" : "66459877",
        "poli" : "Gigi",
        "dokter" : "Angel"
    }
}


# ANCHOR Functions
def lihatSemuaPasien():
    if(len(dictPasien) != 0):
        print('\n------------------------------------- Daftar Pasien -------------------------------------\n')
        print("ID. Pasien\t| Nama  \t| Usia\t| Jenis Kelamin\t| Telepon\t| Poli\t| Dokter")
        for i in dictPasien :
            print("{}\t\t| {}  \t| {}\t| {}\t\t| {}\t| {}\t| {}".format(i,dictPasien[i]["nama"],dictPasien[i]["usia"],dictPasien[i]["kelamin"],
                dictPasien[i]["telepon"],dictPasien[i]["poli"],dictPasien[i]["dokter"]))
    else:
        print("\n* Data Pasien tidak tersedia *")        

def cariPasien():
    if(len(dictPasien) != 0):
        idPasien = input("\nMasukkan ID Pasien yang dicari: ")
        if(idPasien in dictPasien):
            print("\nID. Pasien\t| Nama  \t| Usia\t| Jenis Kelamin\t| Telepon\t| Poli\t| Dokter")
            print("{}\t\t| {}  \t| {}\t| {}\t\t| {}\t| {}\t| {}".format(idPasien,dictPasien[idPasien]["nama"],dictPasien[idPasien]["usia"],
                dictPasien[idPasien]["kelamin"],dictPasien[idPasien]["telepon"],dictPasien[idPasien]["poli"],dictPasien[idPasien]["dokter"])) 
        else:
            print("\n* Data Pasien yang dicari tidak tersedia *")
    else:
        print("\n* Data Pasien tidak tersedia *")

def tambahPasien():
    print('\nInput Data Pasien yang ingin ditambahkan\n')
    idPasien = input("ID (harus berbeda tiap pasien): ")
    if(idPasien in dictPasien):
        print("\n* Data Pasien Sudah Ada *")
    else:
        namaPasien = input("Nama : ")
        usiaPasien = input("Usia (angka) : ")
        kelaminPasien = input("Jenis Kelamin (L/P): ")
        teleponPasien = input("Telepon : ")
        poliPasien = input("Poli : ")
        dokterPasien = input("Dokter : ") 
        pilihanSimpan = input("\nSimpan data pasien ? (1.ya / 2.tidak): ")
        if(pilihanSimpan == "1"):
            dictPasien[idPasien] = {
                "nama" : namaPasien,
                "usia" : usiaPasien,
                "kelamin" : kelaminPasien,
                "telepon" : teleponPasien,
                "poli" : poliPasien,
                "dokter" : dokterPasien
            }
            print("\n* Data pasien berhasil tersmipan *")
            lihatSemuaPasien()
        elif(pilihanSimpan != "1" or pilihanSimpan != "2"):
            print("\n* Pilihan tidak tersedia *")

def ubahPasien():
    idPasien = input("\nMasukkan ID pasien yang ingin diubah datanya : ")
    if idPasien in dictPasien:
        print("\nID. Pasien\t| Nama  \t| Usia\t| Jenis Kelamin\t| Telepon\t| Poli\t| Dokter")
        print("{}\t\t| {}  \t| {}\t| {}\t\t| {}\t| {}\t| {}".format(idPasien,dictPasien[idPasien]["nama"],dictPasien[idPasien]["usia"],
            dictPasien[idPasien]["kelamin"],dictPasien[idPasien]["telepon"],dictPasien[idPasien]["poli"],dictPasien[idPasien]["dokter"])) 
        pilihanSimpan = input("\nUbah data pasien ini? (1.ya / 2.tidak): ")
        if(pilihanSimpan == "1"):
            namaPasien = input("Nama : ")
            usiaPasien = input("Usia (angka) : ")
            kelaminPasien = input("Jenis Kelamin (L/P): ")
            teleponPasien = input("Telepon : ")
            poliPasien = input("Poli : ")
            dokterPasien = input("Dokter : ") 
            pilihanSimpan = input("\nSimpan perubahan data pasien ? (1.ya / 2.tidak): ")
            if(pilihanSimpan == "1"):
                dictPasien[idPasien] = {
                    "nama" : namaPasien,
                    "usia" : usiaPasien,
                    "kelamin" : kelaminPasien,
                    "telepon" : teleponPasien,
                    "poli" : poliPasien,
                    "dokter" : dokterPasien
                }
                print("\n* Data pasien berhasil diubah *")
                lihatSemuaPasien()
            elif(pilihanSimpan != "1" or pilihanSimpan != "2"):
                print("\n* Pilihan tidak tersedia *")
    else:
        print("\n* Data pasien tidak ada *")

def hapusPasien():
    idPasien = input("\nMasukkan ID pasien yang ingin dihapus : ")
    if idPasien in dictPasien:
        print("\nID. Pasien\t| Nama  \t| Usia\t| Jenis Kelamin\t| Telepon\t| Poli\t| Dokter")
        print("{}\t\t| {}  \t| {}\t| {}\t\t| {}\t| {}\t| {}".format(idPasien,dictPasien[idPasien]["nama"],dictPasien[idPasien]["usia"],
            dictPasien[idPasien]["kelamin"],dictPasien[idPasien]["telepon"],dictPasien[idPasien]["poli"],dictPasien[idPasien]["dokter"])) 
        pilihanSimpan = input("\nHapus data pasien ini ? (1.ya / 2.tidak): ")
        if(pilihanSimpan == "1"):
            del dictPasien[idPasien]
            print("\n* Data pasien berhasil dihapus *")
            lihatSemuaPasien()        
        elif(pilihanSimpan != "1" or pilihanSimpan != "2"):
            print("\n* Pilihan tidak tersedia *")   
    else:
        print("\n* Data pasien tidak ada *")

def keMenuUtama():
    pilihanKembali = input("\nKembali ke menu utama? (1.ya / 2.tidak) : ")
    if(pilihanKembali == "1"):
        menuAktif = False
    elif(pilihanKembali == "2"):
        menuAktif = True
    else:
        print("\n* Pilihan tidak tersedia *")
        menuAktif = True
    return menuAktif

    
menuUtama = True

while menuUtama == True :
    # ANCHOR Menu utama
    pilihanMenuUtama = input('''
__________________________________________________
    
            SISTEM DATA PASIEN 
               RS ABDI SEHAT
__________________________________________________

    Menu Utama:
    1. Lihat Daftar Pasien
    2. Tambah Pasien
    3. Ubah Data Pasien
    4. Hapus Pasien
    5. Keluar Program

    Masukkan pilihan angka menu (1/2/3/4/5) : ''')

    if(pilihanMenuUtama == "1") :
        # ANCHOR Menu Utama > Lihat Daftar Pasien
        menuLihatPasien = True

        while(menuLihatPasien == True):
            pilihanMenuLihat = input('''
--------------------------------------------------
            Lihat Daftar Pasien
--------------------------------------------------

    Menu Lihat Daftar Pasien :
    1. Semua pasien
    2. Cari pasien
    3. Kembali ke menu utama

    Masukkan pilihan angka menu (1/2/3) : ''')

            if(pilihanMenuLihat == "1"):
                # ANCHOR Menu Utama > Lihat Daftar Pasien > Semua Pasien
                lihatSemuaPasien()
            elif(pilihanMenuLihat == "2"):
                # ANCHOR Menu Utama > Lihat Daftar Pasien > Cari Pasien
                cariPasien()
            elif(pilihanMenuLihat == "3"):
                # ANCHOR Menu Utama > Lihat Daftar Pasien > Kembali ke Menu Utama
                menuLihatPasien = keMenuUtama()
            else:
                print("\n* Pilihan tidak tersedia *")
        
    elif(pilihanMenuUtama == '2') :
        # ANCHOR Menu Utama > Tambah Pasien
        menuTambahPasien = True

        while(menuTambahPasien == True):
            pilihanMenuTambah = input('''
--------------------------------------------------
                Tambah Pasien
--------------------------------------------------

    Menu Tambah Pasien :
    1. Input data pasien yang ingin ditambah
    2. Kembali ke menu utama

    Masukkan pilihan angka menu (1/2) : ''')

            if(pilihanMenuTambah == "1"):
                # ANCHOR Menu Utama > Tambah Pasien > Input Data Pasien
                tambahPasien()
            elif(pilihanMenuTambah == "2"):
                # ANCHOR Menu Utama > Tambah Pasien > Kembali ke Menu Utama
                menuTambahPasien = keMenuUtama()
            else:
                print("\n* Pilihan tidak tersedia *")

    elif(pilihanMenuUtama == '3'):
        # ANCHOR Menu Utama > Ubah Data Pasien
        menuUbahPasien = True

        while(menuUbahPasien == True):
            pilihanMenuUbah = input('''
--------------------------------------------------
                Ubah Data Pasien
--------------------------------------------------

    Menu Ubah Data Pasien :
    1. Pilih data pasien yang ingin diubah
    2. Kembali ke menu utama

    Masukkan pilihan angka menu (1/2) : ''')

            if(pilihanMenuUbah == "1"):
                # ANCHOR Menu Utama > Ubah Data Pasien > Input Data Pasien
                ubahPasien()
            elif(pilihanMenuUbah == "2"):
                # ANCHOR Menu Utama > Ubah Data Pasien > Kembali ke Menu Utama
                menuUbahPasien = keMenuUtama()
            else:
                print("\n* Pilihan tidak tersedia *")

    elif(pilihanMenuUtama == '4'):
        # ANCHOR Menu Utama > Hapus Pasien
        menuHapusPasien = True

        while(menuHapusPasien == True):
            pilihanMenuHapus = input('''
--------------------------------------------------
                Hapus Pasien
--------------------------------------------------

    Menu Hapus Pasien :
    1. Pilih data pasien yang ingin dihapus
    2. Kembali ke menu utama

    Masukkan pilihan angka menu (1/2) : ''')

            if(pilihanMenuHapus == "1"):
                # ANCHOR Menu Utama > Hapus Pasien > Input Data Pasien
                hapusPasien()
            elif(pilihanMenuHapus == "2"):
                # ANCHOR Menu Utama > Hapus Pasien > Kembali ke Menu Utama
                menuHapusPasien = keMenuUtama()
            else:
                print("\n* Pilihan tidak tersedia *")

    elif(pilihanMenuUtama == '5'):
        # ANCHOR Menu Utama > Keluar Program
        menuUtama = False

    else:
        print("\n* Pilihan tidak tersedia *")

