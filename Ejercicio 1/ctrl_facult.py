#from mod_facult import facultad
from csv import reader
from os import path
from mod_facult import facultad

class ManejaFacultades:
    
    __facultad:list[facultad]

    def __init__(self):
        
        self.__facultad=[]
    
    def Leer_Archivo(self):
        with open(path.dirname(__file__)+"/Facultades.csv","r",encoding="utf-8") as f:

            READER=reader(f,delimiter=";")
            cod:str="0"

            for l in READER:

                if cod not in l[0]:
                    f=facultad(l[0],l[1],l[2],l[3],l[4])
                    self.__facultad.append(f)
                    cod=l[0]
                else:
                    self.__facultad[int(cod)-1].Agregar_Carrera(l)


    def __repr__(self):
        return "{}".format(self.__facultad)
    
    def Mostrar_Facultad(self,cod:str):
        i,b=0,True
        while(b and i<len(self.__facultad)):
            if self.__facultad[i].Get_cod()==cod:
                print("Institución:",self.__facultad[i].Get_nbre())
                print()
                self.__facultad[i].Mostrar_Lista()
                b=False
            i+=1
    
    def Mostrar_Carrera(self,nbre):
        i,b=0,True
        while(b and i<len(self.__facultad)):
            if self.__facultad[i].Devolver_Carrera(nbre):
                print("Institución:",self.__facultad[i].Get_nbre()," ","Localidad:",self.__facultad[i].Get_local())
                b=False
            i+=1







