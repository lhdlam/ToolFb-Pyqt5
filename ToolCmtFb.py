from asyncio import sleep
import sys
from PyQt5 import QtWidgets
from cmt import facebookCmt
from login import data
from selenium import webdriver
from new_giaodien_UI import Ui_MainWindow
import threading
# import pathlib
# path = pathlib.Path(__file__).parent.resolve()

class CmtFacebook:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.my_ui_control()

        MainWindow.show()
        sys.exit(app.exec_())

    def my_ui_control(self):
        self.ui.lbl_thongbao.setText('')
        self.ui.btn_login.clicked.connect(self.on_login)
        self.ui.btn_start.clicked.connect(self.on_start)
        self.ui.btn_stop.clicked.connect(self.on_stop)

    def on_login(self):
        self.ui.lbl_thongbao.setText('Đang chạy login')
        self.path = self.ui.line_folder.text()
        self.soTab = self.ui.line_tab.text()
        self.soLuong = int(self.soTab)
        threads = []
        for l in range(self.soLuong):
            threads += [threading.Thread(target=data, args=(l, self.path),)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        print("end daluong")

    def on_start(self):
        self.ui.lbl_thongbao.setText('Bắt đầu comment')
        self.path = self.ui.line_folder.text()
        self.soTab = int(self.ui.line_tab.text())
        self.soCmt = int(self.ui.line_cmt.text())
        self.linkFb = (self.ui.line_link.text())
        threads = []
        for l in range(self.soTab):
            threads += [threading.Thread(target=facebookCmt,
                                         args=(l, self.soCmt, self.linkFb, self.path),)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        print("end daluong")
        self.ui.lbl_thongbao.setText('Comment xong')

    def on_stop(self):
        print('click stop')
        exit()
        self.ui.lbl_thongbao.setText('Đã dừng')


if __name__ == "__main__":
    cmt_facebook = CmtFacebook()
