# import pandas as pd

# from pandas._config import (
#     get_option,
#     set_option,
#     reset_option,
#     describe_option,
#     option_context,
#     options,
# )

# inheritance
class Sepatu:
    def __init__(self, jenis, ukuran, warna, model):
        self.__jenis = jenis
        self.__ukuran = ukuran
        self.__warna = warna
        self.__model = model
    def get_jenis(self):
        return self.__jenis
    def get_ukuran(self):
        return self.__ukuran
    def get_warna(self):
        return self.__warna
    def get_model(self):
        return self.__model

    def keterangan(self):
        return(f'Saya membeli sepatu {self.__jenis} ukuran {str(self.__ukuran)} warna {self.__warna} model {self.__model}')

class Sepatu_kulit(Sepatu):
    def __init__(self, jenis, ukuran, warna, model):
        super().__init__(jenis, ukuran, warna, model)

class Sepatu_karet(Sepatu):
    def __init__(self, jenis, ukuran, warna, model):
        super().__init__(jenis, ukuran, warna, model)

class Sepatu_denim(Sepatu):
    def __init__(self, jenis, ukuran, warna, model):
        super().__init__(jenis, ukuran, warna, model)


def main():
    kulit = Sepatu_kulit('kulit', 42, 'Hitam', 'pantopel')
    print(kulit.keterangan())
    karet = Sepatu_karet('karet', 40, 'cokelat', 'boots')
    print(karet.keterangan())
    denim = Sepatu_denim('denim', 38, 'biru', 'sneakers')
    print(denim.keterangan())
main()




#override
class Sepatu:
    def __init__(self, nama, jenis, ukuran, warna, model):
        self.__nama = nama
        self.__jenis = jenis
        self.__ukuran = ukuran
        self.__warna = warna
        self.__model = model
    def get_nama(self):
        return self.__nama
    def get_jenis(self):
        return self.__jenis
    def get_ukuran(self):
        return self.__ukuran
    def get_warna(self):
        return self.__warna
    def get_model(self):
        return self.__model

    def keterangan(self):
        return(f'{self.__nama} membeli sepatu {self.__jenis} ukuran {str(self.__ukuran)} warna {self.__warna} model {self.__model}')

class Sepatu_kulit(Sepatu):
    def __init__(self, nama, jenis, ukuran, warna, model):
        super().__init__(nama, jenis, ukuran, warna, model)
        
class Sepatu_karet(Sepatu):
    def __init__(self, nama, jenis, ukuran, warna, model, kode = 'ATT000'):
        super().__init__(nama, jenis, ukuran, warna, model)
        self.__kode = kode
    def keterangan(self):
        return super().keterangan() + ' dengan kode ' + self.__kode

class Sepatu_denim(Sepatu):
    def __init__(self, nama, jenis, ukuran, warna, model):
        super().__init__(nama, jenis, ukuran, warna, model)


def main():
    kulit = Sepatu_kulit('Ilham', 'kulit', 42, 'Hitam', 'pantopel')
    print(kulit.keterangan())

    karet = Sepatu_karet('Yoga', 'karet', 40, 'cokelat', 'boots')
    print(karet.keterangan())

    denim = Sepatu_denim('Hesti', 'denim', 38, 'biru', 'sneakers')
    print(denim.keterangan())

main() 



# # program lengkap

# nama_anggota = ['Salmaa Alifia Rizka','Yoga Randiansyah','Hestiavin Eka Dhelpi','Moch Miftah Fauzan A','Ilham Ardian']
# nim = [215060700111006, 215060700111040, 215060701111010, 215060701111037, 215060707111048]

# print('-'*40)
# tabel={
#     'Nama':nama_anggota,
#     'NIM':nim,}

# pd.set_option('display.colheader_justify','center')
# pddataframe1 = pd.DataFrame(data = tabel)
# pddataframe1.index +=1
# print(pddataframe1)
# print('-'*40) 


class Sepatu:
    def __init__(self, nama, jenis, ukuran, warna, model):
        self.__nama = nama
        self.__jenis = jenis
        self.__ukuran = ukuran
        self.__warna = warna
        self.__model = model
    def get_nama(self):
        return self.__nama
    def get_jenis(self):
        return self.__jenis
    def get_ukuran(self):
        return self.__ukuran
    def get_warna(self):
        return self.__warna
    def get_model(self):
        return self.__model

    def keterangan(self):
        return(f'{self.__nama} membeli sepatu {self.__jenis} ukuran {str(self.__ukuran)} warna {self.__warna} model {self.__model}')

class Sepatu_kulit(Sepatu):
    def __init__(self, nama, jenis, ukuran, warna, model):
        super().__init__(nama, jenis, ukuran, warna, model)
        
class Sepatu_karet(Sepatu):
    def __init__(self, nama, jenis, ukuran, warna, model, kode = 'ATT000'):
        super().__init__(nama, jenis, ukuran, warna, model)
        self.__kode = kode
    def keterangan(self):
        return super().keterangan() + ' dengan kode ' + self.__kode

class Sepatu_denim(Sepatu):
    def __init__(self, nama, jenis, ukuran, warna, model):
        super().__init__(nama, jenis, ukuran, warna, model)


def main():
    kulit = Sepatu_kulit('Ilham', 'kulit', 42, 'Hitam', 'pantopel')
    print(kulit.keterangan())

    karet = Sepatu_karet('Yoga', 'karet', 40, 'cokelat', 'boots')
    print(karet.keterangan())

    denim = Sepatu_denim('Hesti', 'denim', 38, 'biru', 'sneakers')
    print(denim.keterangan())

main() 