import pytest 
from src.Contactoo import Contacto

def test_CreacionContacto():
    contacto = Contacto(
        nombre="Gabriel",
        apellido="Paz",
        direccion="Calle 6a San Vicente",
        email="gabriel.pazg@campusucc.edu.co",
        Telefonos=["3164172093"],
        PalabrasClave=["Yo"]
    )
    assert contacto.nombre == "Gabriel"

def test_nombreFaltante():
    with pytest.raises(ValueError, match="El nombre y apellido son obligatorios."):
        Contacto(nombre="", apellido="Paz")

def test_ContactoString():
    contacto = Contacto(
        nombre="Daniel",
        apellido="Fajardo",
        Telefonos=["1112223333"],
        PalabrasClave=["Profesor"]
    )
    Esperado = (
        "Nombre: Daniel Fajardo\n"
        "Direccion: \n"
        "Email: \n"
        "Numeros telefonicos: 1112223333\n"
        "Palabras Clave: Profesor"
    )
    assert str(contacto) == Esperado
    
    #Si el test no corre normalmente toca ejecutarlo dentro de un entorno virtual :)