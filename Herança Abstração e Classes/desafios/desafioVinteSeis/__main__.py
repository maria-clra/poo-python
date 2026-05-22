from classes import *

def main(): 
    f1 = Horista("paulo", 12, 200)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Mensalista("amanda", 2000)
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == "__main__":
    main()
