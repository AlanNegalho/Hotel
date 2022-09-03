from colorama import init, Fore, Back
from con import mydb
import main
import os

def regist(): 
    os.system('clear')


    print(Fore.CYAN+f"\n {'-'*51} ")
    print(Fore.RED+f"|{'Infor-Hotel `o´'.center(51)}|")
    print(Fore.CYAN+f" {'-'*51} \n")
    print(Back.LIGHTMAGENTA_EX +f" 1 -> {'Registros Ocupação'.center(44)}<-|")
    print(f"|{' '.center(51)}|")
    print(Back.LIGHTMAGENTA_EX +f" 0 -> {'Home'.center(44)}<-|")
    print()

    op = str(input(Fore.RED +"-> "))

    if op == "1":
        Registro.registro()
    elif op == "0":
        main.inicio()
        # Comandos para sair de um script
    else:
        print('Digite uma opção valida.')
        return regist()
if __name__ == "__main__":
    regist()
#classe registros de quartos do hotel    
class Registro():
    def __init__(self, cpf):
        self.cpf = cpf
    #funçao registro
    def registro():
        os.system('clear')
        mycursor = mydb.cursor()
        print(Fore.GREEN +'|Quartos desocupados|')
        mycursor.execute("SELECT * FROM quarto WHERE reserva = 'L'")
        print(Fore.BLUE +'Nº|Categoria|')
        for row in mycursor:
            print(row[0],row[1])
        mycursor.execute("SELECT * FROM quarto WHERE reserva = 'V'")
        print()
       
        print(Fore.GREEN +'|Quartos ocupados|')
        print(Fore.BLUE +'Nº|Categoria|')
        for row in mycursor:
            print(row[0],row[1])
        print()
        per =input(Fore.CYAN+"Voltar ou inicio digite 'S': ")
        if per in 'Ss':
            main.inicio()
        else:
            return (per)

