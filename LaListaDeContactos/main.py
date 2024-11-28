__author__ = "Gabriel Esteban Paz Guerrero"
__license__ = "GPL"
__version__ = "1.0.3"
__email__ = "gabriel.pazg@campusucc.edu.co"

from src.Contactoo import Contacto
from src.ListaContactos import ListaDeContactos

def main():
    lista_contactos = ListaDeContactos()

    while True:
        print("\n--- Lista de Contactos ---")
        print("1. Agregar un nuevo contacto")
        print("2. Eliminar un contacto")
        print("3. Ver la información detallada de un contacto")
        print("4. Modificar la información de un contacto")
        print("5. Mostrar la lista completa de contactos")
        print("6. Buscar contactos por palabras claves")
        print("7. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1": 
           
            __nombre = input("Nombre: ").strip()
            __apellido = input("Apellido: ").strip()

            if not __nombre or not __apellido:
                print("Error: El nombre y apellido son obligatorios.")
                continue

            __direccion = input("Dirección: ").strip()
            __email = input("Correo electrónico: ").strip()
            __telefonos = input("Números telefónicos (separados por coma): ").split(",")
            __palabrasClave = input("Palabras clave (separadas por coma): ").split(",")

            contacto = Contacto(__nombre, __apellido, __direccion, __email, __telefonos, __palabrasClave)
            try:
                mensaje = lista_contactos.agregarContacto(contacto)
                print(mensaje)
            except ValueError as e:
                print(e)

        elif choice == "2":
           
            __nombre = input("Nombre: ").strip()
            __apellido = input("Apellido: ").strip()
            if lista_contactos.eliminarContacto(__nombre, __apellido):
                print(f"Contacto {__nombre} {__apellido} eliminado correctamente.")
            else:
                print(f"Contacto {__nombre} {__apellido} no encontrado.")

        elif choice == "3":
           
            __nombre = input("Nombre: ").strip()
            __apellido = input("Apellido: ").strip()
            lista_contactos.verContacto(__nombre, __apellido)

        elif choice == "4":
    
            __nombre = input("Nombre del contacto a modificar: ").strip()
            __apellido = input("Apellido del contacto a modificar: ").strip()

            nuevo_nombre = input("Nuevo nombre (deje en blanco para no cambiar): ").strip() or None
            nuevo_apellido = input("Nuevo apellido (deje en blanco para no cambiar): ").strip() or None
            __direccion = input("Nueva dirección (deje en blanco para no cambiar): ").strip() or None
            __email = input("Nuevo correo electrónico (deje en blanco para no cambiar): ").strip() or None
            __telefonos = input("Nuevos números telefónicos (separados por coma, deje en blanco para no cambiar): ")
            __telefonos = __telefonos.split(",") if __telefonos else None
            __palabrasClave = input("Nuevas palabras clave (separadas por coma, deje en blanco para no cambiar): ")
            __palabrasClave = __palabrasClave.split(",") if __palabrasClave else None

            try:
                lista_contactos.ModificarContacto(
                    __nombre, __apellido, nuevo_nombre=nuevo_nombre, nuevo_apellido=nuevo_apellido,
                    direccion=__direccion, email=__email, telefonos=__telefonos, palabrasClave=__palabrasClave
                )
            except ValueError as e:
                print(e)

        elif choice == "5":
            
            lista_contactos.listaContactos()

        elif choice == "6":
        
            palabra_clave = input("Ingrese una palabra clave: ").strip()
            resultados = lista_contactos.buscarPorPalabraClave(palabra_clave)
            if resultados:
                print("\nResultados de la búsqueda:")
                for contacto in resultados:
                    print(contacto)
            else:
                print(f"No se encontraron contactos con la palabra clave '{palabra_clave}'.")

        elif choice == "7":
            print("¡Gracias por usar la Lista de Contactos!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()