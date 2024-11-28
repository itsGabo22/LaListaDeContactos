import pytest
from src.ListaContactos import ListaDeContactos
from src.Contactoo import Contacto

@pytest.fixture
def listadeContactos():
    return ListaDeContactos()

@pytest.fixture
def pruebaContacto():
    return Contacto(
        nombre="Prueba",
        apellido="Usuario",
        direccion="Calle Falsa 123",
        email="prueba@correo.com",
        Telefonos=["123456789"],
        PalabrasClave=["Test", "Prueba"] 
    )


def test_agregarContacto(listadeContactos: ListaDeContactos, pruebaContacto: Contacto):
    assert listadeContactos.agregarContacto(pruebaContacto)

def test_agregarContactoDuplicado(listadeContactos: ListaDeContactos, pruebaContacto: Contacto):
    listadeContactos.agregarContacto(pruebaContacto)
    with pytest.raises(ValueError, match="El contacto ya existe."):
        listadeContactos.agregarContacto(pruebaContacto)

def test_eliminarContacto(listadeContactos: ListaDeContactos, pruebaContacto: Contacto):
    listadeContactos.agregarContacto(pruebaContacto)
    listadeContactos.eliminarContacto("Prueba", "Usuario")

    for palabra in pruebaContacto.PalabrasClave:
        assert not listadeContactos.buscarPorPalabraClave(palabra)

def test_buscarPorPalabraClave(listadeContactos: ListaDeContactos, pruebaContacto: Contacto):

    listadeContactos.agregarContacto(pruebaContacto)
    assert pruebaContacto in listadeContactos.contactos.values()
    print("Palabras clave del contacto:", pruebaContacto.PalabrasClave)
    
    resultados = listadeContactos.buscarPorPalabraClave("Test")
    assert len(resultados) > 0, "No se encontraron resultados para la palabra clave 'Test'."
    assert resultados[0].nombre == "Prueba"
    assert resultados[0].apellido == "Usuario"

#Si el test no corre normalmente toca ejecutarlo dentro de un entorno virtual :)
