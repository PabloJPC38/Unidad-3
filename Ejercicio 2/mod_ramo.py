from typing import List

from mod_flor import Flor
from typing import Literal
class Ramo:
    __tamaño:Literal["chico","mediano","grande"]
    __flor:list[Flor]

    def __init__(self,tamaño:Literal["chico","mediano","grande"]):
        self.__tamaño=tamaño
        self.__flor=[]

    def Set_flor(self,flor):
        self.__flor.append(flor)
    def Get_tamaño(self):
        return self.__tamaño
    def Get_flor(self):
        return self.__flor

    def __repr__(self):
        return "{} , {}".format(self.__tamaño,self.__flor)
