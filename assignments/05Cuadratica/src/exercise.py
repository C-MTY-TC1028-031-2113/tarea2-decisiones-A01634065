import math

def main():
    # Escribe tu código abajo de esta línea
    import math
a= int(input("Da el valor de a: "))
b= int(input("Da el valor de b: "))
c= int(input("Da el valor de c: "))
discriminante=((b**2) - 4*a*c)
r1=((-b) + (math.sqrt(discriminante)))/2*a
r2=((-b) - (math.sqrt(discriminante)))/2*a
if a==0 and b==0:
    print ("No tiene solucion")
elif a==0 and b!=0:
    despeje= ((-c)/b)
    print (despeje)
elif discriminante<0:
    print ("Raices complejas")
elif  discriminante==0:
    x=(-b)/2*a
else:
    print (r1)
    print (r2)
if __name__ == '__main__':
    main()
