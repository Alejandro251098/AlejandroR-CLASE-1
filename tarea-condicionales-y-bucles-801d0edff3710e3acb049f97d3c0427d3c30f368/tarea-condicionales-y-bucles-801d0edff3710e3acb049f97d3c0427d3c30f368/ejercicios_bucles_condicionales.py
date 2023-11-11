# CONDICIONALES

# ejercicio 1 : VERIFICACION DE NUMERO PAR O IMPAR

# numero = int(input('Ingrese un numero entero'))

# if (numero % 2) == 0: 
#     print('Es par')
# else:
#     print('Es impar')
 


    
    
#  ejercicio 2 : Clasificacion de edades


# edad = int(input("ingrese sus edad"))

# if edad  < 18 :
#       print("eres menor de edad")
        
# elif edad >= 18 and edad <= 65 :
#          print("eres un adulto")
        
# else:  
#   print("eres un adulto mayor")  



# Ejercicio 3 :Calculadora de descuento

#precio = int(input("ingrese el valor del producto"))
# edad = int(input("ingrese su edad"))


# if edad < 18  :
#     print(precio*0.9)
 
# elif edad >= 65:
#     print(precio * 0.85)
    
# if edad >=18 and edad < 65 :
#     print(precio)  



# Ejercicio 4 : Clasificacion de notas 


# nota = int(input("ingrese un numero"))
 
# if nota >= 90 and nota <= 100 : 
#     print ("A : sobrealiente")

# elif nota >= 80 and nota <= 89 :   
#     print ("B: bueno")
# elif nota >=70 and nota <= 79 :
#     print ("C: satisfactorio")
# elif nota >= 60 and nota <= 69 :
#     print("D: necesita mejorar")

# else :
#    print("F: reprobado")


# Ejercicio 5 : calculo impuesto sobre la renta


# salario = int ( input("ingrese el valor de su salario anual"))

# if salario <= 10000  :
#    print  ("no se aplica impuesto")
# elif salario > 10000 and salario <= 50000 :
#    print ( salario * 0.1)
# elif salario > 50000 and salario <= 100000 :
#     print (salario * 0.2)

# else :
#     print ( salario * 0.3) 
   
   

# EJERCICIO BUCLES "while"


# Ejercicio 1 :Contador ascendente y descendente 

# ascendente = 0
# descendente = 11
# while ascendente < 10 :
#    ascendente += 1
#    descendente -= 1
#    print(ascendente , "/" , descendente) 


# Ejercicio 2 : Adivina el numero

# import random

# aleatoreo = random.randint( 1,100)
# adivina = 0

# while adivina != aleatoreo :
#     if adivina == 0 :
#         print ( "inicia el juego")
#     elif adivina < aleatoreo :
#         print ( "demasiado bajo")
        
#     else :
#         print ("demasaido alto")
#     adivina = int(input("ingresa el numero"))           
#  print("haz ganado")


# BUCLES "for "

# Ejercicio 1 : Tblas de multiplicar 

# numeros = int(input('Ingrese un numero'))

# for multipos in range(1, 11):
#       resultado = numeros * multipos
#       print(numeros, '*', multipos, '=', resultado) 



# Ejercicio 2 : Suma de numeros pares

# numero = int (input("ingrese un numero"))
# suma = 0
# for ( numero ) in range ( 2 , numero + 1) :
#     if  numero % 2 == 0 :
    
#      print( numero)
#      suma = suma + numero
     
# print ( "la suma de los pares es ", suma)


 
# EJERCICIO 3 : Patron de asteriscos 

# num = int(input("ingrese un valor"))

# for num in range ( 1 , num +1):
#   for  n in range (num ):
#      print("*" , end= "")
#   print("")


# CONDICIONALES Y BUCLES 


# EJERCICIO 1: Suman de numeros pares for y if 


# numero = int (input("ingrese un numero"))
# suma = 0
# for ( numero ) in range ( 1 , numero + 1) :
#     if  numero % 2 == 0 :
    
#      print( numero)
#      suma = suma + numero
     
# print ( "la suma de los pares es ", suma)

# EJERCICIO 2 : Contador de vocales while e if

# def  contar_vocales(input_string) :
#      vocales ="aeiou" 
#      cantidad = 0 
#      index = 0
#      while  index < len(input_string) :      
#       if input_string[index].lower() in  vocales:
#          cantidad += 1             
#       index += 1  
#      return  cantidad 
# cadena= input(" ingrese una frase:")
# print( "La cantidad de vocales es :", contar_vocales(cadena))


cadena= input("frase:")

contador_voc = 0

index= 0

while index < len(cadena) :
   letra= cadena[index] 
   if letra.lower() in "aeiou":
      contador_voc +=1  
   index +=1
print("la cantidad es ", contador_voc )   


# EJERCICIO 3 : numeros primos for if y else


# num = int(input("ingrese un numero entero mayor a uno : "))

# if num <= 1 :
#          print("por favor escribir un numero entero positivo mayor a uno :")
# else :
#        contador = 0  
#        for  i in range(1 , num + 1):
#         if num % i == 0 :
#               contador += 1      
#        if contador == 2 : 
#                 print(f"{num} es un numero primo " )
#        else :
#                 print(f"{num} no es un numero primo")       
                 
                      
   
# EJERCICIO 4 : Adivina el numero secreto con while e if 

# import random

# aleatoreo = random.randint( 1,100)
# adivina = 0

# while adivina != aleatoreo :
#     if adivina == 0 :
#         print ( "inicia el juego")
#     elif adivina < aleatoreo :
#         print ( "demasiado bajo")
        
#     else :
#         print ("demasaido alto")
#     adivina = int(input("ingresa el numero"))           
#  print("haz ganado")



# EJERCICIO 5 : Patron de asteriscos


# num = int(input("ingrese un valor"))

# for x in range (1,  num +1 ):
#   for  y in range (num ):
#          if num % 2 == 0 :
#           print("*",end="" )   
#   else :
#      print ("*")  
         
         
  
                      
                  
         
                 