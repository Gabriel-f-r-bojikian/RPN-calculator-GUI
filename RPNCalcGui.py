'''
This is a simple RPN Calculator made with Python and PyQt5
Done by: Gabriel Fernandes
Email: gabriel.f.r.bojikian@gmail.com

'''
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QPushButton
from functools import partial
import calculadoraRPN


class RPNCalcUi(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("RPN Calculator")
    self.masterLayout = QHBoxLayout() #Master layout for the program
    self.leftLayout = QVBoxLayout() #Layout for the keyboard and the input screen
    self.rightLayout = QVBoxLayout() #Layout for the stack display

    self._createInputWidget()
    self._createButtons()
    self._createStackDisplay()
    self._setUpLayouts()

    self.setLayout(self.masterLayout)

  def _createInputWidget(self):
    self.inputWidget = QLineEdit()
    self.inputWidget.setReadOnly(True)
    self.leftLayout.addWidget(self.inputWidget)


  def _createButtons(self):
    self.buttons = {}
    buttonsLayout = QGridLayout()
    self.buttons = {
      '^'         : (0, 0),
      'Switch'    : (0, 1),
      'Backspace' : (0, 2),
      'Enter'     : (0, 3),
      '7'         : (1, 0),
      '8'         : (1, 1),
      '9'         : (1, 2),
      '/'         : (1, 3),
      '4'         : (2, 0),
      '5'         : (2, 1),
      '6'         : (2, 2),
      'x'         : (2, 3),
      '1'         : (3, 0),
      '2'         : (3, 1),
      '3'         : (3, 2),
      '-'         : (3, 3),
      '0'         : (4, 0),
      '.'         : (4, 1),
      'Space'     : (4, 2),
      '+'         : (4, 3),
    }

    for text, pos in self.buttons.items():
      self.buttons[text] = QPushButton(text)
      buttonsLayout.addWidget(self.buttons[text], pos[0], pos[1])

    self.leftLayout.addLayout(buttonsLayout)

  def _createStackDisplay(self):
    self.stackLabels = []
    for x in range(0, 5):
      self.stackLabels.append(QLabel(text = "Placeholder"))
      self.rightLayout.addWidget(self.stackLabels[x])

  def _setUpLayouts(self):
    self.masterLayout.addLayout(self.leftLayout)
    self.masterLayout.addLayout(self.rightLayout)
  
  def setDisplaytext(self, message):
    self.inputWidget.setText(message)
    self.inputWidget.setFocus()
  
  def getDisplayText(self):
    return self.inputWidget.text()

  def clearDisplay(self):
    self.inputWidget.setText('')


class CalculatorController:
  def __init__(self, view, calc):
    self._view = view
    self._calculator = calc
    self._connectSignals()

  def _buildExpression(self, sub_exp):
    expression = self._view.getDisplayText() + sub_exp
    self._view.setDisplaytext(expression)
  
  def _connectSignals(self):
    for btnText, btn in self._view.buttons.items():
      if btnText not in {'Backspace', 'Enter', 'Space', 'Switch'}:
        btn.clicked.connect(partial(self._buildExpression, btnText))

    self._view.buttons['Space'].clicked.connect(partial(self._buildExpression, ' '))
    self._view.buttons['Enter'].clicked.connect(partial(self._evaluateExpression))
    self._view.inputWidget.returnPressed.connect(partial(self._evaluateExpression))
    #self._view.buttons['Enter'].clicked.connect(partial(self._displayResult))


  def _evaluateExpression(self):
    print("I'm looping here")
    entrada = self._view.getDisplayText()
    self._calculator.recebeInputDoUsuario(entrada)
    self._calculator.fazContas()
    
    self._displayResult()
    
  def _displayResult(self):
    resultado = self._calculator.getResultado()
    self._view.setDisplaytext( str(resultado) )
    self._updateStackWidget()
    self._view.inputWidget.setText('')

  def _updateStackWidget(self):
    for index in range(0, 5):
      if index < self._calculator.getTamanhoPilhaDeNumeros():
        self._view.stackLabels[index].setText( str(self._calculator.pilhaDeNumeros[index]) )




if __name__ == '__main__':
  app = QApplication(sys.argv)
  win = RPNCalcUi()
  win.show()

  calculadora = calculadoraRPN.calculadoraRPN()
  CalculatorController(view = win, calc = calculadora)

  sys.exit(app.exec_())