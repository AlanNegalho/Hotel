from colorama import init, Fore, Back
import reserva
import registro
import servicos
import pagamento
import os
init(autoreset=True)

def inicio(): 
    
    os.system('clear')

    print(Fore.CYAN+f"\n {'-'*51} ")
    print(Fore.RED+f"|{'HOTEL DEVELOPER `o´'.center(51)}|")
    print(Fore.CYAN+f" {'-'*51} \n")
    print(Fore.CYAN+f" {'-'*51} ")
    print(Fore.LIGHTGREEN_EX +f"| 1 ->{'Reserva'.center(44)}<-|")
    print(Fore.CYAN+f" {'-'*51} ")
    print(Fore.LIGHTGREEN_EX + f"| 2 ->{'Serviços'.center(44)}<-|")
    print(Fore.CYAN+f" {'-'*51} ")
    print(Fore.LIGHTGREEN_EX + f"| 3 ->{'Registro'.center(44)}<-|")
    print(Fore.CYAN+f" {'-'*51} ")
    print(Fore.LIGHTGREEN_EX + f"| 4 ->{'Pagamento'.center(44)}<-|")
    print(Fore.CYAN+f" {'-'*51} ")
    print(Fore.LIGHTYELLOW_EX+ f"| 0 ->{'Sair'.center(44)}<-|")
    print(Fore.CYAN+f" {'-'*51}\n ")
    op = str(input(Fore.RED + f"-> "))

    if op == "1":
        reserva.reserva()
    elif op == "2":
        servicos.servicos()
    elif op == "3":
        registro.regist()
    elif op == "4":
        pagamento.pag()
    elif op == "0":
        # Comandos para sair de um script
        exit()
    else:
        print('Digite uma opção valida.')
        return inicio()
if __name__ == "__main__":
    inicio()    
