a = input("Introduce un numero: ")
print(a)
x = "x"
b=int(a)
i = 0
while i < b:
  print(x)
  x=x+"x"
  i += 1


a=int(input("ingrese un numero entero mayor que 2"))
contador=int(2)

while a%contador != 0:
    contador=contador+1
if contador==a:
    print("el numero " + str(a) + " es primo")
else:
    print("el numero " + str(a) + " no es primo")  