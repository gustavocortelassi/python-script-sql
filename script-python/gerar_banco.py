import random
import mysql.connector
from faker import Faker
from faker.providers.ssn.pt_BR import Provider as BRProvider

fake = Faker()
provider_br = BRProvider(fake)

bairros = ["Centro", "Jardim", "Vila", "Bela Vista", "São José", "Industrial", "Nova", "Santo Antônio", "Santa Cruz", "Alvorada"]
niveis = ["A1", "A2", "B1", "B2", "C1", "C2"]

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

# Número de registros desejados para atingir 3 GB de dados
tamanho_total_desejado = 3 * 1024  # 3 GB
tamanho_por_registro = 0.0002727508544921875  # Defina o tamanho médio de um registro em MB

num_registros_desejados = tamanho_total_desejado / tamanho_por_registro

for _ in range(int(num_registros_desejados)):
    
    # INSERIR EMPRESAS
    RazaoSocial = fake.company()
    CNPJ = fake.numerify(text="##.###.###/####-##")
    CEP = fake.postcode()
    Logradouro = fake.street_address()
    Bairro = random.choice(bairros)
    Numero = fake.building_number()
    Complemento = fake.street_suffix()

    sql = "INSERT INTO Empresas (RazaoSocial, CNPJ, CEP, Logradouro, Bairro, Numero, Complemento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (RazaoSocial, CNPJ, CEP, Logradouro, Bairro, Numero, Complemento)

    cursor.execute(sql, val)
    
    # INSERIR USUARIOS
    Nome = fake.name()
    CPF = provider_br.cpf()
    Empresas_Id = fake.pyint(0, 2)

    sql = "INSERT INTO Usuarios (Nome, CPF, Empresas_Id) VALUES (%s, %s, %s)"
    val = (Nome, CPF, Empresas_Id)

    cursor.execute(sql, val)    
        
    # INSERIR NIVELAMENTO USUARIO
    
    Niveis_Id = niveis[fake.random_int(min=0, max=len(niveis)-1)]
    Tipo_Prova_Id = fake.random_int(min=1, max=4)  

    Usuarios_Id = fake.random_int(min=1, max=50) 

    sql = "INSERT INTO Nivelamento_Usuario (Niveis_Id, Tipo_Prova_Id, Usuarios_Id) VALUES (%s, %s, %s)"
    val = (Niveis_Id, Tipo_Prova_Id, Usuarios_Id)

    cursor.execute(sql, val)
    
    # INSERIR PERGUNTAS
    Cabecalho = fake.sentence()
    Dificuldade = fake.random_int(min=1, max=6)
    Tipo_Prova_Id = fake.random_int(min=1, max=4)
    Niveis_Id = random.choice(niveis)
    Audio = fake.uri()

    sql = "INSERT INTO Perguntas (Cabecalho, Dificuldade, Tipo_Prova_Id, Niveis_Id, Audio) VALUES (%s, %s, %s, %s, %s)"
    val = (Cabecalho, Dificuldade, Tipo_Prova_Id, Niveis_Id, Audio)

    cursor.execute(sql, val)
    
    # INSERIR RESPOSTAS
    Titulo = fake.sentence() 
    Correto = fake.boolean()  
    Correto = 1 if Correto else 0 
    Ordem = fake.random_int(min=1, max=10)  
    Perguntas_Id = fake.random_int(min=1, max=50)

    sql = "INSERT INTO Respostas (Titulo, Correto, Ordem, Perguntas_Id) VALUES (%s, %s, %s, %s)"
    val = (Titulo, Correto, Ordem, Perguntas_Id)

    cursor.execute(sql, val)
    
    # INSERIR FORMULARIO RESPONDIDO
    Correto = fake.boolean()  
    Correto = 1 if Correto else 0  
    Perguntas_Id = fake.random_int(min=1, max=50)
    Usuarios_Id = fake.random_int(min=1, max=50)

    sql = "INSERT INTO Formulario_Respondido (Correto, Perguntas_Id, Usuarios_Id) VALUES (%s, %s, %s)"
    val = (Correto, Perguntas_Id, Usuarios_Id)

    cursor.execute(sql, val)
    
    # INSERIR FORMULARIO WRITE
    Corrigido = fake.boolean()  
    Corrigido = 1 if Corrigido else 0  
    Resposta = fake.text()  
    Formulario_Respondido_Id = fake.random_int(min=1, max=50)

    sql = "INSERT INTO Formulario_Write (Corrigido, Resposta, Formulario_Respondido_Id) VALUES (%s, %s, %s)"
    val = (Corrigido, Resposta, Formulario_Respondido_Id)

    cursor.execute(sql, val)
    
    mydb.commit()   



print("Inserção de dados concluída.")

cursor.close()
mydb.close()