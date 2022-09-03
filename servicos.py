from colorama import init, Fore, Back
from con import mydb
import validar_CPF
import os
import main


def servicos(): 
    os.system('clear')

    print(Fore.CYAN+f"\n {'-'*51} ")
    print(Fore.RED+f"|{'Serviços `o´'.center(51)}|")
    print(Fore.CYAN+f" {'-'*51} \n")
    print(Back.CYAN+f" 1 -> {'consumer'.center(43)}<-|")
    print(f"|{' '.center(50)}|")
    print(Back.CYAN+f" 2 -> {'Lavanderia'.center(43)}<-|")
    print(f"|{' '.center(50)}|")
    print(Back.CYAN+f" 0 -> {'Home'.center(43)}<-|")
    print()

    op = str(input(Fore.RED+"-> "))

    if op == "1":
        Consumer.frigoba()
    elif op == "2":
        Consumer.lavanderia()
    elif op == "0":
        main.inicio()
        # Comandos para sair de um script
    else:
        print('Digite uma opção valida.')
        return servicos()
if __name__ == "__main__":
    servicos()
#classe serviços
class Consumer():
    def __init__(self,nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
    #funçao frigobar
    def frigoba():
        os.system('clear')
        mycursor = mydb.cursor()
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
        n_quarto = input('Quarto Nº -> ')
        sql = "SELECT * FROM frigoba WHERE id = %s"
        val= (n_quarto,)
        mycursor.execute(sql,val)

        print(Fore.BLUE +'Categoria| Produtos|')
        for row in mycursor:
            print(row[1], row[2] )
        print()
        per = input("'S'-> ")
        print('ok!')
        per = input('deseja mas alguma coisa s/n: ')
        if per in 'Ss':
            Consumer.lavanderia()
        elif per in 'Nn':
            servicos()
    #funçao lavanderia
    def lavanderia():
        os.system('clear')
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

        print('1 = vestuario|2 = roupas de cama')
        print('      R$50   |       R$ 100 ')
        opc = input('-> ')
        print('ok!')
        per = input('deseja mas alguma coisa s/n: ')
        if per in 'Ss':
            Consumer.lavanderia()
        elif per in 'Nn':
            servicos()