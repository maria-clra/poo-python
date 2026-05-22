from classes import *

def main(): 
    bebida = Leite()
    bebida.preparar()

    bebida = Cafe()
    bebida.preparar()

    bebida = Cha()
    bebida.preparar()

if __name__ == "__main__":
    main()

