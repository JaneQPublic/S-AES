from PyQt6 import QtCore, QtGui, QtWidgets
import aes
import sys


class Ui_Form4(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form4, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 436)
        Form.setWindowIcon(QtGui.QIcon('./img/b4.jpg'))

        # 设置密文显示文本框
        self.showc = QtWidgets.QTextBrowser(parent=Form)
        self.showc.setGeometry(QtCore.QRect(470, 303, 148, 130))
        self.showc.setObjectName("showc")

        # 设置加密按钮
        self.eButton = QtWidgets.QPushButton(parent=Form)
        self.eButton.setGeometry(QtCore.QRect(237, 119, 55, 38))
        self.eButton.setObjectName("eButton")
        self.eButton.clicked.connect(self.en)
        # 解密按钮
        self.dButton = QtWidgets.QPushButton(parent=Form)
        self.dButton.setGeometry(QtCore.QRect(227, 221, 54, 30))
        self.dButton.setObjectName("dButton")
        self.dButton.clicked.connect(self.d)
        # 篡改按钮
        self.cButton = QtWidgets.QPushButton(parent=Form)
        self.cButton.setGeometry(QtCore.QRect(430, 251, 54, 30))
        self.cButton.setObjectName("cButton")
        self.cButton.clicked.connect(self.c)

        # 设置按钮和输入框所在的frame
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(-55, 280, 500, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        # 创建labels和输入框
        self.plaintext = QtWidgets.QLabel(parent=self.frame)
        self.plaintext.setGeometry(QtCore.QRect(135, 80, 100, 16))
        self.plaintext.setObjectName("plaintext")
        self.key = QtWidgets.QLabel(parent=self.frame)
        self.key.setGeometry(QtCore.QRect(195, 120, 24, 16))
        self.key.setObjectName("key")
        self.num = QtWidgets.QLabel(parent=self.frame)
        self.num.setGeometry(QtCore.QRect(220, 101, 50, 16))
        self.num.setObjectName("num")
        self.nline = QtWidgets.QLineEdit(parent=self.frame)
        self.nline.setGeometry(QtCore.QRect(273, 100, 30, 20))
        self.nline.setObjectName("nline")
        self.pline = QtWidgets.QLineEdit(parent=self.frame)
        self.pline.setGeometry(QtCore.QRect(193, 80, 170, 20))
        self.pline.setObjectName("pline")
        self.kline = QtWidgets.QLineEdit(parent=self.frame)
        self.kline.setGeometry(QtCore.QRect(223, 120, 130, 20))
        self.kline.setObjectName("kline")

        # 设置窗口大标题
        self.title = QtWidgets.QLabel(parent=Form)
        self.title.setGeometry(QtCore.QRect(55, 10, 301, 101))
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
        self.de = QtWidgets.QLabel(parent=Form)
        self.de.setGeometry(QtCore.QRect(460, 20, 150, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 172))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 172))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.de.setPalette(palette)
        self.de.setObjectName("de")

        # 设置listview创建背景
        self.listView = QtWidgets.QListView(parent=Form)
        self.listView.setGeometry(QtCore.QRect(-10, -20, 641, 541))
        self.listView.setStyleSheet("background-image: url(./img/b4.jpg);")
        self.listView.setObjectName("listView")

        self.listView.raise_()
        self.showc.raise_()
        self.eButton.raise_()
        self.dButton.raise_()
        self.cButton.raise_()
        self.frame.raise_()
        self.title.raise_()
        self.de.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        # 设置显示的内容
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "工作模式"))
        self.eButton.setWhatsThis(_translate(
            "Form", "<html><head/><body><p align=\"center\">"
            "<span style=\" font-size:18pt; color:#55ffff;\">加密</span></p></body></html>"))
        self.eButton.setText(_translate("Form", "CBC加密"))
        self.dButton.setText(_translate("Form", "CBC解密"))
        self.cButton.setText(_translate("Form", "篡改密文"))
        self.key.setText(_translate("Form", "密钥"))
        self.num.setText(_translate("Form", "密钥数量"))
        self.plaintext.setText(_translate("Form", "明文/密文"))
        self.title.setText(_translate(
            "Form", "<html><head/><body><p align=\"center\">"
            "<span style=\" font-size:72pt; font-weight:700;\">S-AES</span></p></body></html>"))
        self.de.setText(_translate(
            "Form", "<html><head/><body><p align=\"center\">"
            "<span style=\" font-size:28pt; font-weight:700;\">工作模式</span></p></body></html>"))

    def en(self):
        # 定义加密函数
        key = self.kline.text()
        plain = self.pline.text()
        num = int(self.nline.text())
        self.showc.setText("密文为：")
        self.showc.append(aes.CBC_encrypt(plain, key, num))

    def d(self):
        # 定义解密函数
        key = self.kline.text()
        plain = self.pline.text()
        num = int(self.nline.text())
        self.showc.setText("明文为：")
        self.showc.append(aes.CBC_decrypt(plain, key, num))
    def c(self):
        # 定义篡改函数
        key = self.kline.text()
        cipher = self.pline.text()
        num = int(self.nline.text())
        plain = aes.CBC_decrypt(cipher, key, num)
        plain_new = aes.change(cipher, key, num)
        self.showc.setText("改前解密结果为：")
        self.showc.append(plain)
        self.showc.append("改后解密结果为：")
        self.showc.append(plain_new)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_Form4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
