from ctrl_facult import ManejaFacultades

if __name__=="__main__":

    def menu(obj:ManejaFacultades):
        op,b=0,True
        while b:
            print()
            print("1-Mostrar nombre de la facultad, nombre de las carrerras y su duración")
            print()
            print("2-Mostrar código de carrera, nombre y localidad de la facultad")
            print()
            print("3-Para Terminar")
            print()
            op=int(input("Ingrese opción:"))

            if op==1:
                obj.Mostrar_Facultad(input("Ingrese código de facultad:"))
                print()
            if op==2:
                obj.Mostrar_Carrera(input("Ingrese nombre de la carrera:"))
                print()
            if op==3:
                b=False
    
    obj=ManejaFacultades()
    obj.Leer_Archivo()
    menu(obj)

#Valores de prueba
#1
#Ingeniería en Agrimensura