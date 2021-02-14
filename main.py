import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

# mgf ui
import mgf_qt_ui.ui_py.mgf_main as mgf_ui_main

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mgf_ui_main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
