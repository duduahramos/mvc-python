def introduction_page():
    message = """\nSistema Cadastral\n\t* Cadastrar Pessoa - 1\n\t* Busca Pessoa Por Nome - 2\n\t* Sair - 5"""

    print(message)
    command = input("Comando: ")

    return command
