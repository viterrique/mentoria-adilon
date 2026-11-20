# 1 - O que é um algoritimo?
# 2 - Variaveis

texto_string = "Hello World"
numero_int = 10
numero_float = 3.14
verdadeiro_boolean = True
falso_boolean = False

# 3 - I/O

texto_digitado = input("Digite algo: ")
print(texto_digitado)

# 4 - Operadores e expressoes

soma = numero_int+numero_float
print(f"soma: {soma}")
subtracao = numero_int-numero_float
print(f"subtracao: {subtracao}")
multiplicacao = numero_int*numero_float
print(f"multiplicacao: {multiplicacao}")
divisao = numero_int/numero_float
print(f"divisao: {divisao}")
potencia = numero_int**numero_float
print(f"potencia: {potencia}")
porcentagem = numero_int%numero_float
print(f"porcentagem: {porcentagem}")

maior_que = numero_int>numero_float
print(f"maior_que: {maior_que}")
menor_que = numero_int<numero_float
print(f"menor_que: {menor_que}")
maior_igual_que = numero_int>=numero_float
print(f"maior_igual_que: {maior_igual_que}")
menor_igual_que = numero_int<=numero_float
print(f"menor_igual_que: {menor_igual_que}")

# 5 - Condicionais

teste_boolean = True
print(f"comparacao: {teste_boolean == True}")

# and = true, se todos os membros da comparacao forem verdadeiros
# and = false, se houver pelo menos um membro falso na comparacao

and_boolean = verdadeiro_boolean and teste_boolean
print(f"comparacao de and: {and_boolean}")

# or = true, se pelo menos um membro da comparacao for verdadeiro
# or = false, se todos os membros da comparacao forem falsos

or_boolean = falso_boolean or teste_boolean
print(f"comparacao de or: {or_boolean}")

# Desafio 1

# Faça um programa para cadastro de usuários.
# Ele deve obedecer os seguintes requisitos:

# 1 - O usuário deve informar o nome
# 2 - O usuário deve informar o rg
# 3 - O usuário deve informar a idade

# 4 - Após cada resposta do usuário deve retornar
# uma mensagem para indicar que foi registrado
# com sucesso. Ex: "Nome registrado com sucesso!"

# 5 - Deve fazer a comparacao da idade:
# 5.1 - Se a idade for maior ou igual a 60, deve
# guardar "Idoso" em uma variavel
# 5.2 - Se a idade for maior ou igual a 18, deve
# guardar "Adulto" em uma variavel
# 5.3 - Se a idade for maior ou igual a 13, deve
# guardar "Adolescente" em uma variavel
# 5.3 - Se a idade for menor que 13, deve
# guardar "Criança" em uma variavel

# 6 - Deve exibir o registro do usuário assim:
'''
    Usuário registrado!
    
    Nome: x
    RG: y
    Grupo etario: z 
'''