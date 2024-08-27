from Direccion import Direccion
from Persona import Persona
from Telefono import Telefono

class Contacto(Direccion, Persona, Telefono ):
    def __init__(self):
        self.__Email = ""

    def GetEmail(self):
        return self.__Email

    def SetEmail(self, email):
        self.__Email = email

    def MostrarContacto(self):
        print("----Contacto----")
        print("Nombre: " + self.GetNombre())
        print("Apellidos: " + self.GetApellidos())
        print("Fecha de Nacimiento: " + self.GetFechaNacimiento())
        print("Teléfono fijo: " + self.GetTelefonoFijo())
        print("Teléfono móvil: " + self.GetTelefonoMovil())
        print("Teléfono del trabajo: " + self.GetTelefonoTrabajo())
        print("Calle: " + self.GetCalle())
        print("Piso: " + self.GetPiso())
        print("Ciudad: " + self.GetCiudad())
        print("Código Postal: " + self.GetCodigoPostal())
        print("Email: " + self.GetEmail())
        print("----------------")

