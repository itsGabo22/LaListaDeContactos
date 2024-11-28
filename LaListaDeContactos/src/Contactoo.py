__author__ = "Gabriel Esteban Paz Guerrero"
__license__ = "GPL"
__version__ = "1.0.3"
__email__ = "gabriel.pazg@campusucc.edu.co"


class Contacto:
    def __init__(self, nombre, apellido, direccion=None, email=None, Telefonos=None, PalabrasClave=None):
        if not nombre or not apellido:
            raise ValueError("El nombre y apellido son obligatorios.")
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion or ""
        self.email = email or ""
        self.Telefonos = Telefonos or []
        self.PalabrasClave = PalabrasClave or []

    def __str__(self):
        return (
            f"Nombre: {self.nombre} {self.apellido}\n"
            f"Direccion: {self.direccion}\n"
            f"Email: {self.email}\n"
            f"Numeros telefonicos: {', '.join(self.Telefonos)}\n"
            f"Palabras Clave: {', '.join(self.PalabrasClave)}"
        )
