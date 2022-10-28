# import
import os
import numpy as np

# limpta tela
os.system("cls || clear") or None

# atribuição dos arquivos de texto para variáveis
dadosAnos = 'anos.txt'
dadosAltura = 'altura.txt'

# extração dos valores dos arquivos txt para criar arrays
vetorAltura = np.loadtxt(dadosAltura, dtype='float')
vetorAnos = np.loadtxt(dadosAnos, dtype='float')

# index dos anos
indexAnos = np.where(vetorAnos[(vetorAnos > 1998) & (vetorAnos < 2005)])

# encontrar valores de altura pelo index dos anos
valoresAltura = vetorAltura[np.where(vetorAltura[(vetorAnos > 1998) & (vetorAnos < 2005)])]

# encontrar a quantidade de itens do indexAnos
quantidadeAnos = np.size(indexAnos)

# cálculo da média
# soma das alturas
somaAlturas = np.sum(valoresAltura)

# cálculo da média
media = somaAlturas / quantidadeAnos

# output media
print(f"A soma das alturas é de {somaAlturas} e a quantidade de anos é de {quantidadeAnos}."
    f" Com isso, fazendo a média (soma das alturas / soma da quantidade de anos), o resulta é {media}.")
