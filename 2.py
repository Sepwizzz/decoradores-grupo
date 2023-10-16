import random

def validar_rango(func):
    def wrapper(lista):
        # Verificar si todos los números están en el rango [0, 100]
        for i in lista:
            pass
        if i < 255:
            # Si todos los números están en el rango, ejecutar la función
            return func(lista)
        else:
            return "Algunos números están fuera del rango [0, 100]. No se ejecutará la función estadística."

    return wrapper


def generar_direccion_ip():
    octetos = [str(random.randint(0, 255)) for _ in range(4)]
    direccion_ip = ".".join(octetos)
    delimiter = "."
    lista = direccion_ip.split(delimiter)
    lista2=[]
    for i in lista:
        lista2.append(int(i))
    print(direccion_ip)
    return lista2

# funcionesss

def tipo(tipo):
    print(f"es tipo :{type(tipo)}")


def  clase(lista):
    i=lista[0]
    print(lista)
    if i < 127:
        print("class a")
    elif i <191:
        print("class b")
    elif i <223:
        print("class c")
    elif i <239:
        print("class d")
    elif i <255:
        print("class e")

#-------------------------------------------
ip=generar_direccion_ip()
lista=[237,11]
uno=validar_rango(clase)
capa2=uno(ip)
capa2
    