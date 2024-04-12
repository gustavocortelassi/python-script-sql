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

num_nivUser = 50

for _ in range(num_nivUser):
    
    niveis = ["A1", "A2", "B1", "B2", "C1", "C2"]

    Niveis_Id = niveis[fake.random_int(min=0, max=len(niveis)-1)]
    Tipo_Prova_Id = fake.random_int(min=1, max=4)  

    Usuarios_Id = fake.random_int(min=1, max=50) 

    sql = "INSERT INTO Nivelamento_Usuario (Niveis_Id, Tipo_Prova_Id, Usuarios_Id) VALUES (%s, %s, %s)"
    val = (Niveis_Id, Tipo_Prova_Id, Usuarios_Id)

    cursor.execute(sql, val)
    mydb.commit()

print(num_nivUser, "registros inseridos com sucesso.")

cursor.close()
mydb.close()
