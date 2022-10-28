# Grupo: Ñ sei
# Membros: Aline Rezende e Thallonys
# Converte metros em pés e pés em metros

# import
import os

# limpa tela
os.system("cls || clear") or None

# função


def converter(valor, opcao):
    """Função que converter ou metros para pés ou pés para metros"""
    # metros para pés
    if opcao == 1:
        # cálculo
        metro = 3.281
        resultado = valor * metro

    # pés para metros
    elif opcao == 2:
        # cálculo
        pe = 0.3048
        resultado = valor * pe

    return resultado


# input
# menu
print('Escolha uma opção de conversão:\n'
      '|----------------------------|\n'
      '| 1 - Converte metros em pés |\n'
      '| 2 - Converte pés em metros |\n'
      '|----------------------------|')

opcao = int(input('Entre com a opção: '))

# if statement
if opcao == 1:
    # input
    metrosQuantidade = float(input('Entre com a quantidade de metros: '))

    # chamar função
    resultado = converter(metrosQuantidade, opcao)

    # output
    print(f'{metrosQuantidade} metro(s) equivale a {resultado} pés.')

elif opcao == 2:
    # input
    peQuantidade = float(input('Entre com a quantide de pés: '))

    # chamar função
    resultado = converter(peQuantidade, opcao)

    # output
    print(f'{peQuantidade} pé(s) equivale a {resultado} metros.')

else:
    # output
    print('Opção incorreta, mermão!')
