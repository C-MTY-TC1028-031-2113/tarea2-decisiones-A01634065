
def main():
    pass
edad= int(input("Ingresa tu edad: "))
if edad>=18:
    ID= str(input("¿Tienes identificación oficial? (s/n): "))
    if ID=="s":
        print ("Trámite de licencia concedido")
    elif ID=="n":
        print ("No cumples requisitos")
    else:
        print("Respuesta incorrecta")

    
else:
    print ("No cumples requisitos")
    

if __name__ == '__main__':
    main()
