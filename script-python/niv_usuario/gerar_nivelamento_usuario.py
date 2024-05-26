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

num_nivUser = 15000000
batch_size = 1000  # Tamanho do lote

try:
    for i in range(0, num_nivUser, batch_size):
        batch_data = []
        for _ in range(batch_size):
            niveis = ["A1", "A2", "B1", "B2", "C1", "C2"]
            Niveis_Id = niveis[fake.random_int(min=0, max=len(niveis)-1)]
            Tipo_Prova_Id = fake.random_int(min=1, max=4)
            Usuarios_Id = fake.random_int(min=1, max=1000000)
            batch_data.append((Niveis_Id, Tipo_Prova_Id, Usuarios_Id))
        
        sql = "INSERT INTO Nivelamento_Usuario (Niveis_Id, Tipo_Prova_Id, Usuarios_Id) VALUES (%s, %s, %s)"
        cursor.executemany(sql, batch_data)
        mydb.commit()
        print(f"Inseridos {i + batch_size} registros")

finally:
    cursor.close()
    mydb.close()

print(num_nivUser, "registros inseridos com sucesso.")
