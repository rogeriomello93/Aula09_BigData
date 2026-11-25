def soma(x,y):
    r = x + y
    # print(r)
    return r #retorna o resultdo


# num1 = 5
# num2 = 9
# soma(num1,num2)
for i in range(3):
    num1 = float(input('Informe o numero: '))
    num2 = float(input('Informe o outro numero: '))
    resultado = soma(num1,num2)
    print(resultado)