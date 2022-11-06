class nodo(object):
    info,sig = None,None

class valores(object):
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino
    
class polinomio(valores):
    def __init__(self):
        self.grado = -1
        self.termino_mayor = None

    def agregar(self,termino,valor):
        aux = nodo()
        dato = valores(valor, termino)
        aux.info = dato
        if termino > self.grado:
            aux.sig = self.termino_mayor
            self.termino_mayor = aux
            self.grado = termino
        else:
            nuevo_termino = self.termino_mayor
            while((nuevo_termino is not None)):
                nuevo_termino = nuevo_termino.sig
            aux.sig = nuevo_termino.sig
            nuevo_termino = aux
    
    def borrar(self, termino):
        aux = self.termino_mayor
        if (self.grado == termino):
            self.termino_mayor = aux.sig
            del aux
        else:
            while aux.sig is not None:
                if aux.sig.info.termino == termino:
                    aux.sig = aux.sig.sig
                    del aux.sig
                    return
                aux = aux.sig

    def objeto(self, termino):
        aux = self.termino_mayor
        while((aux is not None) and (aux.info.term > termino)):
            aux = aux.sig
        if ((aux is not None) and (aux.info.term == termino)):
            return aux.info.val
        else:
            return 0
    
    def imprimir(self):
        nuevo_termino = self.termino_mayor
        while(nuevo_termino is not None):
            nuevo_termino = nuevo_termino.sig
            return "{}x{}".format(nuevo_termino.info.val, nuevo_termino.info.term)


x = polinomio()
y = x.agregar(1,2)
z = x.agregar(3,4)

def suma(y,z):
    return print(y+z)

def resta(y,z):
    return print(y-z)

def multiplicacion(y,z):
    return print(y*z)

def division(y,z):
    return print(y/z)

suma(y,z)
resta(y,z)
multiplicacion(y,z)
division(y,z)