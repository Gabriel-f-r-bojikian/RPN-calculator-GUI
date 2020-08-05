#Calculadora implementada como uma classe. As operações aritméticas básicas e potenciação foram implementadas
import operacoes

class calculadoraRPN:
  def __init__(self):
    self.operadoresAceitos = operacoes.operadoresAceitos
    self.pilhaDeNumeros = []
    self.pilhaDeOperacoes = []


  def recebeInputDoUsuario(self, entrada):
    bufferNumeros = []
    bufferOperadores = []
    bufferEntrada = entrada.split(' ')
    bufferNumeros, bufferOperadores = self.separaNumeroDeOperador(bufferEntrada)
    self.montaPilhaNumeros(bufferNumeros)
    self.montaPilhaOperacoes(bufferOperadores)


  def separaNumeroDeOperador(self, entrada):
    listaNumeros = []
    listaOperadores = []

    for item in entrada:
      if item in self.operadoresAceitos:
        listaOperadores.append(item)
      elif confirmaSeFloat(item):
        listaNumeros.append(float(item))

    return listaNumeros, listaOperadores


  def montaPilhaNumeros(self, listaDeNumeros):
    for numero in listaDeNumeros:
      self.pilhaDeNumeros.append(numero)

  def getTamanhoPilhaDeNumeros(self):
    return len(self.pilhaDeNumeros)

  def montaPilhaOperacoes(self,listaDeOperacoes):
    for operacao in listaDeOperacoes:
      self.pilhaDeOperacoes.append(operacao)

  def fazContas(self):
    valorDireito = 0
    valorEsquerdo = 0
    while len(self.pilhaDeOperacoes) > 0:
      operacao = self.pilhaDeOperacoes.pop(0)
      
      if not len(self.pilhaDeNumeros) == 0:
        valorDireito = self.pilhaDeNumeros.pop()
      else:
        break #Chega aqui se pilha está vazia
      
      if not len(self.pilhaDeNumeros) == 0:
        valorEsquerdo = self.pilhaDeNumeros.pop()
      else:
        #print("Erro: Numero insuficiente de argumentos")
        self.pilhaDeNumeros.append(valorDireito)
        break #Chega aqui se pilha está vazia

      resultado = operacoes.fazContaIndividual(valorEsquerdo, valorDireito, operacao)
      self.pilhaDeNumeros.append(resultado)


  def getResultado(self):
    if len(self.pilhaDeNumeros) > 0:
      return self.pilhaDeNumeros[len(self.pilhaDeNumeros) - 1]
    else:
      return -3.14

  def trocaPosicaoDosUltimosDaPilha(self):
    if self.getTamanhoPilhaDeNumeros() > 1:
      valor1 = self.pilhaDeNumeros.pop()
      valor2 = self.pilhaDeNumeros.pop()
      self.pilhaDeNumeros.append(valor1)
      self.pilhaDeNumeros.append(valor2)
      

def confirmaSeFloat(valor):
  try:
    float(valor)
    return True
  except ValueError:
    return False