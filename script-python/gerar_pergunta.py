import mysql.connector
from faker import Faker
from faker.generator import random

fake = Faker()

niveis = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']

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

num_perguntas = 50

for _ in range(num_perguntas):
    
    Cabecalho = fake.sentence()
    Dificuldade = fake.random_int(min=1, max=6)
    Tipo_Prova_Id = fake.random_int(min=1, max=4)
    Niveis_Id = random.choice(niveis)
    Audio = fake.uri()

    sql = "INSERT INTO Perguntas (Cabecalho, Dificuldade, Tipo_Prova_Id, Niveis_Id, Audio) VALUES (%s, %s, %s, %s, %s)"
    val = (Cabecalho, Dificuldade, Tipo_Prova_Id, Niveis_Id, Audio)

    cursor.execute(sql, val)
    mydb.commit()

print(num_perguntas, "registros inseridos com sucesso.")

cursor.close()
mydb.close()
