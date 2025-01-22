#Cola
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None


    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None:
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo


    def eliminar(self):
        if self.frente is None:
            print("La cola está vacía.")
            return
        eliminado = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print(f"Elemento eliminado: {eliminado}")


    def mostrar(self):
        actual = self.frente
        if actual is None:
            print("La cola está vacía.")
            return
        while actual:
            print(actual.dato, end=" -> " if actual.siguiente else "")
            actual = actual.siguiente
        print()


cola = Cola()
cola.insertar(10)
cola.insertar(20)
cola.insertar(30)
print("Cola después de insertar elementos:")
cola.mostrar()

cola.eliminar()
print("Cola después de eliminar el frente:")
cola.mostrar()

cola.eliminar()
cola.eliminar()
print("Cola después de vaciarla:")
cola.mostrar()
