maestre={"prioridad":4,"descripcion":"Maestre","personas":" "}
Niño={"prioridad":2,"descripcion":"niño","personas":" "}
mecanico={"prioridad":4,"descripcion":"mecanico","personas":" "}
Hombre={"prioridad":3,"descripcion":"hombre","personas":" "}
Vigia={"prioridad":4,"descripcion":"Vigia","personas":" "}
Capitan={"prioridad":5,"descripcion":"Capitan","personas":" "}
Timonel={"prioridad":4,"descripcion":"Timonel","personas":" "}
Mujer={"prioridad":3,"descripcion":"mujer","personas":" "}
3edad={"prioridad":2,"descripcion":"abuelo","personas":" "}
Niña={"prioridad":1,"descripcion":"Niña","personas":" "}

cms=PriorityQueue()
cms.enqueue(maestre["prioridad"],maestre)
cms.enqueue(Niño["prioridad"],Niño)
cms.enqueue(mecanico["prioridad"],mecanico)
cms.enqueue(Hombre["prioridad"],Hombre)
cms.enqueue(Vigia["prioridad"],Vigia)
cms.enqueue(Capitan["prioridad"],Capitan)
cms.enqueue(Timonel["prioridad"],Timonel)
cms.enqueue(Mujer["prioridad"],Mujer)
cms.enqueue(Viejo["prioridad"],Viejo)
cms.enqueue(Niña["prioridad"],Niña)


for x in range(cms.length()):
  bote=cms.dequeue()
  print(f"el pasajero: {bote['personas']} ha subido al bote")
