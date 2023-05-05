class Apartament:
    def __init__(self, pret, adresa, descriere, nr_camere):
        self.pret = pret
        self.adresa = adresa
        self.descriere = descriere
        self.nr_camere = nr_camere

    def afiseaza_informatii(self):
        print(
            f"Apartament cu {self.nr_camere} "
            f"camere la adresa {self.adresa}, "
            f"pret: {self.pret}, "
            f"descriere: {self.descriere}")


class Complex(Apartament):
    def __init__(self, pret, adresa, descriere):
        super().__init__(pret, adresa, descriere, nr_camere=None)
        self.apartamente = []

    def adauga_apartament(self, apartament):
        self.apartamente.append(apartament)

    def afiseaza_informatii(self):
        super().afiseaza_informatii()
        for apartament in self.apartamente:
            apartament.afiseaza_informatii()


apartament1 = Apartament(100000, "Strada Stefan cel Mare, 68", "Apartament cu 2 camere", nr_camere=2)
apartament2 = Apartament(120000, "Strada Alexandru cel Bun 42", "Apartament cu 3 camere", nr_camere=3)
apartament3 = Apartament(130000, "Strada Bucuresti 3A", "Apartament cu 4 camere", nr_camere=4)

complex = Complex(500000, "Strada Viilor 13A", "Complex rezidențial")
complex.adauga_apartament(apartament1)
complex.adauga_apartament(apartament2)
complex.adauga_apartament(apartament3)

complex_mare = Complex(1000000, "Strada Stefan Voda 45/3", "Complex mare")
complex_mare.adauga_apartament(complex)

complex_mare.afiseaza_informatii()
