from colorama import init, Fore, Back
from con import *
from pessoa import Pessoa
import datetime
import time
import validar_CPF
import reserva
import main
import os


#classe pagamento
class Pagamento(Pessoa):
    def __init__(self,cpf):
        pass
    #Funçao pagamento
    def pagamento():
        os.system('clear')
        c = ConecxaoBD()
        c.conecta()
        print('Despesa Hospede'.center(30))
        print(Fore.GREEN+f"\n {'-'*30} ")
        print()
        cont = True
        while cont:
            cpf = str(input("CPF: "))
            if len(cpf) >= 14:
                validar = validar_CPF.Validar(cpf)
                if validar == False:
                    print("CPF inválido!\n")
                else:
                    cont = False
            else:
                print("Informe um nº de CPF válido!")
        n = input('Nº quarto: ')
        sql = "SELECT * FROM funcionario WHERE id = %s"
        val= (n,)
        c.cur.execute(sql,val)
        c = c.cur.fetchall()
        
        sqli = "update quarto set reserva = %s where id = %s"
        valo = ('L', n)
        c = ConecxaoBD()
        c.conecta()
        c.cur.execute(sqli,valo)
        c.con.commit()
        print(Fore.BLUE+"Funcionario responssavel")
        print()
        c = c.cur.fetchall()
        for x in c:
            print(x[1])
        print()
        c = ConecxaoBD()
        c.conecta()
        sql = "SELECT * FROM reserva WHERE cpf = %s"
        val= (cpf,)
        c.cur.execute(sql,val)
        c = c.cur.fetchall()
        print(Fore.BLUE+"NOME | Nº |Check-In|Check-Out|")
        print()
        for x in c:
            print(x[1],x[4],x[5],x[6])
            print('')
            c = ConecxaoBD()
            c.conecta()
            sql = "SELECT * FROM quarto WHERE  id = %s"
            val= (n,)
            print(Fore.BLUE+'|Valor da diaria|')
            c.cur.execute(sql,val)
            c = c.cur.fetchall()
            for x in c:
                print(' R$',x[2])
            print(f"\n {'-'*23} ")
            print(Fore.BLUE+'|  Forma de Pagamento |')
            print(Fore.GREEN+"|1| DINHEIRO / |2|PIX |")
            print()
            op = input(Fore.RED+'-> ')
            if op in '1':
                os.system('clear')
                def slowprint(texto, atraso=0.4):
                    for c in texto:
                        print(c,end='',flush=True)
                        time.sleep(atraso)

                slowprint('Efetuado com Sucesso!')
                print(Fore.CYAN+f"\n {'-'*30} ")
                print(Fore.RED+f"|{'HOTEL DEVELOPER `o´'.center(31)}|")
                print(Fore.CYAN+f" {'-'*30} \n")
                print('Rua: Nova york, 789 - Corrente')
                print('Cep: 64980-000 - Piaui')
                print('Cnpj: 14.354.850/0000-20')
                print('Fone: (89)35732518')
                print(Fore.BLACK+f"{'Recibo'.rjust(29)}")
                print()
                print(f'Valor R$ {x[2]}'.rjust(31))
                print()
                print()
                print(f"{'volte Sempre!'.center(31)}")
                print()
                x = datetime.datetime.now()
                print(f'{x.strftime("%d - %m - %y")}'.center(30))
                print(Fore.CYAN+f" {'-'*30} \n")
                print()
                print()
                print()
                r = input("return Home 'S'-> ")
                if r in 'Ss':
                    main.inicio()
            elif op in '2':
                os.system('clear')
                def slowprint(texto, atraso=0.4):
                    for c in texto:
                        print(c,end='',flush=True)
                        time.sleep(atraso)

                slowprint('Pix recebido com Sucesso!')
                print(Fore.CYAN+f"\n {'-'*30} ")
                print(Fore.RED+f"|{'HOTEL DEVELOPER `o´'.center(31)}|")
                print(Fore.CYAN+f" {'-'*30} \n")
                print('Rua: Nova york, 789 - Corrente')
                print('Cep: 64980-000 - Piaui')
                print('Cnpj: 14.354.850/0000-20')
                print('Fone: (89)35732518')
                print(Fore.BLACK+f"{'Recibo'.rjust(29)}")
                print()
                print(f'Valor R$ {x[2]}'.rjust(31))
                print()
                print()
                print(f"{'volte Sempre!'.center(31)}")
                print()
                x = datetime.datetime.now()
                print(f'{x.strftime("%d - %m - %y")}'.center(30))
                print(Fore.CYAN+f" {'-'*30} \n")
                print()
                print()
                print()
                r = input("return Home 'S'-> ")
                if r in 'Ss':
                    main.inicio()

def pag(): 
    os.system('clear')
    print(Fore.CYAN+f"\n {'-'*51} ")
    print(Fore.RED+f"|{'Pagamentos `o´'.center(51)}|")
    print(Fore.CYAN+f" {'-'*51} \n")
    print(Back.LIGHTYELLOW_EX + f" 1  -> {'pagamento'.center(43)}<-|")
    print(f"|{' '.center(51)}|")
    print(Back.LIGHTYELLOW_EX + f" 0  -> {'Home'.center(43)}<-|")
    print()

    op = str(input(Fore.RED+"-> "))

    if op == "1":
        Pagamento.pagamento()
    elif op == "0":
        main.inicio()
        # Comandos para sair de um script
    else:
        print('Digite uma opção valida.')
        return pag()
if __name__ == "__main__":
    pag()