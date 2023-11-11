# EJERCICIO 2 :verificar paridad
 
# def verificar_pares(numero):
#     if (numero % 2) == 0: 
#         print('Es par')
#     else:
#         print('Es impar')

# verificar_pares(3) 
    
    
# EJERCICIO 3 : DICCIONARIO DE ESTUDIANTES 


estudiantes = {}

def agregar(estudiante,nombre,edad, calificacion):
    
    estudiante[nombre] = {
        "edad":edad , 
        "calificacion":calificacion
    }        
    

    print(estudiante)
    
        
agregar(estudiantes,"alejandro" , 25 , 4.5)
agregar(estudiantes,"juan" , 22 , 4)
agregar(estudiantes,"camila" , 21 , 5)      

def elimina(estudiante, nombre):
    if nombre in estudiante:
        del estudiante[nombre]
        print("estudiante esliminado")
    else:
        print("no se encontro el estudiante")     
    print(estudiante)        
         
elimina(estudiantes , "juan")       
   
           