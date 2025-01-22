class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None


    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo


    def eliminar(self):
        if self.tope is None:
            print("La pila está vacía.")
            return
        eliminado = self.tope.dato
        self.tope = self.tope.siguiente
        print(f"Elemento eliminado: {eliminado}")


    def mostrar(self):
        actual = self.tope
        if actual is None:
            print("La pila está vacía.")
            return
        while actual:
            print(actual.dato, end=" -> " if actual.siguiente else "")
            actual = actual.siguiente
        print()


pila = Pila()
pila.insertar(10)
pila.insertar(20)
pila.insertar(30)
print("Pila después de insertar elementos:")
pila.mostrar()

pila.eliminar()
print("Pila después de eliminar el tope:")
pila.mostrar()

pila.eliminar()
pila.eliminar()
print("Pila después de vaciarla:")
pila.mostrar()
