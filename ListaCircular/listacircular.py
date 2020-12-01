from nodo import Nodo

class CircularList():
    def __init__(self):
        self.primero=None
        self.ultimo=None

def Vacia(self):
    return self.primero==None #Aparecera el Nodo 

def AgregarInicio(self,dato):
    if self.Vacia(): #Solo hay un elemento 
        self.primero=self.ultimo=Nodo(dato)
        self.ultimo.siguiente=self.primero
    else:  #En caso de tener màs elementos, crear un NODO AUXILIAR
        aux=Nodo(dato)
        aux.siguiente=self.primero
        self.primero=aux
        self.ultimo.siguiente = self.primero 

        #aux= self.ultimo
        #self.ultimo=aux.siguiente=Nodo(dato) 

def AgregarFinal(self,dato):
    if self.Vacia():
        self.primero=self.ultimo=Nodo(dato)
        self.ultimo.siguiente=self.primeroe
    else:
        aux= self.ultimo
        self.ultimo = aux.siguiente= Nodo(dato)
        self.primero.siguiente=self.primero  

def Recorrer (self): #Este mètodo, muestra la lista
    aux=self.primero
    while aux:
        print(aux.dato)
        aux = aux.siguiente
     
