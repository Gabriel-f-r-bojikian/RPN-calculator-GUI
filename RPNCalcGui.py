'''
This is a simple RPN Calculator made with Python and PyQt5
Done by: Gabriel Fernandes
Email: gabriel.f.r.bojikian@gmail.com

'''
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QPushButton
import controler

class RPNCalcUi(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("RPN Calculator")
    self.masterLayout = QHBoxLayout() #Master layout for the program
    self.leftLayout = QVBoxLayout() #Layout for the keyboard and the input screen
    self.rightLayout = QVBoxLayout() #Layout for the stack display

    self.criaWidgetEntrada()
    self.criaBotoes()
    self.criaDisplayPilha()
    self._setUpLayouts()

    self.setLayout(self.masterLayout)

  def criaWidgetEntrada(self):
    self.inputWidget = QLineEdit()
    self.leftLayout.addWidget(self.inputWidget)


  def criaBotoes(self):
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
      '*'         : (2, 3),
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

  def criaDisplayPilha(self):
    self.stackLabels = []
    for x in range(0, 5):
      self.stackLabels.append(QLabel(text = str(x) + ': '))
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


if __name__ == '__main__':
  app = QApplication(sys.argv)
  win = RPNCalcUi()
  win.show()

  calculadora = controler.calculadoraRPN.calculadoraRPN()
  controler.CalculatorController(view = win, calc = calculadora)

  sys.exit(app.exec_())