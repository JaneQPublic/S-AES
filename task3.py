from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QInputDialog

import sys

import aes


class Ui_Formbf(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Formbf, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 436)
        Form.setWindowIcon(QtGui.QIcon('./img/b3.jpg'))

        # 设置密钥显示文本框
        self.showk = QtWidgets.QTextBrowser(parent=Form)
        self.showk.setGeometry(QtCore.QRect(525, 250, 95, 95))
        self.showk.setObjectName("textBrowser")

        # 设置按钮
        self.pButton = QtWidgets.QPushButton(parent=Form)
        self.pButton.setGeometry(QtCore.QRect(190, 175, 66, 35))
        self.pButton.setObjectName("pButton")
        self.pButton.clicked.connect(self.decry)
        self.tButton = QtWidgets.QPushButton(parent=Form)
        self.tButton.setGeometry(QtCore.QRect(500, 175, 81, 31))
        self.tButton.setObjectName("tButton")
        self.tButton.clicked.connect(self.showDialog)

        # 设置按钮和输入框所在的frame
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(-1, 220, 261, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        # 创建labels和输入框
        self.pline = QtWidgets.QLineEdit(parent=self.frame)
        self.pline.setGeometry(QtCore.QRect(120, 50, 132, 20))
        self.pline.setObjectName("pline")
        self.cline = QtWidgets.QLineEdit(parent=self.frame)
        self.cline.setGeometry(QtCore.QRect(120, 80, 132, 20))
        self.cline.setObjectName("cline")
        self.plain = QtWidgets.QLabel(parent=self.frame)
        self.plain.setGeometry(QtCore.QRect(82, 50, 40, 20))
        self.cipher = QtWidgets.QLabel(parent=self.frame)
        self.cipher.setGeometry(QtCore.QRect(82, 80, 40, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 75, 219))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        self.plain.setPalette(palette)
        self.cipher.setPalette(palette)
        self.plain.setObjectName("plain")
        self.cipher.setObjectName("cipher")

        # 设置窗口大标题
        self.title = QtWidgets.QLabel(parent=Form)
        self.title.setGeometry(QtCore.QRect(80, 10, 301, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.title.setPalette(palette)
        self.title.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.title.setScaledContents(False)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")

        # 设置窗口小标题
        self.task = QtWidgets.QLabel(parent=Form)
        self.task.setGeometry(QtCore.QRect(475, 50, 163, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 172))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 172))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.task.setPalette(palette)
        self.task.setObjectName("task")

        # 设置listview创建背景
        self.listView = QtWidgets.QListView(parent=Form)
        self.listView.setGeometry(QtCore.QRect(-10, -60, 641, 541))
        self.listView.setStyleSheet("background-image: url(./img/b3.jpg);")
        self.listView.setObjectName("listView")

        self.listView.raise_()
        self.showk.raise_()
        self.pButton.raise_()
        self.tButton.raise_()
        self.frame.raise_()
        self.title.raise_()
        self.task.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        # 设置显示的内容
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "多重加密"))
        self.pButton.setWhatsThis(_translate(
            "Form", "<html><head/><body><p align=\"center\">"
            "<span style=\" font-size:18pt; color:#55ffff;\">加密</span></p></body></html>"))
        self.pButton.setText(_translate("Form", "中间相遇\n攻击"))
        self.tButton.setWhatsThis(_translate(
            "Form", "<html><head/><body><p align=\"center\">"
            "<span style=\" font-size:18pt; color:#55ffff;\">加密</span></p></body></html>"))
        self.tButton.setText(_translate("Form", "多重加密"))
        self.plain.setText(_translate(
            "Form", "<html><head/><body><p align=\"center\">"
            "<span style=\" font-size:11pt; font-weight:700;\">明文</span></p></body></html>"))
        self.cipher.setText(_translate(
            "Form", "<html><head/><body><p align=\"center\""
            "<span style=\" font-size:12pt; font-weight:800;\">密文</span></p></body></html>"))
        self.title.setText(_translate(
            "Form", "<html><head/><body><p align=\"center\">"
            "<span style=\" font-size:72pt; font-weight:700;\">S-AES</span></p></body></html>"))
        self.task.setText(_translate(
            "Form", "<html><head/><body><p align=\"center\">"
            "<span style=\" font-size:22pt; font-weight:700;\">多重加密</span></p></body></html>"))

    def decry(self):
        plain = self.pline.text()
        cipher = self.cline.text()
        self.showk.setText("密钥为：")
        self.showk.append(str(aes.middle_attack(plain, cipher)))

    def showDialog(self):
        # 通过输入对话框实现多个多重加密
        num, okPressed = QInputDialog.getText(self, "第一步", "使用几个密钥加密（2，3）")
        if okPressed:
            plain, okPressed = QInputDialog.getText(self, "输入明文", "明文")
            if okPressed:
                key, okPressed = QInputDialog.getText(self, "输入密钥（bit连在一起）", "密钥")
                if okPressed:
                    num = int(num)
                    self.showk.setText("结果为：")
                    self.showk.append(str(aes.encrypt(plain, key, num)))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_Formbf()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
