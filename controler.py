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
    #Variables that will be used for error handling
    houveErroDeEntrada = False
    stringsErrados = []

    #Getting the input
    entrada = self.janela.getDisplayText()
    houveErroDeEntrada, stringsErrados = self.calculadora.recebeInputDoUsuario(entrada)
    
    #Requesting the calculator to do the math
    if not houveErroDeEntrada:
      self.calculadora.fazContas()
    else:
      self.janela.showInputPopUpErrorMessage(stringsErrados)
    
    self.mostraResultado() #Displaying result in the stack
    
  def mostraResultado(self):
    resultado = self.calculadora.getResultado()
    self.janela.setDisplaytext( str(resultado) )
    self.atualizaWidgetDaPilha()
    self.janela.inputWidget.setText('')


  #This function either works as a backspace for the display or deletes the last
  #item in the stack
  def apagaChar(self):
    textoDaJanela = self.janela.getDisplayText()
    if len(textoDaJanela) > 0: #If there is any text in the display
      textoDaJanela = textoDaJanela[:-1] #Deletes the last item in the text
      self.janela.setDisplaytext(textoDaJanela)
    
    elif self.calculadora.getTamanhoPilhaDeNumeros() > 0:
      self.calculadora.pilhaDeNumeros.pop()

    self.atualizaWidgetDaPilha()

  #Changes the position of the last two items added to the stack
  def trocaPosPilha(self):
    self.calculadora.trocaPosicaoDosUltimosDaPilha()
    self.atualizaWidgetDaPilha()

  #This function handles updating the stack widget
  def atualizaWidgetDaPilha(self):
    self.limpaWidgetDaPilha()

    comprimentoDaPilha = self.calculadora.getTamanhoPilhaDeNumeros()

    for index in range(0, 5):
      if index < comprimentoDaPilha:
        labelText = str(index) + ': ' + str(self.calculadora.pilhaDeNumeros[comprimentoDaPilha - index - 1])
        self.janela.stackLabels[index].setText( labelText )

  #This function clears the stack widget
  def limpaWidgetDaPilha(self):
    for index in range(0, 5):
      self.janela.stackLabels[index].setText( str(index) + ': ' )