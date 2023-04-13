# > funções 

#1.0 que são funções e por que utilizá-las?

#funções que ja utilizamos anteriormente
"""
print() = imprimir uma mensagem (int, float, str) no console (terminal)
input() = retorna um dado informado pelo usuário (entrada padrão) e pode receber um string
len() = receb uam lista e retorna o tamanho dessa lista
max() = retorna o maior de uma lista
"""
#criação inicial

def saudacao():
    print('seja bem-vindo')
    print('é um prazer ter vocÊ fazendo esse curso')
    print('qual é o seu nome?')
    
saudacao()

#função com parâmetro

def saudacao(nome, curso):
    print(f'seja bem-vindo,(nome)')
    print(f'olá, é um prazer ter você fazendo parte do curso de (curso)')

saudacao('Aline melo, python')
saudacao('melo, javascript')

#função cm parâmetro defaut 

def saudacao(nome, curso = 'python'):
    print(f'seja bem vindo(nome)')
    print(f'olá e um prazer ter você fazendo parte do curso de (curso)')
saudacao('aline')

#funções com retorno

def soma(num1, num2):
    print('soma, =  num1 + num2')
soma(5, 7)

def soma(num1, num2):

    return num1 + num2
resultado = soma(5, 7)
print('o resultador da soma é', resultado)

def calculadora(num1, num2, operacao = '+'):
    if(operacao == '+'):
        return num1 + num2
    elif (operacao == '-'):
        return num1 + num1 + num2
    
resultado = calculadora(10,20)
print(resultado)