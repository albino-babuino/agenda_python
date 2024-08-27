from Contacto import Contacto

class Agenda:
    def __init__(self, path):
        self.__Path = path #Es la ruta en la que se encuentra el fichero para almacenar los contactos
        self.__ListaContactos = [] #Aquí se almacenarán los contactos

    def CargarContactos(self):
        # Carga la lista de contactos leyendo desde el archivo
        try:
            fichero = open(self.__Path, "r") #Abrir archivo que se ubica en el path especificado
        except FileNotFoundError:
            print("No existe el fichero de la agenda") #Si no existe el archivo mostramos un error
        else:
            contactos = fichero.readlines() #Leemos todas las líneas del archivo y las guardamos en contactos
            fichero.close() #Cerramos el fichero
            if(len(contactos) > 0): #Si existen contactos
                for contacto in contactos: #Los recorremos todos obteniendo la información de cada línea
                    datos = contacto.split("#") #Separamos cada dato de la línea (contacto)
                    if(len(datos)==11): #Cada contacto tiene 11 atributos
                        nuevocontacto = Contacto() #Instanciamos un objeto de tipo Contacto
                        #Especificamos los atributos
                        nuevocontacto.SetNombre(datos[0])
                        nuevocontacto.SetApellidos(datos[1])
                        nuevocontacto.SetFechaNacimiento(datos[2])
                        nuevocontacto.SetTelefonoMovil(datos[3])
                        nuevocontacto.SetTelefonoFijo(datos[4])
                        nuevocontacto.SetTelefonoTrabajo(datos[5])
                        nuevocontacto.SetCalle(datos[6])
                        nuevocontacto.SetPiso(datos[7])
                        nuevocontacto.SetCiudad(datos[8])
                        nuevocontacto.SetCodigoPostal(datos[9])
                        nuevocontacto.SetEmail(datos[10])
                        self.__ListaContactos = self.__ListaContactos + [nuevocontacto] #Agregamos a la lista de contactos cada uno de los contactos
                        print("INFO: Se han cargado un total de ", len(self.__ListaContactos), " contactos") #Mostramos mensaje de éxito

    def CrearNuevoContacto(self, nuevocontacto):
        # Almacena en la lista de contactos un nuevo contacto
        self.__ListaContactos.append(nuevocontacto) #Otra forma self.__ListaContactos = self.ListaContactos + [nuevocontacto]

    def GuardarContactos(self):
        # Grabará en el fichero la lista de contactos que tiene almacenado el atributo ListaContactos
        try:
            fichero = open(self.__Path, "w") #Abrimos el archivo con la opción de sobreescritura
        except:
            print("ERROR: No se puede guardar") #Si no se puede, mandamos un mensaje de error
        else:
            for contacto in self.__ListaContactos: #Recorremos ListaContactos guardando cada item del contacto acabando con el separador '#'
                texto = contacto.GetNombre() + "#"
                texto += contacto.GetApellidos() + "#"
                texto += contacto.GetFechaNacimiento() + "#"
                texto += contacto.GetTelefonoMovil() + "#"
                texto += contacto.GetTelefonoFijo() + "#"
                texto += contacto.GetTelefonoTrabajo() + "#"
                texto += contacto.GetCalle() + "#"
                texto += contacto.GetPiso() + "#"
                texto += contacto.GetCiudad() + "#"
                texto += contacto.GetCodigoPostal() + "#"
                texto += contacto.GetEmail() + "\n"
                fichero.write(texto) #Escribimos la información del contacto en el archivo

    def MostrarAgenda(self):
        # Mostrará por pantalla el contenido del atributo ListaContactos
        print("####### AGENDA #######")
        print("Número de contactos:", len(self.__ListaContactos))
        for contacto in self.__ListaContactos:
            contacto.MostrarContacto()
        print("######################")

    def BuscarContactoPorNombre(self, nombre):
        # Busca un contacto en ListaContactos por su nombre y lo devuelve
        listaencontrados = []
        for contacto in self.__ListaContactos:
            if contacto.GetNombre() == nombre:
                listaencontrados.append(contacto)
        return listaencontrados

    def BuscarContactoPorTelefono(self, telefono):
        # Busca un contacto en ListaContactos por su teléfono y lo devuelve
        listaencontrados = []
        for contacto in self.__ListaContactos:
            if contacto.GetTelefonoMovil() == telefono or contacto.GetTelefonoFijo() == telefono or contacto.GetTelefonoTrabajo() == telefono:
                listaencontrados.append(contacto)
        return listaencontrados

    def BorrarContactoPorNombre(self, nombre):
        # Busca un contacto en ListaContactos por su nombre y lo borra
        listafinal = []
        for contacto in self.__ListaContactos:
            if contacto.GetNombre() != nombre:
                listafinal.append(contacto)
        print("Se han eliminado ", len(self.__ListaContactos) - len(listafinal), " contactos")
        self.__ListaContactos = listafinal
        #Para eliminar el contacto del archivo txt hay que marcar la opción "5) Guardar cambios"

    def BorrarContactoPorTelefono(self, telefono):
        # Busca un contacto en ListaContactos por su teléfono y lo borra
        listafinal = []
        for contacto in self.__ListaContactos:
            if contacto.GetTelefonoMovil() != telefono and contacto.GetTelefonoFijo() != telefono and contacto.GetTelefonoTrabajo() != telefono:
                listafinal.append(contacto)
        print("Se han eliminado ", len(self.__ListaContactos) - len(listafinal), " contactos")
        self.__ListaContactos = listafinal