import sqlite3


MASTER_PASSWORD = ""

conn = sqlite3.connect("password.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    service TEXT NOT NULL, 
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
""")

# Master Password

senha = input("Insira sua senha master: ")
if senha != MASTER_PASSWORD:
    print("Senha Inválida! Encerrando...")
    exit()


# Password

def get_pasword(service):
    cursor.execute(f"""
    SELECT username, password FROM user
    WHERE service = '{service}'
    """)

    if cursor.rowcount == 00:
        print("Serviço não cadastrado (use 'l' para verificar seus serviços).")
    
    else:
        for user in cursor.fetchall():
            print(user)


def insert_password(service, username, password):
    cursor.execute(f"""
    INSERT INTO user (service, username, password)
    VALUES ('{service}', '{username}', '{password}')
    """)
    conn.commit()


def show_services():
    cursor.execute("""
        SELECT service FROM user;
    """)
    for service in cursor.fetchall():
        print(service)

# Menu Prompt

def menu():
    print("*" * 31)
    print("* i : inserir nova senha      *")
    print("* l : listar serviços salvos  *")
    print("* r : recuperar uma senha     *")
    print("* s : sair                    *")
    print("*" * 31)


while True:
    menu()
    op = input("O que deseja fazer?")
    if op not in ["l", "i", "r", "s"]:
        print("Opção inválida!")
        continue

    if op == "s":
        break

    if op == "i":
        service = input("Qual o nome do serviço? ")
        username = input("Qual o nome de usuario? ")
        password = input("Qual a senha? ")
        insert_password(service, username, password)
    
    if op == "l":
        show_services()
    
    if op == "r":
        service = input("Qual o serviço para o qual quer a senha? ")
        get_pasword(service)

conn.close()