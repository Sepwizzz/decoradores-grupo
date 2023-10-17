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


# PUNTO 3 :D

#10.255.255.255 ---- Si el primer octeto de una IP es 10 entonces se considera privada.
#172.31.255.255 ---- Si el primer octeto es igual a 172 y el segundo octeto está en el rango de 16 a 31 entonces se considera privada.
#192.168.100.50 ---- Si el primer octeto es igual a 192 y el segundo octeto es igual a 168, entonces la dirección IP se considera privada.


def verificar_ip(ip): #crea la funcion
    if ip[0] == 10 or (ip[0] == 172 and 16 <= ip[1] <= 31) or (ip[0] == 192 and ip[1] == 168): 
        #revisa primnero si el inicio de algun octeto de la IP generada es 10, si el primer octeto es igual a 172 y el segundo octeto está en el rango de 16 a 31,Si el primer octeto es igual a 192 y el segundo octeto es igual a 168, entonces la dirección IP se considera privada, lo cual retorna el mensaje abajo
        return "La dirección IP que se proporciono es privada."
    else: #si no se cumple retona el otro mensaje
        return "La dirección IP que se proporciono es pública."


#-------------------------------------------
ip=generar_direccion_ip()
lista=[237,11]
uno=validar_rango(clase)
capa2=uno(ip)
capa2

direccion_ip = generar_direccion_ip()
resultado = verificar_ip(direccion_ip)
print(resultado)