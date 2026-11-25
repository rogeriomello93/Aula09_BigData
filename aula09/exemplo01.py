produto1 = {} #Dicionário vazio

produto = {
    'nome': 'Notebook',
    'preço': 3500.80,
    'marca': 'Lenovo'
}


print(produto) #todas as chaves e valores
print(type(produto)) 

print(produto['nome']) #uma chave e valor em especifico
print(produto['preço']) #uma chave e valor em especifico

#Alterando os dados(valor)
produto['marca'] = "Positivo"
print(produto['marca']) 

# Adicionando chaves

produto['tela'] = '18"'
print(produto)

#deletando uma chave
del produto ['marca']
print(produto)

print(produto.keys()) #mostra as chaves
print(produto.values()) #mostra os valores das chaves
print(produto.items()) #mostra as chaves e valores