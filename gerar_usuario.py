import mysql.connector
from faker import Faker
from faker.generator import random
from faker.providers.ssn.pt_BR import Provider as BRProvider

# Criar uma instância do Faker
fake = Faker()

# Criar uma instância do provider brasileiro de CPF
provider_br = BRProvider(fake)

# Conectar ao banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bancodados"  # Substitua pelo nome do seu banco de dados
)

# Verificar se a conexão foi bem-sucedida
if mydb.is_connected():
    print("Conexão ao banco de dados MySQL bem-sucedida.")
else:
    print("Não foi possível conectar ao banco de dados.")

# Cursor para executar consultas SQL
cursor = mydb.cursor()

# Número de usuários que você deseja inserir
num_users = 500

# Loop para inserir usuários
for _ in range(num_users):
    # Gerar dados falsos para o usuário
    Nome = fake.name()
    CPF = provider_br.cpf()
    Empresas_Id = fake.pyint(0,5000)

    # Consulta SQL para inserir um usuário na tabela "usuario"
    sql = "INSERT INTO Usuarios (Nome, CPF, Empresas_Id) VALUES (%s, %s, %s)"
    val = (Nome, CPF, Empresas_Id)

    # Executar a consulta SQL
    cursor.execute(sql, val)

    # Confirmar a inserção dos dados
    mydb.commit()

# Imprimir mensagem de sucesso
print(num_users, "registros inseridos com sucesso.")

# Fechar o cursor e a conexão
cursor.close()
mydb.close()
