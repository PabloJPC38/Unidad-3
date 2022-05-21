from typing import Any
from mod_flor import Flor
from numpy import array,ndarray
from csv import reader

class Ctrl_Flor:
    __flor:ndarray[Flor,Any]

    def __init__(self,ruta):
        self.__flor=array(Ctrl_Flor.Leer_Archivo,dtype=Flor)

    @staticmethod
    def Leer_Archivo(ruta)->list[Flor]:
        with open(ruta,"r",encoding="utf-8") as f:
            return list(map(Flor,reader(f,delimiter=";")))
