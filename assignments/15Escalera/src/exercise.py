import math
def main():
    #escribe tu código abajo de esta línea
    casa = float(input('Altura de la casa: '))
    angulo = int(input('Angulo en grados: '))
    largo = round(casa / math.sin(math.radians(angulo))) 
    print('Largo de la escalera: '+str(largo))
if __name__ == '__main__':
    main()
