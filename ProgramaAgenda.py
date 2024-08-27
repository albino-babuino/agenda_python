from Agenda import Agenda
from Contacto import Contacto

def ObtenerOpcion(texto):
    #ObtenerOpcion: leerá la opción elegida del menú por parte del usuario
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print("ERROR: Tienes que introducir un número")
        else:
            leido = True
            return numero

def MostrarMenu():
    #MostrarMenu: mostrará el menú de opciones por pantalla
    print('''
    0) Cargar contactos
    1) Mostrar contactos
    2) Buscar contactos
    3) Crear contacto nuevo
    4) Borrar contacto
    5) Guardar cambios
    6) Salir
    ''')

def BuscarContactos(agenda):
    print('''Buscar contactos:
    1) Nombre
    2) Teléfono
    3) Volver
    ''')
    finbuscar = False
    while not finbuscar:
        opcbuscar = ObtenerOpcion("Opción:")
        if opcbuscar == 1:
            encontrados = agenda.BuscarContactoPorNombre(input("Introduce el nombre a buscar: "))
            if len(encontrados) > 0:
                print("#### CONTACTOS ENCONTRADOS ####")
                for item in encontrados:
                    item.MostrarContacto()
                print("###############################")
            else:
                print("INFO: No se han encontrado contactos.")
            finbuscar = True
        elif opcbuscar == 2:
            encontrados = agenda.BuscarContactoPorTelefono(input("Introduce el teléfono a buscar: "))
            if len(encontrados) > 0:
                print("#### CONTACTOS ENCONTRADOS ####")
                for item in encontrados:
                    item.MostrarContacto()
                print("###############################")
            else:
                print("INFO: No se han encontrado contactos.")
            finbuscar = True
        elif opcbuscar == 3:
            finbuscar = True

#BuscarContacto: realizará el proceso completo de búsqueda a excepción de la propia búsqueda en la lista, que realizará la propia clase Agenda

#CrearContacto: realizará el proceso completo de creación de un contacto a excepción del propio almacenamiento en la agenda que lo realizará la propia clase de Agenda
def ProcesoCrearContacto(agenda):
    nuevocontacto = Contacto()
    nuevocontacto.SetNombre(input("Introduce el nombre del contacto: "))
    nuevocontacto.SetApellidos(input("Introduce los apellidos del contacto: "))
    nuevocontacto.SetFechaNacimiento(input("Introduce la fecha de nacimiento del contacto: "))
    nuevocontacto.SetTelefonoMovil(input("Introduce el teléfono móvil del contacto: "))
    nuevocontacto.SetTelefonoFijo(input("Introduce el teléfono fijo del contacto: "))
    nuevocontacto.SetTelefonoTrabajo(input("Introduce el teléfono del trabajo del contacto: "))
    nuevocontacto.SetCalle(input("Introduce la calle de la dirección del contacto: "))
    nuevocontacto.SetPiso(input("Introduce el piso de la dirección del contacto: "))
    nuevocontacto.SetCiudad(input("Introduce la ciudad de la dirección del contacto: "))
    nuevocontacto.SetCodigoPostal(input("Introduce el código postal de la dirección del contacto: "))
    nuevocontacto.SetEmail(input("Introduce el email del contacto: "))
    agenda.CrearNuevoContacto(nuevocontacto)

#BorrarContacto: realizará el proceso de borrado de un contacto a excepión del propio borrado de la agenda que lo realizará la propia clase Agenda
def BorrarContacto(agenda):
    print('''Buscar contacto a borrar por:
    1) Nombre
    2) Teléfono
    3) Volver
    ''')
    finbuscar = False
    while not finbuscar:
        opcbuscar = ObtenerOpcion("Opción: ")
        if opcbuscar == 1:
            agenda.BorrarContactoPorNombre(input("Introduce el nombre del contacto a borrar: "))
            finbuscar = True
        elif opcbuscar == 2:
            agenda.BorrarContactoPorTelefono(input("Introcue el teléfono del contacto a borrar: "))
            finbuscar = True
        elif opcbuscar == 3:
            finbuscar = True

# Main: Función principal de la aplicación que contiene el flujo del programa
def Main():
    agenda = Agenda("agenda.txt")
    agenda.CargarContactos()
    fin = False
    while not fin:
        MostrarMenu()
        opc = ObtenerOpcion("Opción: ")
        if(opc == 0):
            agenda.CargarContactos()
        if(opc == 1):
            agenda.MostrarAgenda()
        elif(opc == 2):
            BuscarContactos(agenda)
        elif(opc == 3):
            ProcesoCrearContacto(agenda)
        elif(opc == 4):
            BorrarContacto(agenda)
        elif(opc == 5):
            agenda.GuardarContactos()
        elif(opc == 6):
            fin = 1

Main()