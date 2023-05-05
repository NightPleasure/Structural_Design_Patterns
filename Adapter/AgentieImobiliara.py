class Imobil:
    def __init__(self, nume_proprietar, adresa, suprafata, nr_camere, pret):
        self.nume_proprietar = nume_proprietar
        self.adresa = adresa
        self.suprafata = suprafata
        self.nr_camere = nr_camere
        self.pret = pret


class AgentieImobiliara:
    def __init__(self, lista_imobile):
        self.lista_imobile = lista_imobile

    def cauta_imobil(self, criterii):
        pass


class AnuntImobiliar:
    def __init__(self, nume_proprietar, adresa, suprafata, nr_camere, pret):
        self.nume_proprietar = nume_proprietar
        self.adresa = adresa
        self.suprafata = suprafata
        self.nr_camere = nr_camere
        self.pret = pret


class AdaptorImobilAnunt:
    def __init__(self, imobil):
        self.nume_proprietar = imobil.nume_proprietar
        self.adresa = imobil.adresa
        self.suprafata = imobil.suprafata
        self.nr_camere = imobil.nr_camere
        self.pret = imobil.pret

    def get_anunt_imobiliar(self):
        return AnuntImobiliar(
            self.nume_proprietar,
            self.adresa,
            self.suprafata,
            self.nr_camere,
            self.pret
        )


imobil = Imobil("Victor Barbaian", "str. Primaverii nr. 10", 100, 3, 250000)
anunt = AdaptorImobilAnunt(imobil).get_anunt_imobiliar()

print(f"Anuntul imobiliar pentru proprietatea de la adresa {anunt.adresa} este disponibil la prețul de {anunt.pret}.")
