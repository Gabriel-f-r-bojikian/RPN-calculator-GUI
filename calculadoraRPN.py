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
    bufferNumeros, bufferOperadores = self.separaNumeroDeOperador(entrada)
    print("Numeros: ")
    print(bufferNumeros)
    print("Operadores: ")
    print(bufferOperadores)
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
      print("Operadores do loop: ")
      print(self.pilhaDeOperacoes)
      if not len(self.pilhaDeOperacoes) == 0:
        operacao = self.pilhaDeOperacoes.pop(0)
      else:
        break
      
      if not len(self.pilhaDeNumeros) == 0:
        valorDireito = self.pilhaDeNumeros.pop()
      else:
        #raise Exception("Pilha vazia")
        break
      
      if not len(self.pilhaDeNumeros) == 0:
        valorEsquerdo = self.pilhaDeNumeros.pop()
      else:
        #print("Erro: Numero insuficiente de argumentos")
        self.pilhaDeNumeros.append(valorDireito)
        break

      resultado = operacoes.fazContaIndividual(valorEsquerdo, valorDireito, operacao)
      self.pilhaDeNumeros.append(resultado)

      #print("\t= ", resultado, "\n")

  def getResultado(self):
    if len(self.pilhaDeNumeros) > 0:
      return self.pilhaDeNumeros[len(self.pilhaDeNumeros) - 1]
    else:
      return -3.14

  def loopPrincipal(self):
    while True:
      print("")
      print(self.pilhaDeNumeros)
      entrada = input('>')
      numeros, operadores = self.recebeInputDoUsuario(entrada)

      self.montaPilhaNumeros(numeros)
      self.montaPilhaOperacoes(operadores)
      
      self.fazContas()

def confirmaSeFloat(valor):
  try:
    float(valor)
    return True
  except ValueError:
    return False


if __name__ == '__main__':
  calc = calculadoraRPN()
  calc.loopPrincipal()