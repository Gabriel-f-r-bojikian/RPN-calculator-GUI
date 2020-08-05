'''
This is a simple RPN Calculator made with Python and PyQt5
Done by: Gabriel Fernandes
Email: gabriel.f.r.bojikian@gmail.com

'''

from RPNCalcGui import *

def main():
  app = QApplication(sys.argv)
  win = RPNCalcUi()
  win.show()

  calculadora = controler.calculadoraRPN.calculadoraRPN()
  controler.CalculatorController(view = win, calc = calculadora)

  sys.exit(app.exec_())


if __name__ == '__main__':
  main()