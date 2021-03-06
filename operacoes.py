#All the mathematical operations are defined in this script

#List of accepted mathematical operations
operadoresAceitos = ["+", "-", "/", "%", "*", "^"]

#Handles the math evaluation
def fazContaIndividual(lvalue, rvalue, operacao):

  if operacao == "+":
    return soma(lvalue, rvalue)

  elif operacao == "-":
    return subtrai(lvalue, rvalue)

  elif operacao == "*":
    return multiplica(lvalue, rvalue)
  
  elif operacao == "/" or operacao == "%":
    return divide(lvalue, rvalue)

  elif operacao == "^":
    return elevaEsqueroAoDireito(lvalue, rvalue)

  else:
    return "Erro: operacao invalida"



def soma(lvalue, rvalue):
  return lvalue + rvalue



def subtrai(lvalue, rvalue):
  return lvalue - rvalue



def multiplica(lvalue, rvalue):
  return lvalue*rvalue



def divide(lvalue, rvalue):
  if rvalue != 0:
    return lvalue / rvalue
  else:
    return lvalue #Returns lvalue to the stack



def elevaEsqueroAoDireito(lvalue, rvalue):
  return lvalue**rvalue