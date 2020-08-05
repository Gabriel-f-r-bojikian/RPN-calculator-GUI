from functools import partial
import calculadoraRPN

class CalculatorController:
  def __init__(self, view, calc):
    self.janela = view
    self.calculadora = calc
    self.conectaSinaisDosBotoes()

  def constroiExpressaoNaTela(self, sub_exp):
    expression = self.janela.getDisplayText() + sub_exp
    self.janela.setDisplaytext(expression)
  
  def conectaSinaisDosBotoes(self):
    for textoDoBotao, botao in self.janela.buttons.items():
      if textoDoBotao not in {'Backspace', 'Enter', 'Space', 'Switch'}:
        botao.clicked.connect(partial(self.constroiExpressaoNaTela, textoDoBotao))

    self.janela.buttons['Space'].clicked.connect(partial(self.constroiExpressaoNaTela, ' '))
    self.janela.buttons['Enter'].clicked.connect(partial(self.avaliaExpressao))
    self.janela.inputWidget.returnPressed.connect(partial(self.avaliaExpressao))
    self.janela.buttons['Backspace'].clicked.connect(partial(self.apagaChar))
    self.janela.buttons['Switch'].clicked.connect(partial(self.trocaPosPilha))


  def avaliaExpressao(self):
    entrada = self.janela.getDisplayText()
    self.calculadora.recebeInputDoUsuario(entrada)
    self.calculadora.fazContas()
    
    self.mostraResultado()
    
  def mostraResultado(self):
    resultado = self.calculadora.getResultado()
    self.janela.setDisplaytext( str(resultado) )
    self.atualizaWidgetDaPilha()
    self.janela.inputWidget.setText('')


  def apagaChar(self):
    textoDaJanela = self.janela.getDisplayText()
    if len(textoDaJanela) > 0:
      textoDaJanela = textoDaJanela[:-1]
      self.janela.setDisplaytext(textoDaJanela)
    
    elif self.calculadora.getTamanhoPilhaDeNumeros() > 0:
      self.calculadora.pilhaDeNumeros.pop()

    self.atualizaWidgetDaPilha()

  def trocaPosPilha(self):
    self.calculadora.trocaPosicaoDosUltimosDaPilha()
    self.atualizaWidgetDaPilha()

  def atualizaWidgetDaPilha(self):
    
    self.limpaWidgetDaPilha()

    comprimentoDaPilha = self.calculadora.getTamanhoPilhaDeNumeros()

    for index in range(0, 5):
      if index < comprimentoDaPilha:
        labelText = str(index) + ': ' + str(self.calculadora.pilhaDeNumeros[comprimentoDaPilha - index - 1])
        self.janela.stackLabels[index].setText( labelText )


  def limpaWidgetDaPilha(self):
    for index in range(0, 5):
      self.janela.stackLabels[index].setText( str(index) + ': ' )