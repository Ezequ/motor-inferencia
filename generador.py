from Regla import Regla
class Generador:
    def GenerarReglas(self):
        rules = []
        rules.append(Regla(['D', 'E'], ['F']))
        rules.append(Regla(['C', 'B'], ['E']))
        rules.append(Regla(['A', 'C'], ['D']))
        rules.append(Regla(['A', 'B'], ['C']))
        return rules


    def GenerarBC(self):
        return ['A', 'B']


    def GenerarConclucion(self):
        return ['F']


    def GenerarReglas2(self):
        reglas = []
        reglas.append(Regla(['Comprar uno nuevo', 'Llevar a reparar'], ['Ir al shoping']))
        reglas.append(Regla(['No responde', 'Placa quemada'], ['Comprar uno nuevo']))
        reglas.append(Regla(['No arranca', 'Placa quemada'], ['Llevar a reparar']))
        reglas.append(Regla(['No arranca', 'No responde'], ['Placa quemada']))
        return reglas


    def GenerarBC2(self):
        return ['No arranca', 'No responde']


    def GenerarConclucion2(self):
        return ['Ir al shoping']