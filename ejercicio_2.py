###PEdir sexo y edad de una persona
###si es mujer y mayor de 18 imprimir("Es mujer y mayor de 18")
##si es mujer y menor de 18 imprimir("Es mjer y menor de 18")
## si es hombre y mayor de 18 imprimir ("Es hombre y mayor de 18")
## si es hombre y menor de 18 imprimir ("Puto el que lo lea")

sexo = input("Ingresar sexo: ")
edad = int(input("Ingresa edad: "))

if(sexo == "mujer" and edad >= 18):
    print("Es mujer y mayor de edad")
elif(sexo=="mujer" and edad < 18):
    print("Es mujer y menor de edad")
elif(sexo=="hombre" and edad >=18):
    print("Es hombre y mayor de edad")
elif(sexo=="hombre" and edad <18):
    print("Hombre menor de edad")
else:
    print("Persona no valida")