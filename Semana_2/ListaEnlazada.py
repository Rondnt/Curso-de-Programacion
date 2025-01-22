#lista enlazada

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente
        if actual.siguiente is None:
            print(f"El dato {dato} no se encontró en la lista.")
        else:
            actual.siguiente = actual.siguiente.siguiente

    def mostrar(self):
      actual = self.cabeza
      if actual is None:
          print("La lista está vacía.")
          return
      while actual:
          print(actual.dato, end=" -> " if actual.siguiente else "")
          actual = actual.siguiente
      print()


lista = ListaEnlazada()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
print("Lista después de insertar elementos:")
lista.mostrar()

lista.eliminar(20)
print("Lista después de eliminar 20:")
lista.mostrar()