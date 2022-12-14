from con import *
from pessoa import Pessoa
from colorama import init, Fore, Back
import validar_CPF
from datetime import date
import os
import main


#classe reserva
class Reserva(Pessoa):
    def __init__(self,nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
    
    #funçao buscar cadastro
    def buscar():
        c = ConecxaoBD()
        c.conecta()
        os.system('clear')
        print(Fore.RED +'Consulta cadastro')
        
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
        sql = "SELECT * FROM cadastro WHERE cpf = %s"
        val= (cpf,)
        c.cur.execute(sql,val)
        c = c.cur.fetchall()
        print( "Nº| NOME |   CPF    |   TELEFONE   |")
        print()
        for x in c:
            print(x[0],x[1],x[2],x[3])
            print(Fore.CYAN +'Ja possui cadastro! ')
            per = input('Deseja realizar a reserva s/n: ')
            if per in 'Ss':
               Reserva.cadastrar_Reserva()
            elif per in 'Nn':
              reserva()
        print('Não possui Cadastro! ')
        per = input('Deseja realizar o Cadastro s/n: ')
        if per in 'Ss':
            Reserva.cadastrar()
        elif per in 'Nn':
            reserva()

    #funçao reserva
    def cadastrar_Reserva():
        c = ConecxaoBD()
        c.conecta()
        os.system('clear')
        print(Fore.RED +'Cadastro Reserva')
        nome = str(input("Nome: "))
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
        telefone = str(input("Telefone Nº: "))
        sql = "SELECT * FROM quarto WHERE reserva = 'L'"
        print('|Nº|Categoria|Valor|Wi-fi|Situação|')
        print()
        c.cur.execute(sql)
        c = c.cur.fetchall()
        for row in c:
            print(row)
        print()

        c = ConecxaoBD()
        c.conecta()
        n_quarto = input('Quarto Nº: ')
        val= (n_quarto,)
        sql = "SELECT * FROM funcionario WHERE id = %s"
        print("Funcionario responssavel")
        c.cur.execute(sql,val)
        c = c.cur.fetchall()

        for row in c:
            print(row[1])
        print()

        dia_checkin,mes_checkin,ano_checkin = map(int,input("Check-In: ").replace('/',' ').split())
        check_in = date(ano_checkin,mes_checkin,dia_checkin)
        dia_checkout,mes_checkout,ano_checkout = map(int,input("Check-Out: ").replace('/',' ').split())
        check_out = date(ano_checkout,mes_checkout,dia_checkout)
        c = ConecxaoBD()
        c.conecta()
        sql = "INSERT INTO reserva ( nome, cpf, telefone, n_quarto, check_in, check_out) VALUES (%s,%s,%s,%s, %s, %s)"
        val = (nome, cpf, telefone, n_quarto, check_in, check_out )
        c.cur.execute(sql,val)
        c.con.commit()
        print()

        sqli = "update quarto set reserva = %s where id = %s"
        valo = ('V', n_quarto)
        c.cur.execute(sqli,valo)
        c.con.commit()
        print(Fore.GREEN +"Reserva realizada com Sucesso!")
        print()

        per = input('Deseja realizar outra Reserva s/n: ')
        if per in 'Ss':
            Reserva.cadastrar_Reserva()
        elif per in 'Nn':
            reserva()
    #funçao cadstrar
    def cadastrar():
        c = ConecxaoBD()
        c.conecta()
        os.system('clear')
        print(Fore.RED +'Cadastro')
        nome = input('Digite o nome:')
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
        telefone = input('Digite o telefone: ')
        val =  nome, cpf, telefone
        sql = "INSERT INTO cadastro ( nome, cpf, telefone) VALUES (%s, %s, %s)"
        val = (nome , cpf, telefone)
        c.cur.execute(sql,val)
        c.con.commit()
        print()

        print(Fore.GREEN +'Cadastrdo com sucesso!')
        print("|  Nome  |     Cpf      | Telefone  |")
        print(val)
        
        per = input('Deseja realizar outro cadastro s/n: ')
        if per in 'Ss':
            Reserva.cadastrar()
        elif per in 'Nn':
            reserva()
    #funçao alterar dados
    def alterar():
        c = ConecxaoBD()
        c.conecta()
        os.system('clear')
        print(Fore.RED +'Atualização de Dados!')
        nome = input('Digite o nome:')
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
        telefone = input('Digite o telefone: ')
        n_registro = input('Nº de registro: ')

        sql = "update cadastro set nome = %s , cpf = %s , telefone = %s where id = %s"
        val = (nome, cpf, telefone, n_registro)
        c.cur.execute(sql,val)
        c.con.commit()

        print()
        print(Fore.GREEN +'Dados alterado com sucesso!')
        print("|  Nome  |     Cpf      | Telefone  | Nº registro")
        print(val)
        print()
        
        per = input('Deseja realizar outra atualizaçâo s/n: ')
        if per in 'Ss':
            Reserva.alterar()
        elif per in 'Nn':
            reserva()
            
def reserva(): 
    os.system('clear')

    print(Fore.CYAN+f"\n {'-'*51} ")
    print(Fore.RED+f"|{'Reserva `o´'.center(51)}|")
    print(Fore.CYAN+f" {'-'*51} \n")
    print(Back.LIGHTBLACK_EX+f" 1  -> {'Buscar'.center(44)}<-|")
    print(f"|{' '.center(52)}|")
    print(Back.LIGHTBLACK_EX+f" 2  -> {'Reservar'.center(44)}<-|")
    print(f"|{' '.center(52)}|")
    print(Back.LIGHTBLACK_EX+f" 3  -> {'Cadastrar'.center(44)}<-|")
    print(f"|{' '.center(52)}|")
    print(Back.LIGHTBLACK_EX+f" 4  -> {'Atualizar '.center(44)}<-|")
    print(f"|{' '.center(52)}|")
    print(Back.LIGHTBLACK_EX+f" 0  -> {'Home'.center(44)}<-|")
    print()

    op = str(input(Fore.RED + "-> "))

    if op == "1":
        Reserva.buscar()
    if op == "2":
        Reserva.cadastrar_Reserva()
    elif op == "3":
        Reserva.cadastrar()
    elif op == "4":
        Reserva.alterar()    
    elif op == "0":
        main.inicio()
        # Comandos para sair de um script
    else:
        print('Digite uma opção valida.')
        return reserva()
if __name__ == "__main__":
    reserva()