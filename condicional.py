# > Estrutura condicionais

idade = 20

if idade >= 18:
    print('você é maior de idade')
else: 
    print('você é menos de idade')
    
"""
    imagine que vocÊ queira imprimir "aprovado(a)", caso o estudante tenha ma média superior ou igual a 7, e "reprovado", caso a média seja inferior a 7.
    """
    
media = float(nput('informe a média do estudante:'))

if media >= 7:
    print('você foi aprovado(a)')
elif media >= 5:
    print('recuperação') 
else:
    print('você foi reprovado(a)')
    
media = 10
prsenca = 100

if media >= 7 and presenca >= 70:
    print('aprovado')

else:
    print('reprovado')