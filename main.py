import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

# mgf
import mgf_qt_ui.ui_py.mgf_main as mgf_qt_ui_main
import mgf_qt_event.mgf_events as mgf_qt_events
import mgf_web.mgf_web as mgf_web

# main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    # mgf MainWindow init
    mgf_ui = mgf_qt_ui_main.Ui_MainWindow()
    mgf_ui.setupUi(MainWindow)

    # mgf events init
    mgf_events = mgf_qt_events.mgf_events_class(mgf_ui)

    MainWindow.show()
    sys.exit(app.exec_())
