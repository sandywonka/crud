class Cart(object):
    def __init__(self):
        self.item = {}

    def tambahProduk(self, kodeProduk, kuantitas):
        self.kodeProduk = kodeProduk
        self.kuantitas = kuantitas
        self.item.update({kodeProduk: kuantitas})

    def hapusProduk(self, kodeProduk):
        try:
            del self.item[kodeProduk]
        except:
            pass

    def tampilkanCart(self):
        print(self.item)
