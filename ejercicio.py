class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre        # Atributo público
        self.__edad = edad          # Atributo privado (encapsulado)

    # Getter: permite leer la edad
    def obtener_edad(self):
        return self.__edad

    # Setter: permite cambiar la edad de forma segura
    def cambiar_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

# Uso de la clase
p = Persona("Ana", 20)

print(p.nombre)             # Acceso directo (público)
print(p.obtener_edad())     # Acceso al atributo encapsulado

p.cambiar_edad(25)          # Cambiar valor solo mediante método
print(p.obtener_edad())
