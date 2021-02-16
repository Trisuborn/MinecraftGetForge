
from PyQt5.QtCore import QTimer

# mgf ui
import mgf_qt_ui.ui_py.mgf_main as mgf_ui_main

github_hint = "<a href='https://github.com/Trisuborn/MinecraftGetForge'>VER 4.0 GitHub地址</a>"

default_forge_ver1 = '1'
default_forge_ver2 = '12'
default_forge_ver3 = '2'
default_forge_ver  = default_forge_ver1+ "." +default_forge_ver2+ "." +default_forge_ver3
forge_ver1 = default_forge_ver1
forge_ver2 = default_forge_ver2
forge_ver3 = default_forge_ver3
forge_ver  = default_forge_ver

class mgf_events_class():
    def __init__(self, main_ui = mgf_ui_main.Ui_MainWindow()):
        print("Events handlers initializing...")
        self.main_ui = main_ui
        self.info_timer()
        self.btn_sure_links()
        self.lineEdit_ver_links()
        print("Events handlers initialized done.")

    def get_version(self):
        forge_ver1 = self.main_ui.lineEdit_ver1.text()
        forge_ver2 = self.main_ui.lineEdit_ver2.text()
        forge_ver3 = self.main_ui.lineEdit_ver3.text()

        if (forge_ver1 and forge_ver2 and forge_ver3):
            forge_ver = forge_ver1 + "." + forge_ver2 + "." + forge_ver3
        else :
            forge_ver = default_forge_ver
        self.main_ui.label_ver.setText("当前选择版本: " + forge_ver)

    # btn_sure_events
    def btn_sure_links(self):
        print("btn sure events links.")
        self.main_ui.btn_sure.clicked.connect(self.btn_sure_clicked)
    def btn_sure_clicked(self):
        self.get_version()

    # lineEdit_ver_events
    def lineEdit_ver_links(self):
        print("lineEdit ver links.")
        self.main_ui.lineEdit_ver1.textChanged.connect(self.lineEdit_ver_changes)
        self.main_ui.lineEdit_ver2.textChanged.connect(self.lineEdit_ver_changes)
        self.main_ui.lineEdit_ver3.textChanged.connect(self.lineEdit_ver_changes)
    def lineEdit_ver_changes(self):
        self.get_version()

    def info_timer(self):
        self.cnt = 0
        self.info_flag = 0
        self.timer = QTimer() #初始化一个定时器
        self.timer.timeout.connect(self.timer_operate) #计时结束调用operate()方法
        self.timer.start(1000) #设置计时间隔并启动
    def timer_operate(self):
        self.cnt += 1
        if (self.cnt%5 == 0):
            self.info_flag = 0 if (self.info_flag) else 1
            if (self.info_flag == 0):
                self.main_ui.label_github.setText(github_hint)
        if (self.info_flag == 1):
            self.main_ui.label_github.setText('已运行时间: ' + str(self.cnt) + '秒')
