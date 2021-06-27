from archivos import *
#Aqui voy a generar el menu de la aplicacion
def menu():
    print("Bienvenido a su agenda papu:")
    print("-"*20)
    print("1. Agregar un registro")
    print("2. Mostrar registros")
    print("0. Salir")
    print("-"*20)
    opcion = input()
    continuar = True
    if opcion == "1":
        agregarRegistro()
    elif opcion == "2":
        mostrarRegistros()
    elif opcion == "0":
        continuar = False
    else: print("Oiga no sea logi!")
    return continuar

#Aqui voy a mostrar lo que haya guardado
def mostrarRegistros():
    personas = leer()
    for p in personas:
        print("--"*10)
        for k,v in p.items():
            print(k,v, sep=":")
        print("--"*10)

#Aca voy a pedir los datos de una nueva persona
def agregarRegistro():
    #va a pedir: nombre, apellido, edad, telefono y correo
    nombre = ""
    while nombre == "":
        nombre = input("Ingrese nombre de la persona:").strip() #esto es trim
        if nombre == "":print("Debe ingresar nombre")
    apellido = ""
    while apellido == "":
        apellido = input("Ingrese apellido de la persona:").strip()
        if apellido == "":print("Debe ingresar un apellido")
    edad = -1
    while edad <=17:
        try:
            edad = int(input("Ingrese edad de la persona"))
            if edad <=17: print("Debe ingresar solo mayores de edad")
        except:
            print("La edad debe ser un numero")
    telefono = ""
    while len(telefono) != 9:
        telefono = input("Ingrese telefono de la persona:")
        if len(telefono)!=9:print("El telefono debe tener largo 9")
    correo = ""
    while not "@" in correo:
        correo = input("Ingrese correo de la persona:").strip()
        if not "@" in correo:print("El correo no es valido")
    persona = {} #es un diccionario
    #persona = {"nombre":nombre,"apellido":apellido,"telefono":telefono}
    persona["nombre"] = nombre
    persona["apellido"] = apellido
    persona["telefono"] = telefono
    persona["correo"] = correo
    persona["edad"] = edad
    guardar(persona)
    