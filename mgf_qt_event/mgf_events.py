
# mgf ui
import mgf_qt_ui.ui_py.mgf_main as mgf_ui_main

class mgf_events_class():
    def __init__(self, main_ui = mgf_ui_main.Ui_MainWindow()):
        print("Events handlers initializing...")
        self.main_ui = main_ui
        self.btn_sure_links();
        print("Events handlers done.")

    # btn_sure_events
    def btn_sure_links(self):
        print("btn sure events links.")
        self.main_ui.btn_sure.clicked.connect(self.btn_sure_events)
    def btn_sure_events(self):
        print("btn_sure_events")

