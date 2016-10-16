# Regla logica: Si X -> Y#
class Regla:
    def __init__(self, premisas, concluciones):
        self.premisas = premisas
        self.concluciones = concluciones

    def getPremisas(self):
        return self.premisas

    def getConcluciones(self):
        return self.concluciones

    def checkPremisa(self, premisa):
        return premisa in self.premisas

    def checkConclucion(self, conclucion):
        return conclucion in self.concluciones
