import mysql.connector
from faker import Faker

fake = Faker()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="yonder"
)

if mydb.is_connected():
    print("Conexão ao banco de dados MySQL bem-sucedida.")
else:
    print("Não foi possível conectar ao banco de dados.")

cursor = mydb.cursor()

num_nivUser = 15000000
batch_size = 10000  # Tamanho do lote

try:
    for i in range(0, num_nivUser, batch_size):
        batch_data = []
        for _ in range(batch_size):
            niveis_id = fake.random_int(min=1, max=6)
            tipo_prova_id = fake.random_int(min=1, max=4)
            user_id = fake.random_int(min=4700, max=15004699)  
            batch_data.append((niveis_id, tipo_prova_id, user_id))
        
        sql = "INSERT INTO nivelamento_usuario (niveis_id, tipo_prova_id, user_id) VALUES (%s, %s, %s)"
        cursor.executemany(sql, batch_data)
        mydb.commit()
        print(f"Inseridos {i + batch_size if i + batch_size <= num_nivUser else num_nivUser} registros")

finally:
    cursor.close()
    mydb.close()

print(num_nivUser, "registros inseridos com sucesso.")
