class Persona:
    def __init__(self,rut,clave,nombre,cargo):
        self._rut = rut
        self._clave = clave
        self._nombre = nombre
        self._cargo = cargo

    def __str__(self):
        return f'rut: {self._rut} \n clave: {self._clave} \n Nombre: {self._nombre} \n Cargo: {self._cargo}'

    