class Flor:
    __num=0
    __nbre=""
    __color=""
    __desc=""

    def __init__(self,datos:list[str]):
        self.__num=int(datos[0])
        self.__nbre=datos[1]
        self.__color=datos[2]
        self.__desc=datos[3]

    def Get_num(self):
        return self.__num
    def Get_nbre(self):
        return self.__nbre
    def Get_color(self):
        return self.__color
    def Get_desc(self):
        return self.__desc
    
    def __repr__(self):
        return "{} , {}, {}, {}".format(self.__num,self.__nbre,self.__color,self.__desc)