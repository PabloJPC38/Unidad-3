from os import path
from ctrl_ramo import Ctrl_Ramo

if __name__=="__main__":
    
    def menu():
        obj,b=Ctrl_Ramo(path.dirname(__file__)+"/flores.csv"),True
        
        while b:
            print()
            print("1- Registrar un ramo")
            print("2- Mostrar las 5 flores más vendidas")
            print("3- Mostrar las flores vendidas por el tamaño")
            print("4- Para terminar")
            print()
            op=int(input("ingrese opción:"))
            
            if op==1:
                obj.Contruir_Ramo(input("Por favor ingrese tamaño de ramo:"))
                print()
            elif op==2:
                obj.Las_Mas_Vendida()
                print()
            elif op==3:
                obj.Flores_Vendidas_Según_Tamaño(input("Ingrese tamaño:"))
                print()
            elif op==4:
                b=False

    
    menu()

"""
### VALORES DE PRUEBA ###
1
chico
Ave del paraiso
Boca de dragon
terminar
1
chico
Nomeolvides
terminar
1
mediano
Petunias
Girasoles
terminar
1
grande
Gladiolos
Hortensias
terminar
1
grande
Gladiolos
Cactus de navidad
Jacintos
terminar
1
mediano
Cactus de navidad
Hortensias
terminar
1
chico
Boca de dragon
Aguileña
terminar
1
chico
Ave del paraiso
terminar
1
mediano
Jacintos
Hortensias
terminar
1
chico
Hortensias
Girasoles
Boca de dragon
terminar
1
grande
Petunias
Cactus de navidad
terminar
"""