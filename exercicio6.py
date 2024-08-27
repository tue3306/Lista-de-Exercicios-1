# Exercício 6

biblioteca = []

def adicionar_livro(titulo, autor, ano):
    
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower() and livro["autor"].lower() == autor.lower():
            print("Este livro já está na biblioteca.")
            return
    livro = {"titulo": titulo, "autor": autor, "ano": ano}
    biblioteca.append(livro)
    print("Livro adicionado com sucesso!")

def listar_livros():
    if biblioteca:
        print("\nLista de livros na biblioteca:")
        for i, livro in enumerate(biblioteca, start=1):
            print(f"{i}. Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    else:
        print("Nenhum livro na biblioteca.")

def buscar_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            print(f"Livro encontrado: Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
            return
    print("Livro não encontrado.")

def remover_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            biblioteca.remove(livro)
            print("Livro removido com sucesso!")
            return
    print("Livro não encontrado.")

while True:
    print("\nMenu da Biblioteca:")
    print("1. Adicionar livro")
    print("2. Listar todos os livros")
    print("3. Buscar livro pelo título")
    print("4. Remover livro")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título do livro: ").strip()
        autor = input("Autor do livro: ").strip()
        ano = input("Ano de publicação: ").strip()
        adicionar_livro(titulo, autor, ano)
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        titulo = input("Digite o título do livro que deseja buscar: ").strip()
        buscar_livro(titulo)
    elif opcao == "4":
        titulo = input("Digite o título do livro que deseja remover: ").strip()
        remover_livro(titulo)
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
