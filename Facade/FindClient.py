class Proprietar:
    def __init__(self, nume, numar_telefon):
        self.nume = nume
        self.numar_telefon = numar_telefon


class Imobil:
    def __init__(self, adresa, proprietar):
        self.adresa = adresa
        self.proprietar = proprietar


class AgentieImobiliara:
    def __init__(self, lista_imobile):
        self.lista_imobile = lista_imobile

    def cauta_imobil(self, adresa):
        for imobil in self.lista_imobile:
            if imobil.adresa == adresa:
                return imobil
        return None


class FacadeAgentieImobiliara:
    def __init__(self, lista_imobile):
        self.agentie_imobiliara = AgentieImobiliara(lista_imobile)

    def obtine_numar_telefon_proprietar(self, adresa_imobil):
        imobil = self.agentie_imobiliara.cauta_imobil(adresa_imobil)
        if imobil is not None:
            return imobil.proprietar.numar_telefon
        return None


imobil1 = Imobil("str. Primaverii 10", Proprietar("Ion Popescu", "0722 123 456"))
imobil2 = Imobil("str. Nucilor 5", Proprietar("Maria Ionescu", "0733 987 654"))
lista_imobile = [imobil1, imobil2]

facade_agentie_imobiliara = FacadeAgentieImobiliara(lista_imobile)

numar_telefon = facade_agentie_imobiliara.obtine_numar_telefon_proprietar("str. Primaverii 10")
print(numar_telefon)

numar_telefon = facade_agentie_imobiliara.obtine_numar_telefon_proprietar("str. Nucilor 5")
print(numar_telefon)

numar_telefon = facade_agentie_imobiliara.obtine_numar_telefon_proprietar("str. Violetei 3")
print(numar_telefon)
