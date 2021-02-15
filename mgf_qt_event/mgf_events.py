
# mgf ui
import mgf_qt_ui.ui_py.mgf_main as mgf_ui_main

default_forge_ver1 = '1'
default_forge_ver2 = '12'
default_forge_ver3 = '2'
default_forge_ver  = default_forge_ver1+ "." +default_forge_ver2+ "." +default_forge_ver3
forge_ver1 = ''
forge_ver2 = ''
forge_ver3 = ''
forge_ver  = ''

class mgf_events_class():
    def __init__(self, main_ui = mgf_ui_main.Ui_MainWindow()):
        print("Events handlers initializing...")
        self.main_ui = main_ui
        self.btn_sure_links();
        print("Events handlers initialized done.")

    # btn_sure_events
    def btn_sure_links(self):
        print("btn sure events links.")
        self.main_ui.btn_sure.clicked.connect(self.btn_sure_events)
    def btn_sure_events(self):
        # print("btn_sure_events")
        forge_ver1 = self.main_ui.lineEdit_ver1.text()
        forge_ver2 = self.main_ui.lineEdit_ver2.text()
        forge_ver3 = self.main_ui.lineEdit_ver3.text()

        if (forge_ver1 and forge_ver2 and forge_ver3):
            forge_ver = forge_ver1 + "." + forge_ver2 + "." + forge_ver3
        else :
            forge_ver = default_forge_ver
        self.main_ui.label_ver.setText("当前选择版本: " + forge_ver)
