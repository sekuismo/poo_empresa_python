from persona import Persona
class Admin(Persona):
    def __init__(self,clave_admin,rut,clave,nombre,cargo):
        super().__init__(rut,clave,nombre,cargo)
        self._clave_admin = clave_admin

   


