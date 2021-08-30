def main():
    # Escribe el código adecuado para completar el programa
x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))
z = int(input("Ingresa el tercer número: "))
    
if x<y and x<z:
    print (x)
    if y<z:
        print (y)
    else:
        print (z)
    if z>y and z>x:
        print (z)
    else:
        print (y)
elif y<x and y<z:
    print (y)
    if x<z:
        print (x)
    else:
        print (z)
    if z>x and z>y:
        print (z)
    else:
        print (x)
elif z<x and z<y:
    print (z)
    if x<y:
        print (x)
    else:
        print (y)
    if y>x and y>z:
        print (y)
    else:
        print (x)
        

