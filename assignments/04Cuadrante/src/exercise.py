def main():
    # Escribe tu código abajo de esta línea
    pass
grados= int(input("Introduce los grados: "))
if grados>-1 and grados<361:
    if grados>0 and grados<90:
        cuadrante=1
        print ("cuadrante "+str(cuadrante))
    elif grados>90 and grados<180:
        cuadrante=2
        print ("cuadrante "+str(cuadrante))
    elif grados>180 and grados<270:
        cuadrante=3
        print ("cuadrante "+str(cuadrante))
    elif grados>270 and grados<360:
        cuadrante=4
        print ("cuadrante "+str(cuadrante))
    else:
        print ("eje")
            
else:
    print ("excede")
if __name__ == '__main__':
    main()
