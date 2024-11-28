__author__ = "Gabriel Esteban Paz Guerrero"
__license__ = "GPL"
__version__ = "1.0.3"
__email__ = "gabriel.pazg@campusucc.edu.co"

class ListaDeContactos:
    def __init__(self):
        self.contactos = {}

    def generarClave(self, nombre, apellido):
        return f"{nombre.strip().lower()}_{apellido.strip().lower()}"

    def agregarContacto(self, contacto):
        clave = self.generarClave(contacto.nombre, contacto.apellido)
        if clave in self.contactos:
            raise ValueError("El contacto ya existe.")
        self.contactos[clave] = contacto
        return f"{contacto.nombre} {contacto.apellido} se añadió exitosamente a tu lista de contactos"

    def eliminarContacto(self, nombre, apellido):
        clave = self.generarClave(nombre, apellido)
        if clave not in self.contactos:
            return False  
        del self.contactos[clave]
        return True

    def listaContactos(self):
        if not self.contactos:
            print("No hay contactos en la lista.")
        else:
            for contacto in self.contactos.values():
                print(contacto)
                print("-" * 40)

    def verContacto(self, nombre, apellido):
        clave = self.generarClave(nombre, apellido)
        contacto = self.contactos.get(clave)
        if contacto:
            print(contacto)
        else:
            print(f"El contacto '{nombre} {apellido}' no fue encontrado.")

    def ModificarContacto(self, nombre, apellido, nuevo_nombre=None, nuevo_apellido=None, direccion=None, email=None, telefonos=None, palabrasClave=None):
        clave_original = self.generarClave(nombre, apellido)
        contacto = self.contactos.get(clave_original)

        if not contacto:
            print("Contacto no encontrado.")
            return False

        if nuevo_nombre:
            contacto.nombre = nuevo_nombre
        if nuevo_apellido:
            contacto.apellido = nuevo_apellido
        if direccion is not None:
            contacto.direccion = direccion
        if email is not None:
            contacto.email = email
        if telefonos is not None:
            contacto.Telefonos = telefonos
        if palabrasClave is not None:
            contacto.PalabrasClave = palabrasClave

        nueva_clave = self.generarClave(contacto.nombre, contacto.apellido)
        if clave_original != nueva_clave:
            del self.contactos[clave_original]
            self.contactos[nueva_clave] = contacto

        print("Contacto actualizado exitosamente.")
        return True


    def buscarPorPalabraClave(self, palabra_clave):
        return [
            contacto for contacto in self.contactos.values()
            if palabra_clave.lower() in ", ".join(contacto.PalabrasClave or []).lower()
        ]

    def mostrarContactos(self):
        if not self.contactos:
            print("La lista de contactos está vacía.")
            return

        print("\n--- Lista de Contactos ---")
        for clave, contacto in self.contactos.items():
            print(f"Clave: {clave}")
            print(contacto)  
            print("-" * 30)
