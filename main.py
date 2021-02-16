import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

# mgf ui
import mgf_qt_ui.ui_py.mgf_main as mgf_qt_ui_main
import mgf_qt_event.mgf_events as mgf_qt_events


from urllib.parse import urlparse

url = 'https://blog.csdn.net/qq_28877125/article/details/81409748'



# main
if __name__ == '__main__':
    dest_str = urlparse(url)
    # print(dict(dest_str))

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    # mgf MainWindow init
    mgf_ui = mgf_qt_ui_main.Ui_MainWindow()
    mgf_ui.setupUi(MainWindow)

    # mgf events init
    mgf_events = mgf_qt_events.mgf_events_class(mgf_ui)

    MainWindow.show()
    sys.exit(app.exec_())
