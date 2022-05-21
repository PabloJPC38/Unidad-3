from ctrl_flor import Ctrl_Flor
from mod_ramo import Ramo

from operator import itemgetter
from  typing import Literal
class Ctrl_Ramo:

    __Ramo:list[Ramo]

    def __init__(self,ruta:str):

        self.__Ramo=[]
        self.__Flor=Ctrl_Flor.Leer_Archivo(ruta)


    def Contruir_Ramo(self,tamaño):

        c,r,b=0,Ramo(tamaño),True
        flor:str
        if tamaño not in ["chico","mediano","grande"]:
            print("Tamaño no valido")
        else:
            while c<5 and b:
                flor=input("Ingrese flor o [terminar] para finalizar:")
                if flor=="terminar":
                    b=False
                else:
                    r.Set_flor(self.Buscar_Flor(flor))
                    c+=1
            self.__Ramo.append(r)

    def Buscar_Flor(self,flor:str):
        i=0

        while(i<len(self.__Flor)):
            if self.__Flor[i].Get_nbre()==flor:
                return self.__Flor[i]
            i+=1

    def Las_Mas_Vendida(self):
        f:dict[str,int]={}
        i=0

        for r in self.__Ramo:
            for flor in r.Get_flor():
                nom=flor.Get_nbre()
                if nom in f:
                    f[nom]+=1
                else:
                    f[nom]=1

        flores=sorted(f.items(), key=itemgetter(1),reverse=True)

        print("Las flores más vendidas son:")
        while i<len(flores) and i<5:
            print(flores[i][0])
            i+=1
    
    def Flores_Vendidas_Según_Tamaño(self,tamaño:str):
        flores:list[str]=[]
        for r in self.__Ramo:
            if r.Get_tamaño()==tamaño:
                for flor in r.Get_flor():
                    if flor.Get_nbre() not in flores:
                        flores.append(flor.Get_nbre())
        print("Las flores vendidas para el tamaño ",tamaño," son:")
        print()
        for f in flores:
            print(f)

    def __repr__(self):

        return "{}".format(self.__Ramo)

