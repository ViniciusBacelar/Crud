# Import the mysql.connector module
import mysql.connector

# Check if this script is being run directly (not being imported as a module)
if __name__ == '__main__':
    # Establish a connection to the MySQL database
    conexao = mysql.connector.connect(
        host="localhost",  # Hostname or IP address of the MySQL server
        user="root",  # Username to use for the connection
        password="",  # Password to use for the connection
        database="projeto_crud"  # Name of the database to connect to
    )

    # Create a cursor object to execute SQL queries
    cursor = conexao.cursor()

    # Define a function to create a new record
    def create():
        # Prompt the user to input a name, age, and profession
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        profissao = input("Profissão: ")

        try:
            # Construct an INSERT query with parameterized values
            comando = 'INSERT INTO pessoas (nome, idade, profissao) VALUES (%s, %s, %s)'
            # Execute the query with the input values
            cursor.execute(comando, (nome, idade, profissao))
            # Commit the changes to the database
            conexao.commit()
        except mysql.connector.Error as err:
            # Catch any MySQL errors and print an error message
            print(f"Error: {err}")

    # Define a function to read all records
    def read():
        try:
            # Construct a SELECT query to retrieve all records
            comando = 'SELECT * FROM pessoas'
            # Execute the query
            cursor.execute(comando)
            # Fetch all the results
            resultado = cursor.fetchall()
            # Print each row of the result set
            for linha in resultado:
                print(linha)
        except mysql.connector.Error as err:
            # Catch any MySQL errors and print an error message
            print(f"Error: {err}")

    # Define a function to update a record
    def update():
        # Prompt the user to input an ID, name, age, and profession
        id = int(input("Digite o id: "))
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        profissao = input("Profissão: ")

        try:
            # Construct an UPDATE query with parameterized values
            comando = 'UPDATE pessoas SET nome = %s, idade = %s, profissao = %s WHERE id = %s'
            # Execute the query with the input values
            cursor.execute(comando, (nome, idade, profissao, id))
            # Commit the changes to the database
            conexao.commit()
        except mysql.connector.Error as err:
            # Catch any MySQL errors and print an error message
            print(f"Error: {err}")

    # Define a function to delete a record
    def delete():
        # Prompt the user to input an ID
        id = int(input("Digite o id: "))

        try:
            # Construct a DELETE query with a parameterized value
            comando = 'DELETE FROM pessoas WHERE id = %s'
            # Execute the query with the input ID
            cursor.execute(comando, (id,))
            # Commit the changes to the database
            conexao.commit()
        except mysql.connector.Error as err:
            # Catch any MySQL errors and print an error message
            print(f"Error: {err}")

    # Print a welcome message and prompt the user to choose an option
    print("Bem-vindo ao crud, deseja Criar(1), Ler(2), Atualizar(3) ou Deletar algum dado ?")
    opcao = int(input())

    # Call the corresponding CRUD function based on the user's input
    if opcao == 1:
        create()
    elif opcao == 2:
        read()
    elif opcao == 3:
        update()
    elif opcao == 4:
        delete()

    # Close the cursor and connection objects
    try:
        cursor.close()
        conexao.close()
    except mysql.connector.Error as err:
        # Catch any MySQL errors and print an error message
        print(f"Error: {err}")
