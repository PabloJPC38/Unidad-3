class carrera:

    __cod_c=""
    __nbre_c=""
    __dur=""
    __title=""

    def __init__(self,cod_c,nbre_c,title,dur):

        self.__cod_c=cod_c
        self.__nbre_c=nbre_c
        self.__dur=dur
        self.__title=title
    
    def Get_cod_c(self):
        return self.__cod_c
    def Get_nbre_c(self):
        return self.__nbre_c
    def Get_dur(self):
        return self.__dur
    def Get_title(self):
        return self.__title
    def __repr__(self):
        return "{} , {} , {} , {}".format(self.__cod_c,self.__nbre_c,self.__dur,self.__title)
    





