import mysql.connector
from faker import Faker
from faker.providers.ssn.pt_BR import Provider as BRProvider

fake = Faker('pt_BR')

provider_br = BRProvider(fake)

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

num_users = 15000000
batch_size = 100000  # Tamanho do lote

Faker.seed(0)

try:
    for i in range(0, num_users, batch_size):
        batch_data = []
        for _ in range(batch_size):
            Nome = fake.name()
            CPF = provider_br.cpf()
            Empresas_Id = fake.pyint(1, 100000)
            batch_data.append((Nome, CPF, Empresas_Id))
        
        sql = "INSERT INTO usuario (nome, cpf, emp_id) VALUES (%s, %s, %s)"
        cursor.executemany(sql, batch_data)
        mydb.commit()
        print(f"Inseridos {i + batch_size} usuários")

finally:
    cursor.close()
    mydb.close()

print(num_users, "usuários inseridos com sucesso.")
