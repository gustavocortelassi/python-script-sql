
# Exibir tamanho da tabela
# SELECT 
#     table_name AS "Table",
#     ROUND(((data_length + index_length) / 1024 / 1024), 2) AS "Size (MB)" 
# FROM 
#     information_schema.tables 
# WHERE 
#     table_schema = 'yonder';

# Zerar o contador de ID
# ALTER TABLE nome_da_tabela AUTO_INCREMENT = 1;
