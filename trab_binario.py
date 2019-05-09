binario = "" #variavel que começa em branco
num = float(input('Insira aqui seu numero para a conversao: ')) #usuario digitando o numero
while num > 0: #o numero precisa ser positivo
  if num % 2 == 0: #o numero precisa ser uma divisao inteira por 2 para receber o 0
    binario = '0'+ str(binario) #entao o 0 vai ser adicionado a string do binario
    num = num / 2 #assim, o numero vai se dividir exato por 2
  else:
    binario = '1' + str(binario) #como a divisao do numero nao vai ser exata, o binario recebe 1
    num = num - 1 #para efetuar a divisao, o numero deve se tornar par
    num = num / 2 #divisao
print(binario) #o numero convertido em binario aparece-rá na tela
