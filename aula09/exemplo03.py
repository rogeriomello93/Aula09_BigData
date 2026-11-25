lista_catalogo = []

for i in range(3):
    print(f'\nLivro {i+1}')
    livro = {}

    livro['titulo'] = input('Informe o titulo do livro: ')
    livro['autor'] = input('Informe o autor: ')
    livro['ano'] = int(input('Informe o ano da publicação: '))
    livro['gênero'] = (input('Informe o gênero: '))
    livro['paginas'] = int(input('Informe o numero de páginas: '))
    lista_catalogo.append(livro)

# print(lista_catalogo)

for elemento in lista_catalogo:
    # print(elemento)
    if elemento['ano']>= 2020:
        print(elemento['titulo'])
        print(elemento['ano'])