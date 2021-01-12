maestre = { "prioridad" : 4 , "descripcion" : "Maestre" , "personas" : "" }
Ni ñ o = { "prioridad" : 2 , "descripcion" : "niño" , "personas" : "" }
mecanico = { "prioridad" : 4 , "descripcion" : "mecanico" , "personas" : "" }
Hombre = { "prioridad" : 3 , "descripcion" : "hombre" , "personas" : "" }
Vigia = { "prioridad" : 4 , "descripcion" : "Vigia" , "personas" : "" }
Capitán = { "prioridad" : 5 , "descripcion" : "Capitán" , "personas" : "" }
Timonel = { "prioridad" : 4 , "descripcion" : "Timonel" , "personas" : "" }
Mujer = { "prioridad" : 3 , "descripcion" : "mujer" , "personas" : "" }
3 edad = { "prioridad" : 2 , "descripcion" : "abuelo" , "personas" : "" }
Ni ñ a = { "prioridad" : 1 , "descripcion" : "Niña" , "personas" : "" }

cms = PriorityQueue ()
cms . enqueue ( maestre [ "prioridad" ], maestre )
cms . poner en cola ( Ni ñ o [ "prioridad" ], Ni ñ o )
cms . poner en cola ( mecanico [ "prioridad" ], mecanico )
cms . poner en cola ( Hombre [ "prioridad" ], Hombre )
cms . poner en cola ( Vigia [ "prioridad" ], Vigia )
cms . poner en cola ( Capitán [ "prioridad" ], Capitán )
cms . poner en cola ( Timonel [ "prioridad" ], Timonel )
cms . enqueue ( Mujer [ "prioridad" ], Mujer )
cms . poner en cola ( Viejo [ "prioridad" ], Viejo )
cms . poner en cola ( Ni ñ a [ "prioridad" ], Ni ñ a )


for  x  in  range ( cms . longitud ()):
  bote = cms . dequeue ()
  print ( f "el pasajero: { bote [ 'personas' ] } estan a bordo" )