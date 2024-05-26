import mysql.connector
from faker import Faker

fake = Faker()

import mysql.connector

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

num_registros = 90000
batch_size = 10000  # Tamanho do lote
form_resp_id = 10001  # Inicializando o form_resp_id

try:
    for i in range(10000, num_registros, batch_size):
        batch_data = []
        for _ in range(batch_size):
            corrigido = fake.boolean()
            resposta = fake.text(max_nb_chars=5000)
            batch_data.append((corrigido, resposta, form_resp_id))
            form_resp_id += 1  # Incrementando o form_resp_id
        
        sql = "INSERT INTO formulario_write (corrigido, resposta, form_resp_id) VALUES (%s, %s, %s)"
        cursor.executemany(sql, batch_data)
        mydb.commit()
        print(f"Inseridos {i + batch_size if i + batch_size <= num_registros else num_registros} registros")

finally:
    cursor.close()
    mydb.close()

print(num_registros, "registros inseridos com sucesso.")
