class Rumah():
    def __init__ (self, thbangun, pondasi, modelrumah, warnarumah, luasrumah, hargarumah):
        self.thbangun = thbangun
        self.pondasi = pondasi
        self.modelrumah = modelrumah
        self.warnarumah = warnarumah
        self.luasrumah = luasrumah
        self.hargarumah = hargarumah

    def tempatberteduh (self):
        print(f'Rumah warna {self.warnarumah} untuk tempat berteduh')

    def menyimpanbarang (self): 
        print(f'Rumah ini memiliki luas {self.luasrumah}, cukup untuk menyimpan barang dengan aman')

    def tempatberkumpul (self): 
        print(f'Rumah dengan model {self.modelrumah} cocok untuk tempat berkumpul keluarga')

    def data(self):
        print(f'Rumah ini berdiri tahun {self.thbangun}')
        print(f'Rumah ini berpondasi {self.pondasi}')
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


