import sys
from PyQt5 import QtCore, QtGui, QtWidgets,sip

from Ellipsometer import four_step
from Ui_main import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.D0_text.setText('0')
        self.ui.D90_text.setText('0')
        self.ui.D180_text.setText('0')
        self.ui.D270_text.setText('0')
        self.ui.operation.clicked.connect(self.operation)
    def operation(self):
        I0 = float(self.ui.D0_text.toPlainText())
        I90 =float(self.ui.D90_text.toPlainText())
        I180 =float(self.ui.D180_text.toPlainText())
        I270 =float(self.ui.D270_text.toPlainText())
        
        sample = four_step(I0,I90,I180,I270)
        delta = str(round(sample.delta(),2))+'°'
        psi = str(round(sample.psi(),2))+'°'
        self.ui.deltaValue.setText(delta)
        self.ui.psiValue.setText(psi)
if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    window = mywindow()
    window.show()
    sys.exit(app.exec_())