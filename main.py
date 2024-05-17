from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def query_by_carro(carro):
    # Caminho para o Secure Connect Bundle
    secure_connect_bundle = 'secure-connect-s202estoque.zip'

    # Informações de autenticação
    client_id = 'AstraCS'
    client_secret = 'vAfiYAOtJUoCLZismkMbPnZD:2a83468879b26afd93a56fbbbc1433fe79ed6731510300bcc3e05b9d00845e79'

    auth_provider = PlainTextAuthProvider(client_id, client_secret)
    cluster = Cluster(cloud={'secure_connect_bundle': secure_connect_bundle}, auth_provider=auth_provider)
    session = cluster.connect('default_keyspace')

    try:
        # Prepara e executa a consulta
        query = "SELECT nome, estante, quantidade FROM pecas WHERE carro = %s"
        prepared = session.prepare(query)
        rows = session.execute(prepared, [carro])

        # Exibe os resultados
        for row in rows:
            print(f"Nome: {row.nome}, Estante: {row.estante}, Quantidade: {row.quantidade}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        # Fecha a conexão
        cluster.shutdown()

if __name__ == "__main__":
    carro = input("Digite o nome do carro: ")
    query_by_carro(carro)
