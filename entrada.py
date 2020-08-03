#Still need to implement a way to parse fractions correctly, like -1/3

def confirmaSeFloat(valor):
  try:
    float(valor)
    return True
  except ValueError:
    return False


class inputStream:

  def __init__(self, operacoesValidas):
    self.operacoesValidas = operacoesValidas
    self.inputStream = []

  def recebeStreamEntrada(self):
    stringEntrada = input(">")
    self.inputStream = stringEntrada.split()

  def separaNumeroDeOperador(self):
    listaNumeros = []
    listaOperadores = []

    for item in self.inputStream:
      if item in self.operacoesValidas:
        listaOperadores.append(item)
      elif confirmaSeFloat(item):
        listaNumeros.append(float(item))
      else:
        print("Erro: " + item + " não é uma entrada válida")

    return listaNumeros, listaOperadores