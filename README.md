 # CRUD com Python, MySQL e Docker

 ![Tela Inicial](img/ilustracao1.png)

 Este é um projeto simples desenvolvido com **Python**, **MySql** e **Docker**, explorando boas práticas como validações com **Regex** e criptografia de senhas com **bcrypt**.

 ## Objetivo do Projeto

 Este projeto tem como objetivo solidificar meu conhecimentos em **Python**, **MySQL**, e **Docker**. Assim como explorar novar tecnologias como **Regex** e o **bcrypt**

 ## IMPORTANTE

 Este projeto fui idealizado para rodar localmente em um ambiente **Linux**. Para aplicações em outros sistemas talvez seja necessário alterações.

 ## Funcionalidades do Projeto:

 - Cadastro de usuários: Nome, e-mail e senha com Regex
 - Proteção de Senhas: Criptografia usando bcrypt
 - Banco de Dados: MySQL rodando em um container Docker

 ## Configurações Iniciais do Docker

 ### Comando Inicial para o container MySQL

Execute o comando abaico para iniciar o container MySQL para esse projeto. Atente-se as variáveis:

- **NOME_DO_CONTAINER**: é o nome desejado do container
- **DIRETORIO_ARMAZENAMENTO_PERMANENTE**: O docker por padrão não armazena os arquivos, sendo assim é necessário indicar uma pasta local para o armazenamento da database
- **SENHA_ACESSO**: É a senha para acessar o MySQL. Lembre-se de adicionar no arquivo .env descrito no tópico a seguir
- **NOME_DATABASE**: É o nome da database. Assim como a SENHA_ACESSO, lembre-se de adicionar no arquivo .env descrito no tópico a seguir

**COMANDO**:
 docker run --name [NOME_DO_CONTAINER] -v mysql_data:[DIRETORIO_ARMAZENAMENTO_PERMANENTE] -e MYSQL_ROOT_PASSWORD=[SENHA_ACESSO] -e MYSQL_DATABASE=[NOME_DATABASE] -p 3306:3306 -d mysql

### Conexão ao Banco de Dados pelo Terminal

Caso seja necessário interagir com o bando de dados direto pelo terminal, use esse comando:

COMANDO:
docker exec -it [CONTAINER_ID] mysql -u root -p

Lembre-se de verificar o container_id pelo Docker Desktop ou pelo próprio terminal

### Criação da Primeira Tabela

É necessário criar a primeira tabela manualmente:

Comando:
CREATE TABLE `cadastro` (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password TEXT NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB;

## Criação de um Arquivo .env

Crie um arquivo .env para importar as configurações do container do MySQL:

DB_HOST =localhost
DB_USER =root
DB_PASSWORD =[SENHA_ACESSO]
DB_NAME =[NOME_DATABASE]
