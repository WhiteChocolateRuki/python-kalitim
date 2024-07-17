
class Seyehat():
    def __init__(self, kalkis, varis):
        self.kalkis = kalkis
        self.varis = varis
    def sure(self):
        return "12 ucus süremizdir"
    def anons(self):
        return "{}-{} uçağımız kalkmak üzere".format(self.kalkis, self.varis)

class Otobus(Seyehat):
    def __init__(self, mola_saatleri, kalkis, varis):
        super().__init__(kalkis, varis)
        self.mola_saatleri = mola_saatleri
 
    def mola_anons(self):
        return "Mola saatimiz: {}".format(self.mola_saatleri)

kalkis = input("Kalkış noktasını girin: ")
varis = input("Varış noktasını girin: ")
mola_saatleri = input("Mola saatlerini girin: ")

seyeh = Seyehat(kalkis, varis)
print(seyeh.anons())

otobus = Otobus(mola_saatleri, kalkis, varis)
print(otobus.mola_anons())


