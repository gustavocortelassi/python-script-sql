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

num_formResp = 100000
batch_size = 10000  # Tamanho do lote

try:
    for i in range(0, num_formResp, batch_size):
        batch_data = []
        for _ in range(batch_size):
            correto = fake.boolean()  
            correto = 1 if correto else 0  
            perguntas_id = fake.random_int(min=1, max=1540010)
            usuarios_id = fake.random_int(min=4700, max=15004699)
            batch_data.append((correto, perguntas_id, usuarios_id))
        
        sql = "INSERT INTO Formulario_Respondido (Correto, Perguntas_Id, Usuarios_Id) VALUES (%s, %s, %s)"
        cursor.executemany(sql, batch_data)
        mydb.commit()
        print(f"Inseridos {i + batch_size if i + batch_size <= num_formResp else num_formResp} registros")

finally:
    cursor.close()
    mydb.close()

print(num_formResp, "registros inseridos com sucesso.")
