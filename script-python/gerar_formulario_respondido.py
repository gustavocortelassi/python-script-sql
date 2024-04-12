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

num_formResp = 50

for _ in range(num_formResp):
    Correto = fake.boolean()  
    Correto = 1 if Correto else 0  
    Perguntas_Id = fake.random_int(min=1, max=50)
    Usuarios_Id = fake.random_int(min=1, max=50)

    sql = "INSERT INTO Formulario_Respondido (Correto, Perguntas_Id, Usuarios_Id) VALUES (%s, %s, %s)"
    val = (Correto, Perguntas_Id, Usuarios_Id)

    cursor.execute(sql, val)
    mydb.commit()

print(num_formResp, "registros inseridos com sucesso.")

cursor.close()
mydb.close()
