from abc import ABC, abstractmethod

class ItemPerpustakaan(ABC):
    def __init__(self,id_item,judul):
        self.id_item = id_item
        self.__judul = judul

    @abstractmethod
    def deskripsi(self):
        pass

    def get_id(self):
        return self.id_item
    
    def get_judul(self):
        return self.__judul
    

class Penulis:
    def __init__(self,nama,kewarganegaraan):
        self.nama = nama
        self.kewarganegaraan = kewarganegaraan

    
    def __str__(self):
        return f"{self.nama} ({self.kewarganegaraan})"
    

class Buku(ItemPerpustakaan):
    def __init__(self, id_item, judul, penulis:Penulis):
        super().__init__(id_item, judul)
        self.penulis = penulis

    def deskripsi(self):
        return f"Buku: {self.get_judul()}  |  Penulis: {self.penulis.nama} ({self.penulis.kewarganegaraan})"
    

class ManagerPerpustakaan:
    def __init__(self):
        self.koleksi = []
        self.terurut = False

    def validasi_id_unik(self,id):
        for buku in self.koleksi:
            if buku.get_id() == id:
                return False
        return True
        
    def tambah_buku_baru(self):
        input_id = int(input("masukkan ID buku baru (Angka) : "))

        if self.validasi_id_unik(input_id) is not False:
            print("ID Valid")
            input_judul = input("Masukkan judul buku: ")
            input_penulis = input("Masukkan nama penulis: ")
            input_warganegaraan = input("Masukkan kewarganegaraan penulis: ")
            penulis_baru = Penulis(input_penulis,input_warganegaraan)
            buku_baru_tervalidasi = Buku(input_id,input_judul,penulis_baru)
            self.koleksi.append(buku_baru_tervalidasi)
            self.terurut = False
            print(f"[SUKSES] '{input_judul}' karya {input_penulis} berhasil ditambahkan.")

    def urutkan_koleksi(self):
        length_koleksi = len(self.koleksi)
        for i in reversed(range(length_koleksi)):
            swapped = False
            for j in range(i):
                if self.koleksi[j].get_id() > self.koleksi[j + 1].get_id():
                    swapped = True
                    self.koleksi[j], self.koleksi[j + 1] = self.koleksi[j + 1], self.koleksi[j]
            if not swapped:
                break
        self.terurut = True
        print("")
        print("Koleksi berhasil diurutkan")
        print("")
        return self.koleksi, self.terurut 
    
    def cari_buku(self,id_target):
        if self.terurut == False:
            print("[Peringatan] Mohon untuk mengurutkan data terlebih dahulu")
            return
        left = 0
        right = len(self.koleksi) - 1

        while left <= right:
            midPoint = left + (right - left) // 2
            current_data = self.koleksi[midPoint]
            if current_data.get_id() == id_target:
                 print(f"[Ditemukan] {current_data.get_judul()}     |  {current_data.penulis.nama}")
                 print(f"Detail Penulis: {current_data.penulis}" )
                 return
            if id_target < current_data.get_id():
                right = midPoint - 1
            else:
                left = midPoint + 1
        print(f"[Hasil] ID {id_target} tidak ditemukan")
        return -1
    
    def tampilkan_koleksi(self):
        if len(self.koleksi) == 0 :
            print("")
            print("Buku Masih Kosong!")
            print("")
            return
        print(f"{'ID':<10}| Informasi Buku")
        print("-"*25) 
        
        for koleksi in self.koleksi:
            print(f"[{koleksi.get_id()}] {koleksi.deskripsi()}")
    

sistem_perpustakaan = ManagerPerpustakaan()


while True:
    print("="*25)
    print('LIBSEARCH - DIGITAL ARCHIEVE (ASSOSIATION)')
    print("="*25)

    print("""
    1. Tambah Buku Baru
    2. Tampilkan Semua Koleksi
    3. Urutkan Koleksi (Bubble sort)
    4. Cari Buku (Binary Search)
    5. Keluar
        
    """)
    inputan_user = int(input("Pilih Menu (1 - 5): "))
    if inputan_user == 1:
        sistem_perpustakaan.tambah_buku_baru()
    elif inputan_user == 2:
        sistem_perpustakaan.tampilkan_koleksi()
    elif inputan_user == 3:
        sistem_perpustakaan.urutkan_koleksi()
    elif inputan_user == 4:
        target = int(input("Masukkan ID buku yang dicari: "))
        sistem_perpustakaan.cari_buku(target)
    elif inputan_user == 5 :
        print("Terima kasih, Sampai jumpa")
        break
    else:
        print("Inputan Tidak Valid")

     
