class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo_actual, dato):
        if dato < nodo_actual.dato:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(dato)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, dato)
        elif dato > nodo_actual.dato:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(dato)
            else:
                self._insertar_recursivo(nodo_actual.derecho, dato)
        else:
            print(f"El dato {dato} ya existe en el árbol.")

    def eliminar(self, dato):
        self.raiz = self._eliminar_recursivo(self.raiz, dato)

    def _eliminar_recursivo(self, nodo_actual, dato):
        if nodo_actual is None:
            print(f"El dato {dato} no se encontró en el árbol.")
            return nodo_actual

        if dato < nodo_actual.dato:
            nodo_actual.izquierdo = self._eliminar_recursivo(nodo_actual.izquierdo, dato)
        elif dato > nodo_actual.dato:
            nodo_actual.derecho = self._eliminar_recursivo(nodo_actual.derecho, dato)
        else:
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            elif nodo_actual.derecho is None:
                return nodo_actual.izquierdo

            nodo_actual.dato = self._minimo_valor(nodo_actual.derecho)
            nodo_actual.derecho = self._eliminar_recursivo(nodo_actual.derecho, nodo_actual.dato)

        return nodo_actual

    def _minimo_valor(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual.dato

    def mostrar(self, tipo_recorrido="inorden"):
        if tipo_recorrido == "inorden":
            print("Recorrido Inorden:")
            self._inorden(self.raiz)
        elif tipo_recorrido == "preorden":
            print("Recorrido Preorden:")
            self._preorden(self.raiz)
        elif tipo_recorrido == "postorden":
            print("Recorrido Postorden:")
            self._postorden(self.raiz)
        print() 

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izquierdo)
            print(nodo.dato, end=" ")
            self._inorden(nodo.derecho)

    def _preorden(self, nodo):
        if nodo:
            print(nodo.dato, end=" ")
            self._preorden(nodo.izquierdo)
            self._preorden(nodo.derecho)

    def _postorden(self, nodo):
        if nodo:
            self._postorden(nodo.izquierdo)
            self._postorden(nodo.derecho)
            print(nodo.dato, end=" ")

arbol = ArbolBinario()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Árbol inicial:")
arbol.mostrar("inorden")

print("\nEliminar 20:")
arbol.eliminar(20)
arbol.mostrar("inorden")

print("\nEliminar 30:")
arbol.eliminar(30)
arbol.mostrar("inorden")

print("\nEliminar 50 (raíz):")
arbol.eliminar(50)
arbol.mostrar("inorden")