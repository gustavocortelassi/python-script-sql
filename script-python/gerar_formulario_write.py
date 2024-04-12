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

num_formWrite = 50

for _ in range(num_formWrite):
    Corrigido = fake.boolean()  
    Corrigido = 1 if Corrigido else 0  
    Resposta = fake.text()  
    Formulario_Respondido_Id = fake.random_int(min=1, max=50)

    sql = "INSERT INTO Formulario_Write (Corrigido, Resposta, Formulario_Respondido_Id) VALUES (%s, %s, %s)"
    val = (Corrigido, Resposta, Formulario_Respondido_Id)

    cursor.execute(sql, val)
    mydb.commit()

print(num_formWrite, "registros inseridos com sucesso.")

cursor.close()
mydb.close()
