classs BoundedPriorityQueue:
  def __init__(self, niveles):
    self.__data = [Queue() for x in range (niveles)]
    self.__size = 0


  def is__empty(self):
      return self.__size=0

  def length (self):
      return self.__size

  def enqueue(self, prioridad,elem) :
      self.__data[prioridad] enqueue (elem) 
      if prioridad < self.length() and prioridad >=0:
          self.__data[prioridad].enqueue(elem)

    def dequeue(self):
        if not self.is__empty #Por si la cola esta vacìa 
        for nivel in self.__data: #Regresara un FALSE, 
            #cadena=cadena+"I"+str(elem) 
            #cadena=cadena+"I"
            #return cadena
         if not nivel.is_empty(): #¿Hay algo que sacar?
             return nivel.dequeue() #Preguntar ¿La cola esta vacìa?
         

    def to_string(self):
        for nivel in range(self.length())
        print(f"Nivel {nivel} --> {self.__data[nivel].to_string() }")
