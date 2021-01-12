class PriorityQueue:
  def __init__(self):
    self.__data= list() #[]

  def is__empty(self):
    return len(self.__data)== 0

  def length(self):
    return len(self.__data)

  def enqueue(self,elem, prioridad): 
    if prioridad>=0:
      n=0
      while n<len(self.__data)and self.__data[n]['La prioridad es']<=prioridad:
        n+1
          #Ingresa un elemento al final 
    self.__data.append(elem) #Insertar 

  def dequeue(self): 
    if self.is__empty():
      print("Ya está vacía")#Preguntar si ya esta vacía
    #return self.__data.pop(0) #Para agregar
    else:
      return self.__datos.pop(0)


  def to_string(self): #¿Todo esta OK? Estado actual 
    cadena=""  
    for n in range (len(self.__data)):#in self.__data:
      print(f"La prioridad "{self.__data[n]['prioridad']} {self.data[n]})
      