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

num_formularios = 1000000  # Número de registros a serem inseridos
batch_size = 10000  # Tamanho do lote

try:
    for i in range(0, num_formularios, batch_size):
        batch_data = []
        for _ in range(batch_size):
            corrigido = fake.boolean(chance_of_getting_true=50)
            resposta = fake.paragraph(nb_sentences=5)
            form_resp_id = fake.random_int(min=90000, max=100000)
            correcao = fake.sentence()
            usuario_id = 0
            nota_writing = fake.random_element(elements=('A', 'B', 'C', 'D', 'E'))
            batch_data.append((corrigido, resposta, form_resp_id, correcao, usuario_id, nota_writing))
        
        sql = "INSERT INTO formulario_write (corrigido, resposta, form_resp_id, correcao, usuario_id, nota_writing) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.executemany(sql, batch_data)
        mydb.commit()
        print(f"Inseridos {i + batch_size if i + batch_size <= num_formularios else num_formularios} registros")

finally:
    cursor.close()
    mydb.close()

print(num_formularios, "registros inseridos com sucesso na tabela formulario_write.")
