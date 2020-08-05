import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QPushButton, QMessageBox
import controler

class RPNCalcUi(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("RPN Calculator")
    self.masterLayout = QHBoxLayout() #Master layout for the program
    self.leftLayout = QVBoxLayout() #Layout for the keyboard and the input screen
    self.rightLayout = QVBoxLayout() #Layout for the stack display
    
    #Create buttons and displays
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
    #We will use a map to declare the buttons
    #The index is the button text and the tuple value indicates the position
    #of the button on the app keyboard
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

    #Creating the buttons based on the map
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

  def showInputPopUpErrorMessage(self, listaStringsErrados):
    mensagemDeErro = self.compoeMensagemDeErroDeEntrada(listaStringsErrados)
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText(mensagemDeErro)
    msg.setIcon(QMessageBox.Warning)

    x = msg.exec_()

  def compoeMensagemDeErroDeEntrada(self, listaStringsErrados):
    mensagemDeErro = "Error - The following entries are invalid:\n"
    for item in listaStringsErrados:
      mensagemDeErro += item
      mensagemDeErro += " "
    
    return mensagemDeErro
    
if __name__ == '__main__':
  app = QApplication(sys.argv)
  win = RPNCalcUi()
  win.show()

  calculadora = controler.calculadoraRPN.calculadoraRPN()
  controler.CalculatorController(view = win, calc = calculadora)

  sys.exit(app.exec_())