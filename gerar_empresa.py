import mysql.connector
from faker import Faker
from faker.providers.ssn.pt_BR import Provider as BRProvider

# Criar uma instância do Faker
fake = Faker('pt_BR')

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

# Número de empresas que você deseja inserir
num_emp = 5000

Faker.seed(0)
# Loop para inserir Empresas
for _ in range(num_emp):
    # Gerar dados falsos para a empresa
    RazaoSocial = fake.company()
    CNPJ = fake.numerify(text="##.###.###/####-##")
    CEP = fake.postcode()
    Logradouro = fake.street_address()
    Bairro = fake.neighborhood()
    Numero = fake.building_number()
    Complemento = fake.street_suffix()

    # Consulta SQL para inserir uma empresa na tabela "Empresas"
    sql = "INSERT INTO Empresas (RazaoSocial, CNPJ, CEP, Logradouro, Bairro, Numero, Complemento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (RazaoSocial, CNPJ, CEP, Logradouro, Bairro, Numero, Complemento)

    # Executar a consulta SQL
    cursor.execute(sql, val)

    # Confirmar a inserção dos dados
    mydb.commit()

# Imprimir mensagem de sucesso
print(num_emp, "empresas inseridas com sucesso.")

# Fechar o cursor e a conexão
cursor.close()
mydb.close()
