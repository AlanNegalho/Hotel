#conexao
import mysql.connector


class ConecxaoBD():
  def __init__(self,host="localhost",user="root",password="123456",
              database="hotel"):
              self.host = host
              self.user = user
              self.password = password
              self.database = database

  def conecta(self):
    self.con = mysql.connector.connect(
      host = self.host,
      user = self.user,
      password = self.password,
      database = self.database)
    self.cur = self.con.cursor()

  def desconecta(self):
    self.con.close()
  
  def executa_DQL(self, sql):
    self.conecta()
    self.cur.execute(sql)
    res = self.cur.fetchall()
    self.desconecta()
    return res

  def executa_DML(self,sql):
    self.conecta()
    self.cur.execute(sql)
    self.con.commit()
    self.desconecta()

#print(ConecxaoB)
#c = ConecxaoBD()
#c.conecta()
#sql = "INSERT INTO cadastro ( nome, cpf, telefone) VALUES ('a' , 'b', 'c')"
#c.cur.execute(sql)
#c.con.commit()


 # mydb = mysql.connector.connect(
  