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

    name = input("Digite o seu Nome")           # Pedindo nome ao usuário
    email = input("Digite seu Email:")          # Pedindo email ao usuário  
    pas = input("Digite a sua Senha:")          # Pedindo a senha ao usuário

    try:
        conexao = conectar_banco()             # Iniciando conexão
        cursor = conexao.cursor()              # Criando o 'Manipulador' do Banco de Dados
        cursor.execute("INSERT INTO cadastro VALUES (null, %s, %s, %s)",(name,email,pas)) # Executando Comando
        conexao.commit()                       # Confirma as alterações do Banco de Dados
        print("Registro Criado com sucesso!")
    
    except mysql.connector.Error as bode:      # Except para mostrar Erro do MySql
        print(f"Deu ruim! {bode}")

    finally:                                    # Fechando a Conexão com o Banco
        if conexao.is_connected():
            conexao.close() 

def read():
    print("Selecionado: Buscar Registros!")

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM cadastro")
        cadastros = cursor.fetchall()     # Retorna o resultado da pesquisa como uma lista de tuplas
        print("\n Veja os Registros Encontrados!")
        for i in cadastros:               # Percorre cada tupla dentro da lista, cada i é uma TUPLA
            print(f"Registro Número: {i[0]}, Nome: {i[1]}, email: {i[2]}")

    except mysql.connector.Error as bode:
        print(f"Deu Ruim! {bode}")

    finally:
        if conexao.is_connected():
            conexao.close()

def update():
    print("Selecionado: Atualizar")
    id_usuario = input("Digite o ID do usuário que deseja atualizar: ")
    name = input("Digite o novo nome: ")
    email = input("Digite o novo email: ")

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("UPDATE cadastro SET nome = %s, email = %s WHERE id = %s", (name, email, id_usuario))
        conexao.commit()
        print("Registro Atualizado com Sucesso !")

    except mysql.connector.Error as bode:
        print(f"Deu Ruim ! {bode}")

    finally:
        if conexao.is_connected():
            conexao.close()

def delete():
    id_usuario = input("Digite o ID do usuário que deseja excluir: ")

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM cadastro WHERE id = %s", (id_usuario,)) # LEmbrar da ','
        conexao.commit()
        print("Registro Excluído com Sucesso!")

    except mysql.connector.Error as bode:
        print(f"Deu Ruim! {bode}")

    finally:
        if conexao.is_connected():
            conexao.close()

def menu():
    print("\nBem Vindo ao CRUD")
    while True:

        print("\nO que deseja fazer ?")
        print("\n(1) Criar Registro")
        print("(2) Listar Registros")
        print("(3) Atualizar Registro")
        print("(4) Excluir Registro")
        print("(5) Sair")

        decisao = input("")

        if decisao == "1":
            create()
        elif decisao == "2":
            read()
        elif decisao == "3":
            update()
        elif decisao == "4":
            delete()
        elif decisao == "5":
            print("Fechando programa ...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
    