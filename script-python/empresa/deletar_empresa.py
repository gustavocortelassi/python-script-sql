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

total_deleted = 0

while True:
    # Excluir em lotes de 1 milhão de registros
    sql = "DELETE FROM empresa ORDER BY id LIMIT 10000000"
    cursor.execute(sql)
    mydb.commit()
    
    # Verificar quantos registros foram excluídos nesta operação
    deleted_count = cursor.rowcount
    total_deleted += deleted_count
    
    if deleted_count == 0:
        break
    
    print(f"{deleted_count} empresas excluídas nesta iteração. Total excluído: {total_deleted}")

print("Exclusão concluída.")

cursor.close()
mydb.close()
