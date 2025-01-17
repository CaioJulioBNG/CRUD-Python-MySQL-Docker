import mysql.connector
from dotenv import load_dotenv
import os
import bcrypt
import re

def encriptize(password):                  # Função para encriptar a senha
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash_password

def check_passw(hashed_password, user_password):
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def validar_nome(name):
    name_regex = r'^[A-Za-zÀ-ÿ]+(?: [A-Za-zÀ-ÿ]+)*$'
    check_regex = bool(re.match(name_regex, name))
    return check_regex

def validar_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    check_regex = bool(re.match(email_regex, email))
    return check_regex

def validar_password(passw):
    passw_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    check_regex = bool(re.match(passw_regex, passw))
    return check_regex

def validar_duplicagem(name):

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM cadastro WHERE nome = %s",(name,))
        resposta = cursor.fetchall()
        if resposta:
            return False
        else:
            return True
        
    except mysql.connector.Error as bode:
        print(f"Deu Ruim! {bode}")

    finally:
        if conexao.is_connected():
            conexao.close()


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

    while True:
        name = input("Digite o seu Nome:").strip()

        if not validar_nome(name):
            print("Nome inválido. Use apenas letras e espaços.")
            continue
        
        if not validar_duplicagem(name):
            print("Nome já cadastrado no sistema. Por favor use outro")
            continue

        break

    while True:
        email = input("Digite o seu Email")
        if validar_email(email):
            break
        print("Email inválido, Digite no formato (aaaaa@aaaaa.aaa)")

    while True:
        passw = input("Digite a sua Senha:")
        if validar_password(passw):
            pass_encript = encriptize(passw)
            break
        print("Senha Inválida! Coloque ao menos uma: letra minúscula, letra maiúscula, número, caractere especial, mínimo 8 caracteres")


    try:
        conexao = conectar_banco()             # Iniciando conexão
        cursor = conexao.cursor()              # Criando o 'Manipulador' do Banco de Dados
        cursor.execute("INSERT INTO cadastro VALUES (null, %s, %s, %s)",(name,email,pass_encript)) # Executando Comando
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

def login():
    print("Selecionado: Login")

    name = input("Digite o seu nome:")
    passw = input("Digite sua senha")

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM cadastro WHERE nome = %s", (name,))
        resultado = cursor.fetchall()
        if resultado:
            passw_db = resultado[0][3]
            if check_passw(passw_db, passw):
                print("Login Realizado com Sucesso!")
            else:
                print("Senha Incorreta! Tente Novamente!")
        else:
            print("Usuário não encontrado! Tente Novamente !")

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
        print("(6) Realizar Login")

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
        elif decisao == "6":
            login()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
    