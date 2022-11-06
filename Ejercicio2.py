class nave():
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros

    def __str__(self):
        if self.nombre == "Estrella de la muerte":
            return "La {} tiene un diámetro de {} m, su tripulación es de {} miembros y el número de pasajeros es de {} entre personas y droides.".format(self.nombre, self.largo, self.tripulacion, self.pasajeros)
        else:
            return "El {} tiene un largo de {} m, una tripulación de {} miembros y el número de pasajeros es de {} entre personas y droides.".format(self.nombre, self.largo, self.tripulacion, self.pasajeros)

Ala_x = nave("Ala-X", 20, 4, 1)
Ala_y = nave("Ala-Y", 14, 4, 1)
At_At = nave("AT-AT", 15, 4, 1)
Caza_Tie = nave("Caza-Tie", 14, 2, 0)
Crucero = nave("Crucero estelar", 8000, 850, 1100)
Destructor = nave("Destructor", 1150, 1000, 1400)
Estrella_de_la_muerte = nave("Estrella de la muerte", 160000, 165000, 200000)
Halcon_Milenario = nave("Halcón Milenario", 35, 2, 6)

naves = [Ala_x, Ala_y, At_At, Caza_Tie, Crucero, Destructor, Estrella_de_la_muerte, Halcon_Milenario]

# 1
naves_ordenadas = sorted(naves, key=lambda self: self.nombre)
naves_pasajeros = sorted(naves, key=lambda self: self.pasajeros, reverse=True)

print("Las naves ordenadas por nombre son:")
for i in naves_ordenadas:
    print(i.nombre)

print("Las naves ordenadas por tamaño de manera descendente son:")
for i in naves_ordenadas:
    print(i.nombre)

# 2
print(Halcon_Milenario)
print(Estrella_de_la_muerte)

# 3 
def pasajeros_5(naves_pasajeros):
    print("Las 5 naves con mayor número de pasajeros son:")
    for i in range (5):
        if i < len(naves_pasajeros):
            print(naves_pasajeros[i].nombre)

pasajeros_5(naves_pasajeros)

# 4
naves_tripulacion = sorted(naves, key=lambda self: self.tripulacion, reverse=True)

def mayor_tripulacion(naves_tripulacion):
    return print("La nave con mayor tripulación es la", naves_tripulacion[0].nombre)

mayor_tripulacion(naves_tripulacion)

# 5
def naves_AT(naves):
    print("Las naves que empiezan con AT son:")
    for i in naves:
        if i.nombre[:2] == "AT":
            print(i.nombre)

naves_AT(naves)

# 6
def naves_6_pasajeros(naves):
    print("Las naves que pueden llevar a 6 o más son:")
    for i in naves:
        if i.pasajeros >= 6:
            print(i.nombre)

naves_6_pasajeros(naves)

# 7
naves_largo = sorted(naves, key=lambda self: self.largo)
def naves_tamanio(naves_largo):
    print("La nave de mayor tamaño es la", naves_largo[len(naves_largo)-1], "y la nave de menor tamaño es el", naves_largo[0])

naves_tamanio(naves_largo)
