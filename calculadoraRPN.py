#Calculadora implementada como uma classe. As operações aritméticas básicas e potenciação foram implementadas
import operacoes
import entrada

class calculadoraRPN:
  def __init__(self):
    self.operadoresAceitos = operacoes.operadoresAceitos
    self.pilhaDeNumeros = []
    self.pilhaDeOperacoes = []
    self.fluxoEntrada = entrada.inputStream(self.operadoresAceitos)

  def recebeInputDoUsuario(self):
    self.fluxoEntrada.recebeStreamEntrada()
    numeros, operadores = self.fluxoEntrada.separaNumeroDeOperador()
    return numeros, operadores

  def montaPilhaNumeros(self, listaDeNumeros):
    for numero in listaDeNumeros:
      self.pilhaDeNumeros.append(numero)

  def montaPilhaOperacoes(self,listaDeOperacoes):
    for operacao in listaDeOperacoes:
      self.pilhaDeOperacoes.append(operacao)

  def fazContas(self):
    valorDireito = 0
    valorEsquerdo = 0
    while len(self.pilhaDeOperacoes) > 0:
      
      if not len(self.pilhaDeOperacoes) == 0:
        operacao = self.pilhaDeOperacoes.pop(0)
      else:
        break
      
      if not len(self.pilhaDeNumeros) == 0:
        valorDireito = self.pilhaDeNumeros.pop()
      else:
        print("Erro: Pilha vazia")
        break
      
      if not len(self.pilhaDeNumeros) == 0:
        valorEsquerdo = self.pilhaDeNumeros.pop()
      else:
        print("Erro: Numero insuficiente de argumentos")
        self.pilhaDeNumeros.append(valorDireito)
        break

      resultado = operacoes.fazContaIndividual(valorEsquerdo, valorDireito, operacao)
      self.pilhaDeNumeros.append(resultado)

      print("\t= ", resultado, "\n")

  def loopPrincipal(self):
    while True:
      print("")
      print(self.pilhaDeNumeros)

      numeros, operadores = self.recebeInputDoUsuario()

      self.montaPilhaNumeros(numeros)
      self.montaPilhaOperacoes(operadores)
      
      self.fazContas()


if __name__ == '__main__':
  calc = calculadoraRPN()
  calc.loopPrincipal()