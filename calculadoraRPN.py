import operacoes

class calculadoraRPN:
  def __init__(self):
    self.operadoresAceitos = operacoes.operadoresAceitos
    self.pilhaDeNumeros = []
    self.pilhaDeOperacoes = []

  #Handles parsing the user input
  def recebeInputDoUsuario(self, entrada):
    #Buffers
    bufferNumeros = []
    bufferOperadores = []
    
    #Variables for error handling
    houveIgnorados = False
    ignorados = []
    
    #Setting up the buffers
    bufferEntrada = entrada.split(' ')
    bufferNumeros, bufferOperadores, houveIgnorados, ignorados = self.separaNumeroDeOperador(bufferEntrada)
    
    #Setting up the stacks
    self.montaPilhaNumeros(bufferNumeros)
    self.montaPilhaOperacoes(bufferOperadores)

    #Values returned for error handling purposes
    return houveIgnorados, ignorados

  #Separates numbers from operators and invalid entries
  def separaNumeroDeOperador(self, entrada):
    #Buffers
    listaNumeros = []
    listaOperadores = []
    
    #Variables for error handling
    houveIgnorados = False
    ignorados = []

    for item in entrada:
      if item in self.operadoresAceitos:
        listaOperadores.append(item) #Include operator to the stack
      elif confirmaSeFloat(item):
        listaNumeros.append(float(item)) #Include number to the stack
      else:
        houveIgnorados = True #Signals invalid entries 
        ignorados.append(item) #Records said invalid entries

    #Returning the number and operator buffers and the error handling variables
    return listaNumeros, listaOperadores, houveIgnorados, ignorados

  #Sets the number stack
  def montaPilhaNumeros(self, listaDeNumeros):
    for numero in listaDeNumeros:
      self.pilhaDeNumeros.append(numero)

  def getTamanhoPilhaDeNumeros(self):
    return len(self.pilhaDeNumeros)

  #Sets the operator stacks
  def montaPilhaOperacoes(self,listaDeOperacoes):
    for operacao in listaDeOperacoes:
      self.pilhaDeOperacoes.append(operacao)

  #Control flux for the calculator
  def fazContas(self):
    #Buffers
    valorDireito = 0
    valorEsquerdo = 0
    
    #Perform calculations until the operator stack is empty
    while len(self.pilhaDeOperacoes) > 0:
      operacao = self.pilhaDeOperacoes.pop(0)
      
      if not len(self.pilhaDeNumeros) == 0:
        valorDireito = self.pilhaDeNumeros.pop()
      else:
        break #Arrives here only if number stack is empty
      
      if not len(self.pilhaDeNumeros) == 0:
        valorEsquerdo = self.pilhaDeNumeros.pop()
      else:
        self.pilhaDeNumeros.append(valorDireito)
        break #Arrives here only if number stack is empty

      #Do the evaluation and push the result to the stack
      resultado = operacoes.fazContaIndividual(valorEsquerdo, valorDireito, operacao)
      self.pilhaDeNumeros.append(resultado)

  
  def getResultado(self):
    if len(self.pilhaDeNumeros) > 0:
      return self.pilhaDeNumeros[len(self.pilhaDeNumeros) - 1]
    else:
      return -9999999 #Unreasonable result

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