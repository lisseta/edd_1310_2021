class PriorityQueue:
  def __init__(self):
    self.__datos=list()
  def is_empty(self):
    return len(self.__datos)==0
  def length (self):
    return len(self.__datos)
  def enqueue (self, prioridad, elem):
    if prioridad>=0:
        a=0
        while a<len(self.__datos) and self.__datos[a]['prioridad']<=prioridad:
          a+=1
        self.__datos.insert(x,elem)
  def dequeue (self):
    if self.is_empty():
      print('cola vacia')
    else:
      return self.__datos.pop(0)
  def to_String(self):
    for x in range(len(self.__datos)):
      print(f" {self.__datos[x]['prioridad']}  {self.__datos[x]['descripcion']}, {self.__datos[x]['personas']} ")
