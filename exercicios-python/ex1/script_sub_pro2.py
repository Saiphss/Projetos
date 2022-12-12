#Definindo uma função (retorna valores).
#Estudo sobre Parâmetros.
def taximetro(distancia,multiplicador = 1): #Cabeçalho da função com dois parâmetros formais.
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor
pagamento = taximetro(3.5) #Chamada da função taximetro com um parâmetro real.
print(pagamento)