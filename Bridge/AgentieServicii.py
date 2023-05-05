from abc import ABC, abstractmethod


class Proprietate(ABC):
    @abstractmethod
    def get_descriere(self):
        pass


class Serviciu(ABC):
    @abstractmethod
    def ofera_serviciu(self):
        pass


class Casa(Proprietate):
    def get_descriere(self):
        return "Casa cu 3 camere si gradina mare"


class Vanzare(Serviciu):
    def ofera_serviciu(self):
        return "Vanzare"


class AgentieImobiliara:
    def __init__(self):
        self.proprietati = []
        self.servicii = []

        casa1 = Casa()
        vanzare1 = Vanzare()

        casa2 = Casa()
        vanzare2 = Vanzare()

        self.proprietati.append(casa1)
        self.proprietati.append(casa2)

        self.servicii.append(vanzare1)
        self.servicii.append(vanzare2)

    def afiseaza_proprietati(self):
        for proprietate in self.proprietati:
            print(proprietate.get_descriere())

    def afiseaza_servicii(self):
        for serviciu in self.servicii:
            print(serviciu.ofera_serviciu())


agentie = AgentieImobiliara()

print("Proprietati:")
agentie.afiseaza_proprietati()

print("Servicii:")
agentie.afiseaza_servicii()
