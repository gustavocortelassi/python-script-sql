import mysql.connector
from faker import Faker
import random

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

num_perguntas = 500000  # Total de perguntas
num_respostas = num_perguntas * 4  # 4 respostas por pergunta
batch_size = 10000  # Tamanho do lote

try:
    for i in range(0, num_respostas, batch_size):
        batch_data = []
        for _ in range(batch_size // 4):  # Para cada lote, criamos respostas para batch_size // 4 perguntas
            pergunta_id = fake.random_int(min=1, max=num_perguntas)
            ordem_respostas = [1, 2, 3, 4]
            random.shuffle(ordem_respostas)  # Embaralha a ordem das respostas para randomizar a ordem
            correta_pos = fake.random_int(min=0, max=3)  # Define a posição da resposta correta
            
            for idx in range(4):
                titulo = fake.sentence(nb_words=6)[:45]  # Garante que o título tenha no máximo 45 caracteres
                correto = 1 if idx == correta_pos else 0
                ordem = ordem_respostas[idx]
                batch_data.append((titulo, correto, ordem, pergunta_id))
        
        sql = "INSERT INTO respostas (titulo, correto, ordem, pergunta_id) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql, batch_data)
        mydb.commit()
        print(f"Inseridos {i + batch_size if i + batch_size <= num_respostas else num_respostas} registros")

finally:
    cursor.close()
    mydb.close()

print(num_respostas, "registros inseridos com sucesso.")
