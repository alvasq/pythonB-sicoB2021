a=str(input("ingrese una contraseña"))
contra =str("1234alan") 
if (a.lower==contra.lower):
    
    print("contraseña correcta")
else:
    print("contraseña invalida")    
print("_________________________________________________")
a = input("Ingresa tu nombre: ")
nombre=a[0]
genero = input("Ingresa tu Genero (M o H): ")
if (genero == "M" and nombre.lower() < 'm') or (genero == "H" and nombre.lower() > 'n'):
    grupo = "A"
else:
    grupo = "B"
print("perteneces al grupo: " + grupo)
