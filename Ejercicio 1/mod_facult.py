from mod_carrera import carrera

class facultad:

    __cod=""
    __nbre=""
    __dir=""
    __local=""
    __tel=""
    __carrera:list[carrera]

    def __init__(self,cod,nbre,dir,local,tel):

        self.__cod=cod
        self.__nbre=nbre
        self.__dir=dir
        self.__local=local
        self.__tel=tel
        self.__carrera=[]

    def __repr__(self):

        return "{} , {} , {} , {} , {}".format(self.__cod,self.__nbre,self.__dir,self.__local,self.__tel,self.__carrera)
    
    def Get_nbre(self):
        return self.__nbre
    def Get_local(self):
        return self.__local
    def Get_cod(self):
        return self.__cod
    def Agregar_Carrera(self,l):
        obj=carrera(l[0],l[1],l[2],l[3])
        self.__carrera.append(obj)
    def Mostrar_Lista(self):
        for c in self.__carrera:
            print("Nombre:",c.Get_nbre_c()," Duración:",c.Get_dur())
            print()
    
    def Devolver_Carrera(self,nbre:str)->bool:
        i,b,band=0,False,True
        while(band and i<len(self.__carrera)):
            if self.__carrera[i].Get_nbre_c()==nbre:
                print("Codigo ",self.__carrera[i].Get_cod_c(),"-",self.Get_cod())
                band,b=False,True
            i+=1
        return b
