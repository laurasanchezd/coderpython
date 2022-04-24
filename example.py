vor= "all"

vor2= "you"

var3="need"

var4="is"

var5="love"

print(vor,vor2,var3,var4,var5)

class Persona:

    def __init__(self, nombre,apellido,perro):

      self.nombre= nombre
      self.apellido= apellido
      self.perro= perro

    def __str__(self):
     return "mi nombre es :" +self.nombre 
persona1= Persona("lau", "sanchez" ,"sd")
print(persona1.nombre , persona1.apellido)