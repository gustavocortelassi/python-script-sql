import mysql.connector
from faker import Faker
from faker.providers.ssn.pt_BR import Provider as BRProvider

fake = Faker('pt_BR')

provider_br = BRProvider(fake)

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

num_emp = 10000

Faker.seed(0)
for _ in range(num_emp):
    RazaoSocial = fake.company()
    CNPJ = fake.numerify(text="##.###.###/####-##")
    CEP = fake.postcode()
    Logradouro = fake.street_address()
    Bairro = fake.neighborhood()
    Numero = fake.building_number()
    Complemento = fake.street_suffix()

    sql = "INSERT INTO Empresas (RazaoSocial, CNPJ, CEP, Logradouro, Bairro, Numero, Complemento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (RazaoSocial, CNPJ, CEP, Logradouro, Bairro, Numero, Complemento)

    cursor.execute(sql, val)
    mydb.commit()

print(num_emp, "empresas inseridas com sucesso.")

cursor.close()
mydb.close()
