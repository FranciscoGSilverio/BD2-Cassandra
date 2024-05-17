1.
Criar a tabela: 
 CREATE TABLE pecas (
    id int,
    nome text,
    carro text,
    estante int,
    nivel int,
    quantidade int,
    PRIMARY KEY ((id, nome), estante)
 );

Inserindo os itens:
	
 INSERT INTO pecas (id, nome, carro, estante, nivel, quantidade) VALUES (5, 'Pistao', 'Mustang', 4, 1, 167);
 INSERT INTO pecas (id, nome, carro, estante, nivel, quantidade) VALUES (4, 'Suspencao', 'Argo', 1, 1, 3500);

2.	
QUERIES:
 SELECT * FROM pecas WHERE nome = 'Pistao' ALLOW FILTERING;
 SELECT quantidade FROM pecas;
 SELECT COUNT(*) FROM pecas;
 SELECT MAX(quantidade) AS "maior quantidade", MIN(quantidade) AS "menor quantidade" FROM pecas;
 SELECT nome, carro, quantidade FROM pecas WHERE estante = 3 ALLOW FILTERING;
 SELECT quantidade FROM pecas WHERE nivel = 1 ALLOW FILTERING;
 SELECT * FROM pecas WHERE estante < 3 AND nivel > 4 ALLOW FILTERING;

 
