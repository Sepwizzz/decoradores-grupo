def validar_rango(func):
    def wrapper(lista):
        # Verificar si todos los números están en el rango [0, 100]
        if all(0 <= x <= 100 for x in lista):
            # Si todos los números están en el rango, ejecutar la función
            return func(lista)
        else:
            return "Algunos números están fuera del rango [0, 100]. No se ejecutará la función estadística."

    return wrapper

# Funciones 
def suma(lista):
    return sum(lista)

def promedio(lista):
    return sum(lista) / len(lista)

# Agrega más funciones estadísticas según sea necesario

# Decoramos las funciones estadísticas con la validación del rango
suma_validada = validar_rango(suma)
promedio_validado = validar_rango(promedio)

# Ejemplos de uso
lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 30, 110, 50]

print(suma_validada(lista1))  # Salida: 150
print(promedio_validado(lista2))  # Salida: Algunos números están fuera del rango [0, 100]. No se ejecutará la función estadística.
