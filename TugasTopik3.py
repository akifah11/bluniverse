class Rumah():
    def __init__ (self, thbangun, pondasi, modelrumah, warnarumah, luasrumah, hargarumah):
        self.__thbangun = thbangun      # properti privat
        self.__pondasi = pondasi        # properti privat
        self.modelrumah = modelrumah
        self.warnarumah = warnarumah
        self.luasrumah = luasrumah
        self.hargarumah = hargarumah

    def get_thbangun(self):      # method getter
        return self.__thbangun
    
    def get_pondasi(self):       # method getter
        return self.__pondasi
    
    def set_thbangun(self, thbangun):    # method setter
        self.__thbangun = thbangun

    def set_pondasi(self, pondasi):      # method setter
        self.__pondasi = pondasi    

    def tempatberteduh (self):
        print(f'Rumah warna {self.warnarumah} untuk tempat berteduh')

    def menyimpanbarang (self): 
        print(f'Rumah ini memiliki luas {self.luasrumah}, cukup untuk menyimpan barang dengan aman')

    def tempatberkumpul (self): 
        print(f'Rumah dengan model {self.modelrumah} cocok untuk tempat berkumpul keluarga')

    def data(self):
        print(f'Rumah ini bermodel {self.modelrumah}')
        print(f'Rumah ini berwarna {self.warnarumah}')
        print(f'Rumah ini memiliki luas {self.luasrumah}')
        print(f'Rumah ini dibeli dengan harga {self.hargarumah}')

rumahku = Rumah(2005, 'batu bata', 'joglo', 'coklat', '500 m2', '100 juta')
rumahmu = Rumah(2018, 'beton bertulang', 'minimalis', 'biru', ' 500 m2', '450 juta')

rumahku.tempatberteduh()  
rumahku.menyimpanbarang()
rumahku.tempatberkumpul()
rumahku.data()
print("\n") 
rumahmu.tempatberteduh()
rumahmu.menyimpanbarang()
rumahmu.tempatberkumpul()
rumahmu.data()

#objek baru dari class dan akses variabel privat
print('\n Akses variabel privat dengan method getter dan setter')
rumahnya = Rumah(2000, 'batu kali', 'industrial', 'abu abu', '900 m2', '600 juta')
print(rumahnya.get_thbangun())
print(rumahnya.get_pondasi())

rumahnya.set_thbangun(2001)
rumahnya.set_pondasi('kayu ulin')
print(rumahnya.get_thbangun())
print(rumahnya.get_pondasi())