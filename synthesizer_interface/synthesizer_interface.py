from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class UiMainWindow(object):
    def setup_ui(self, MainWindow):

        # Setting up the main application window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(165, 216, 255);")

        # Creating the central widget (main part of the window)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Creating the header (label with text)
        self.label_h2 = QtWidgets.QLabel(self.centralwidget)
        self.label_h2.setGeometry(QtCore.QRect(310, 45, 391, 101))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_h2.setFont(font)
        self.label_h2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_h2.setObjectName("label_h2")
        
        # Creating a combo box for selecting a male or female voice
        self.combo_box_female_male_voice = QtWidgets.QComboBox(self.centralwidget)
        self.combo_box_female_male_voice.setGeometry(QtCore.QRect(110, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_box_female_male_voice.setFont(font)
        self.combo_box_female_male_voice.setStyleSheet("background-color: rgb(165, 216, 255);")
        self.combo_box_female_male_voice.setObjectName("combo_box_female_male_voice")
        self.combo_box_female_male_voice.addItem("")
        self.combo_box_female_male_voice.addItem("")

        # Creating a text field for entering text
        self.plain_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plain_text.setGeometry(QtCore.QRect(113, 150, 631, 141))
        self.plain_text.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(255, 255, 255);")
        self.plain_text.setObjectName("plain_text")
        self.button_voice_over = QtWidgets.QPushButton(self.centralwidget)
        self.button_voice_over.setGeometry(QtCore.QRect(480, 320, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        # Creating a button to voice the text
        self.button_voice_over.setFont(font)
        self.button_voice_over.setObjectName("button_voice_over")
        self.button_download = QtWidgets.QPushButton(self.centralwidget)
        self.button_download.setGeometry(QtCore.QRect(120, 320, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        # Creating a button to download the voiced text
        self.button_download.setFont(font)
        self.button_download.setObjectName("butto_download")
        
        # Setting the central widget as the main element of the window
        MainWindow.setCentralWidget(self.centralwidget)

        # Creating a status bar at the bottom of the window
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        # Calling the function to translate the UI
        self.retrans_late_ui(MainWindow)

        # Connecting slots to UI elements
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retrans_late_ui(self, MainWindow):
        # Setting text for the UI
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Пишет"))
        self.label_h2.setText(_translate("MainWindow", "Введите текст"))
        self.combo_box_female_male_voice.setItemText(0, _translate("MainWindow", "Голос женский"))
        self.combo_box_female_male_voice.setItemText(1, _translate("MainWindow", "Голос мужской "))
        self.button_voice_over.setText(_translate("MainWindow", "Озвучить"))
        self.button_download.setText(_translate("MainWindow", "Скачать"))


if __name__ == "__main__":
    # Creating the application and launching the main window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
