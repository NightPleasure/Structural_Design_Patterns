class Anunt:
    def __init__(self, adresa, num_camere, num_bai, mp, pret):
        self.adresa = adresa
        self.num_camere = num_camere
        self.num_bai = num_bai
        self.mp = mp
        self.pret = pret

    def afisare(self):
        print("Adresa:", self.adresa)
        print("Număr de camere:", self.num_camere)
        print("Număr de băi:", self.num_bai)
        print("Metri pătrați:", self.mp)
        print("Preț:", self.pret)


class DecoratorPozeProfesionale(Anunt):
    def __init__(self, anunt):
        self.anunt = anunt
        self.pret = 1000

    def afisare(self):
        self.anunt.afisare()
        print("Poze profesionale:", self.pret)


anunt = Anunt("Strada Principală 123", 3, 2, 1500, 200000)
anunt_cu_poze = DecoratorPozeProfesionale(anunt)
anunt_cu_poze.afisare()
