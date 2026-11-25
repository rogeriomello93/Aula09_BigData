# #Funções
# print()
# input()
# int()

#Definindo a função
def saudacao():
    print('Olá')

def saudacao2(x): # x é um Parametro
    print(f'Olá, {x}')


# saudacao()

#-------------------------------------#
nome = input('Digite seu nome: ')
saudacao2(nome) #passagem por parametro
saudacao2('Antonio')
saudacao2('Pedro')