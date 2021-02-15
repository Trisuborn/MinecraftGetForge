import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

# mgf ui
import mgf_qt_ui.ui_py.mgf_main as mgf_ui_main

def mgf_init(main_window):
    mgf_ui = mgf_ui_main.Ui_MainWindow()
    mgf_ui.setupUi(main_window)

    mgf_ui.textBrowser.clear()
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")
    mgf_ui.textBrowser.append("<a href=\"https://github.com/Trisuborn/MinecraftGetForge\">项目</a>")


# main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    mgf_init(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
