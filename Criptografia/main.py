# -*- coding: utf-8 -*-
# Importações
import random
import math


# Pedir a mensagem que será encriptada
# , encoding="utf-8" Faz o código ler o arquivo em UTF-8
with open('D:\\CriptografiaPython\\Criptografia\\msg.criptografar.txt', 'r', encoding="utf-8") as arquivo:
    texto_base = arquivo.read()


# Verifica se as chaves são valores primos
def verificar_primos(number, y=5):
    # Faz a verificação para ver se não é 1, 2 ou 3 pois já são primos
    if number <= 1:
        return False
    if number <= 3:
        return True

    # Loops que vai testar se o valor é primo através do teste de Miller Rabin
    # O while faz divisões com resto 2 até que o D seja um numero impar
    r, d = 0, number - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for Miller in range(y):
        # A variável randomiza e recebe um numero no intervalo de 2, "number" -2 um valor ente -1 e 1
        randomizado = random.randint(2, number - 2)
        x = pow(randomizado, d, number)
        if x == 1 or x == number - 1:
            continue
        for Rabin in range(r - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break
        else:
            return False
    return True


# Gera números aleatórios em baseados em bits
def gerar_primo(bits):
    while True:
        numero = random.getrandbits(bits)
        # Faz a verificação para ver se o numero não é primo
        if numero % 2 != 0 and verificar_primos(numero):
            return numero


# Numero de primero em bits formular de acordo com a necessidade
bits = 8
# Variáveis que vão receber os primos
chave_P = gerar_primo(bits)
chave_Q = gerar_primo(bits)
# Mostra na tela ambos os primos
print(f"Número primo P com {bits} bits: {chave_P}")
print(f"Número primo Q com {bits} bits: {chave_Q}")


# Calcula o valor de N
# Mostra a chave N e chama a função lambda
chave_N = ((lambda p, q: p*q)(chave_P, chave_Q))
print(f"O valor de N é: {chave_N}")

# Abre o arquivo para edição ou cria
with open('D:\\CriptografiaPython\\Criptografia\\dados\\chave_N.txt', 'w', encoding="utf-8") as chave_N_arquivo:
    # Abre o arquivo e escreve dentro
    chave_N_arquivo.write(str(chave_N))
chave_N_arquivo.close()


# Calcula o valor de Z usando a função lambda
chave_Z = ((lambda p, q: (p-1)*(q-1))(chave_P, chave_Q))
# Mostra a chave Z
print(f"O valor de Z é: {chave_Z}")


# Calcula a chave E
def calcular_E(z):
    # O valor para E é 65537
    e = 65537
    # Garante que E seja coprimo com Z
    # gcd é uma função que procura o máximo divisor comum dentre dois valores
    while math.gcd(e, z) != 1:
        e = random.randint(2, z - 1)
    return e


# Chama a função para encontrar o expoente de cifragem E
chave_E = calcular_E(chave_Z)
print(f"O valor de E é: {chave_E}")


# Calcula o inverso modular
# usando o algoritmo de Euclides Estendido
def inverso_modulo(z, e):

    if e == 0:
        return (z, 1, 0)
    else:
        g, x, n = inverso_modulo(e, z % e)
        return (g, n, x - (z // e) * n)


# Calcula a chave D usando o algoritmo de Euclides Estendido
def calcular_D(z, e):
    # Formação da tupla para mostrar apenas o numero do meio e ignorar os outros dois valores
    _, d, _ = inverso_modulo(e, z)
    # Calcula o modulo desse valor
    d = (d + z) % z
    return d


# Mostra a chave D
chave_D = calcular_D(chave_Z, chave_E)
print(f"O valor de D é: {chave_D}")
# Transforma em string o valor
chave_D_str = str(chave_D)
# Abre o arquivo ou cria
with open('D:\\CriptografiaPython\\Criptografia\\dados\\chave_D.txt', 'w', encoding="utf-8") as chave_D_arquivo:
    # Abre o arquivo e escreve dentro
    chave_D_arquivo.write(chave_D_str)
chave_D_arquivo.close()


# Converte a mensagem com a função ord() para Código Padrão Americano
numeros = [ord(caractere) for caractere in texto_base]


# Criptografa
texto_cifra = [(numero ** chave_E) % chave_N for numero in numeros]


# Essa parte transforma a lista texto_cifra em uma string e já separa os valores com espaço
texto_cifra_str = ' '.join(map(str, texto_cifra))


# Abre o arquivo e escreve a mensagem dentro
with open('D:\\CriptografiaPython\\Criptografia\\dados\\msg.criptografada.txt', 'w', encoding="utf-8") as msg_cripto:
    # Abre ou cria o arquivo e coloca a mensagem
    msg_cripto.write(texto_cifra_str)
# Fecha o arquivo
msg_cripto.close()
