# -*- coding: utf-8 -*-
# Recebe a entrada do usuário para chave_N
chave_N = int(input("Digite o valor para chave_N: "))


# Recebe a entrada do usuário para chave_D
chave_D = int(input("Digite o valor para chave_D: "))


# Pegando dados da mensagem do usuário em armazenando tem texto cifra (como uma lista de números)
texto_cifra = input("Digite os valores da mensagem separados por espaço: ")


# Convertendo os valores para inteiros e dividindo a entrada com espaços
# A parte int, texto_cifra.split() transforma uma grande string em pequenas ou seja ramifica
# A função map vai fazer todos itens da lista virar int e logo em seguida vem o list que transforma os valores numeros em uma lista, porem para funcionar tem que colocar os valores em espaço
# Essa parte tb trata os erros do código
try:
    texto_cifra = list(map(int, texto_cifra.split()))
except ValueError:
    print("Entre com valores inteiros separado por espaço")
    exit()


# Descriptografa
# Necessário as duas chaves D e N e a mensagem separa por espaços
# Função chr busca o valor Unicode de cada numero
mensagem_descriptografada = [chr((numero ** chave_D) % chave_N) for numero in texto_cifra]
# O join é uma função que junta os elementos sequenciais fornecidos pelo usuário e como exemplo usa '' para falar que é um string vazia e dentro dela ele coloca os valores
mensagem_original = ''.join(mensagem_descriptografada)


# Mostra a mensagem
print("\nMensagem descriptografada:", mensagem_original)
