x = int(input("ingrese un numero: "))
if x > 0 or x == 0:
    print("es un numero positivo")
else:
    print("es un numero negativo")
  
if mismo_numero > 0 or mismo_numero == 0:
    print("el mismo numero es positivo")
else:
    print("el numero es negativo")


x = int(input("ingrese un numero: "))
multi = int(x * x)
print(multi)
if multi > 0 or multi == 0:
    print("el numero es positivo")
else:
    print("el numero es negativo")
print("humano vas a ingresar dos numeros")

x = int(input("ingrese numero 1 : "))
y = int(input("ingrese numero 2 : "))

if x == y:
    print("son iguales")
if x > y:
    print(f"el numeor mayor es {x}: ")
if x < y:
    print(f"el mayor numero es {y}:")
else:
    print("fuera rctm")
