from persona import Persona
class Admin(Persona):
    #clave admin 1234  clave 2 = 15B16K  rut = 11111111
    def __init__(self,clave_admin='1',rut='1',clave='1',nombre='Daniel',cargo='Administrador'):
        super().__init__(rut,clave,nombre,cargo)
        self._clave_admin = clave_admin

    def __str__(self):
        return f'Admin: {self._nombre}  Rut:  {self._rut}  Cargo: {self._cargo}  clave 1 :  {self._clave_admin}  clave 2 : {self._clave}  '



    def getAcceso(self):
        return self._clave_admin

    def getAcceso2(self):
        return self._clave
    def getRut(self):
        return self._rut




