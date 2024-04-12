import mysql.connector
from faker import Faker

fake = Faker()

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

num_respostas = 50

for _ in range(num_respostas):
    
    Titulo = fake.sentence() 
    Correto = fake.boolean()  
    Correto = 1 if Correto else 0 
    Ordem = fake.random_int(min=1, max=10)  
    Perguntas_Id = fake.random_int(min=1, max=50)

    sql = "INSERT INTO Respostas (Titulo, Correto, Ordem, Perguntas_Id) VALUES (%s, %s, %s, %s)"
    val = (Titulo, Correto, Ordem, Perguntas_Id)

    cursor.execute(sql, val)
    mydb.commit()

print(num_respostas, "registros inseridos com sucesso.")

cursor.close()
mydb.close()
