import mysql.connector
from dotenv import load_dotenv
import os


def conectar_banco():

    load_dotenv() # Carregando as variáveis do arquivo .env

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
        )

def create():
    print("Selecionado: Criar Registro!")

    name = input("Digite o seu Nome")
    email = input("Digite seu Email:")
    pas = input("Digite a sua Senha:")

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO cadastro VALUES (null, %s, %s, %s)",(name,email,pas))
        conexao.commit()
        print("Registro Criado com sucesso!")
    
    except mysql.connector.Error as ruim:
        print(f"Deu ruim! {ruim}")

    finally:
        if conexao.is_connected():
            conexao.close()

if __name__ == "__main__":
    create()
    