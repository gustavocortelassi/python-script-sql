import mysql.connector
from faker import Faker
from faker.generator import random
from faker.providers.ssn.pt_BR import Provider as BRProvider

fake = Faker()
provider_br = BRProvider(fake)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bancodados" 
)

if mydb.is_connected():
    print("Conexão ao banco de dados MySQL bem-sucedida.")
else:
    print("Não foi possível conectar ao banco de dados.")

cursor = mydb.cursor()

num_users = 1000000

for _ in range(num_users):
    
    Nome = fake.name()
    CPF = provider_br.cpf()
    Empresas_Id = fake.pyint(3, 1002)

    
    sql = "INSERT INTO Usuarios (Nome, CPF, Empresas_Id) VALUES (%s, %s, %s)"
    val = (Nome, CPF, Empresas_Id)

    cursor.execute(sql, val)
    mydb.commit()

print(num_users, "registros inseridos com sucesso.")

cursor.close()
mydb.close()
