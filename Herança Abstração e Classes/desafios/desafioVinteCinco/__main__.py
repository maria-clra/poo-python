from rich import print, inspect

from classes import *

def main(): 
    dist = 20
    entrega = Drone(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}")

    
if __name__ == "__main__":
    main()

