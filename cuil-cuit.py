class CuilCuit:
    __id = 0
    __numero = 0
    __dv = 0

    def __init__(self, id, numero, dv):
        self.__id = id
        self.__numero = numero
        self.__dv = dv

    def __str__(self):
        return self.cuilcuit
    
    @property
    def cuilcuit(self):
        return "{}-{}-{}".format(self.__id, self.__numero, self.__dv)

    @property
    def id(self):
        "ID del CUIL/CUIT (ID-nnnnnnnn-nn)."
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
        return None
    
    @property
    def numero(self):
        "NÚMERO del CUIL/CUIT (nn-_NÚMERO_-nn)."
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
        return None

    @property
    def dv(self):
        "DV del CUIL/CUIT (nn-nnnnnnnn-DV)."
        return self.__dv

    @dv.setter
    def dv(self, dv):
        self.__dv = dv
        return None
