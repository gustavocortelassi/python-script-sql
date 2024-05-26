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

num_formWrite = 10000  # Número de registros por ID
tamanho_texto = 10000000  # Tamanho aproximado do texto em caracteres

for _ in range(num_formWrite):
    Corrigido = fake.boolean()  
    Corrigido = 1 if Corrigido else 0  
    
    # Gerando um texto com aproximadamente 10.000.000 de caracteres
    Resposta = fake.text(max_nb_chars=tamanho_texto)
    
    Formulario_Respondido_Id = fake.random_int(min=10000, max=100000)

    sql = "INSERT INTO Formulario_Write (Corrigido, Resposta, Formulario_Respondido_Id) VALUES (%s, %s, %s)"
    val = (Corrigido, Resposta, Formulario_Respondido_Id)

    cursor.execute(sql, val)
    mydb.commit()

print(num_formWrite, "registros inseridos com sucesso.")

cursor.close()
mydb.close()
