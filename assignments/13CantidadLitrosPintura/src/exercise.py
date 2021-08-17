import math
def main():
    #escribe tu código abajo de esta línea
    area = float(input('Area a pintar en metros: '))
    cantidad = int(input('Rendimiento (m2/l): '))
    litrosPintura = area/cantidad
    print('Litros a comprar: '+ str(int(math.ceil(litrosPintura))))
if __name__ == '__main__':
    main()
