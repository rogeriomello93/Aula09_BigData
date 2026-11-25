lista_contato = []
for registro in range(3):
    print(f'\nContato {registro+1}:')
    nome = input('Informe o nome: ')
    telefone = int(input('Informe o telefone: '))
    email = input('Informe o email: ')
    
    contato ={}

    contato['nome'] = nome
    contato['telefone'] = telefone
    contato['email'] = email
    lista_contato.append(contato)

for elemento in lista_contato:
    # print(elemento)
    print(f'O nome do cliente {registro+1} é: {elemento['nome']}')
    print(f'O numero de contato do cliente {registro+1} é: {elemento['telefone']}')
    print(f'O email do cliente {registro+1} é: {elemento['email']}\n')