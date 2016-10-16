from Regla import Regla
from generador import Generador

def EncadenamientoHaciaAtras(parametros):
    reglas, baseConocimiento, conclucion = parametros
    while (not comp(conclucion, baseConocimiento)):
        skip = False
        for regla in reglas:
            if comp(conclucion, regla.getConcluciones()):
                if comp(regla.getPremisas(), baseConocimiento):
                    print "Se aplico Regla:", (regla.getPremisas(), regla.getConcluciones())
                    baseConocimiento.extend(regla.getConcluciones())
                    skip = True
                else:
                    for premisa in regla.getPremisas():
                        if premisa not in baseConocimiento:
                            EncadenamientoHaciaAtras([reglas, baseConocimiento, [premisa]])
            if skip:
                break
    print baseConocimiento
    return

def EncadenamientoHaciaAdelante(parametros):
    reglas, baseConocimiento, conclucion = parametros
    while (not comp(conclucion, baseConocimiento)):
        skip = False
        for regla in reglas:
            if comp(regla.getPremisas(), baseConocimiento) and not comp(regla.getConcluciones(), baseConocimiento):
                print "Se aplico Regla:", (regla.getPremisas(), regla.getConcluciones())
                baseConocimiento = baseConocimiento + regla.getConcluciones()
                skip = True
            if skip:
                break
    return

# Se fija si la Lista 1 esta dentro de la Lista2#
def comp(list1, list2):
    for val in list1:
        if val not in list2:
            return False
    return True







if __name__ == "__main__":
    generador = Generador()
    print "Encadenamiento hacia Adelante"
    EncadenamientoHaciaAdelante([generador.GenerarReglas2(), generador.GenerarBC2(), generador.GenerarConclucion2()])
    print "Encadenamiento hacia Atras"
    EncadenamientoHaciaAtras([generador.GenerarReglas2(), generador.GenerarBC2(), generador.GenerarConclucion2()])