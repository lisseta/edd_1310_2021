print(f"Sè harà un crucero, donde, la prioridad de los pasajeros esta dada por un nùmero")
class BoundedPriorityQueue:
  def __init__(self,niveles):
    self.data=[Queue() for x in range(niveles)]
    self.size=0 

  def length (self): #No.Elementos con prioridad acotada
      return self.__size

print(f"Los pasajeros son los siguientes")
cola=["niñas", "niños", "mujeres", "hombres", "maestre", "mecanico", "vigia","timonel", "capitan",]
cola.append("Capitan")
print(cola)

#Sacar elementos del inicio
print(f"El orden es el siguiente")
p= cola.pop(0)
print(f"Los primeros pasajeros son {p}")

p= cola.pop(0)
print(f"Los segundos pasajeros son {p}")

p= cola.pop(0)
print(f"Los terceros pasajeros son {p}")

print(f"La fila ha terminado, todos estan a bordo")

def enqueue(self, prioridad,elem) :
      #self.__data[prioridad] enqueue (elem) 
      if prioridad < self.length() and prioridad >=0:
          self.__data[prioridad].enqueue(elem) 
def  to_String ( self ):
    para  x  en el  rango ( len ( self . __datos )):
      print ( f " { self . __datos [ x ] [ 'prioridad' ] }   { self . __datos [ x ] [ 'descripcion' ] } , { self . __datos [ x ] [ 'personas' ] } " )
