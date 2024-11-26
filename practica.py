
print("\n Parte 1")
def bienvenido():
    n=input("Como te llamas?: ")
    print("Hola",n,"bienvenido a mi programa")
bienvenido()

print("\n Parte 1 segunda parte")
import math
def area_circulo():
    a=int(input("Digite el radio del circulo: "))
    area =math.pi *a**2
    return area
print("El area del circulo es: ", area_circulo())

print("\n parte 2")
def descuento(precio, descuento = 10):

    descuentoP=precio-(precio*(descuento/100))

    return descuentoP


precioP=int(input("Digite el precio del producto: "))
porcentaje =input("Digite el porcentaje de descuento: ")
if porcentaje == '':
    print("El valor a pagar es: ", descuento(precioP))
else:
    porcentaje=int(porcentaje)
    print("El valor a pagar es: ", descuento(precioP, porcentaje))


print("\n parte 3")

def mayor_valor(*num):
    return max(num)
print(f"El mayor valor es: {mayor_valor(1,2,3,4,10,6,7,)}")

print("\n parte 4")

def sumarlista(lista):
    s=0
    for i in lista:
        s=s+i
    return s

def mayorlista(lista):
    return max(lista)

def menornumeros(lista):
    return min(lista)


lista1=[2, 16, 6, 8, 19, 22, 23]
menor = menornumeros(lista1)
print(f"La suma de los valores de la lista es: {sumarlista(lista1)}")
print(f"El mayor valor de la lista es: {mayorlista(lista1)}")
print(f"El menor valor de la lista es: {menornumeros(lista1)}")

print("\n parte 4 segunda parte")

def mascaracteres(lista):
    pos = 0
    for x in range(len(lista)):
        if len(lista[x]) > len(lista[pos]):
            pos = x
    return lista[pos]

Lista2=["Manzana", "Jose", "zanahoria", "Juan", "Tomate", "Maria", "Pera"]
print(f"La palabra con mayor caracteres es: {mascaracteres(Lista2)}")