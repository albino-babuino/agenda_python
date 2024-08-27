class Telefono:
    def __init__(self):
        self.__TelefonoFijo = ""
        self.__TelefonoMovil = ""
        self.__TelefonoTrabajo = ""

    def GetTelefonoFijo(self):
        return self.__TelefonoFijo
    def GetTelefonoMovil(self):
        return self.__TelefonoMovil
    def GetTelefonoTrabajo(self):
        return self.__TelefonoTrabajo

    def SetTelefonoFijo(self, fijo):
        self.__TelefonoFijo = fijo
    def SetTelefonoMovil(self, movil):
        self.__TelefonoMovil = movil
    def SetTelefonoTrabajo(self, trabajo):
        self.__TelefonoTrabajo = trabajo

