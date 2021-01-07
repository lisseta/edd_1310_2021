from colas import Queue

q1= Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_String())

print ("PRUEBA 2 QUEUE")
c1={"id":1 "nombre":"Lizeth", "balace":20.5} #COLA, estructura de datos lineal o de dos dimensiones 
c2={"id":2 "nombre":"Lizeth", "balace":3456.5.5}
c3={"id":3 "nombre":"Lizeth", "balace":10000.0}

atencion=Queue()
atencion.enqueue(c1)
atencion.enqueue(c1)
atencion.enqueue(c1)
print(atencion.to_string())
siguiente=atencion.dequeue()
print(f"Bienvenido Sr. {siguiente['nombre']}, ¿EN QUÈ PODEMOS SERVIRLE HOY")
print(atencion.to_string())

print("PRUEBAS DE COLAS CON PRIORIDAD ACOTADA")

maestres={"prioridad":4, "descripcion":"Maestre", "personas":["Juan P", "Diego H"]}
niños={"prioridad":2, "descripcion":"Niños", "personas":["Santi H", "Angel H"]}
mecanicos={"prioridad":4, "descripcion":"Mecanicos", "personas":["Diana T", "Marìa Z"]}

cpa=BoundedPriorityQueue(7)
cpa.enqueue(maestres)