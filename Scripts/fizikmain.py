# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from keyboard import add_hotkey
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider,QDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-image: url(Assets/Fizik Main UI.svg);")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(1280, 260, 501, 281))
        self.treeWidget.setStyleSheet("QHeaderView::section {background-color: black; color: white; border:none;font: 63 13pt \"Segoe UI Semibold\";padding-left:31px}\n"
"QTreeWidget::item {color: white;border:none;font: 63 16pt \"Segoe UI Semibold\";padding-left:28px;}\n"
"QTreeWidget {background-color: rgba(52, 46, 255, 0.3); border:none;background-image:url();font: 63 12pt \"Segoe UI\";}\n"
"QTreeWidget::item {text-align: center;}")
        self.treeWidget.setProperty("showDropIndicator", False)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setItemsExpandable(False)
        self.treeWidget.setExpandsOnDoubleClick(False)
        self.treeWidget.setObjectName("treeWidget")
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(125)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setMinimumSectionSize(48)
        self.treeWidget.header().setStretchLastSection(False)
        self.aracivme_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.aracivme_lineEdit.setGeometry(QtCore.QRect(580, 354, 113, 51))
        self.aracivme_lineEdit.setStyleSheet("QLineEdit{\n"
"background-color:#CCCCCC94;\n"
"border:none;\n"
"color: rgb(204, 204, 204);\n"
"font-family: \"Open Sans\";\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;\n"
"padding:3px;\n"
"}")
        self.aracivme_lineEdit.setObjectName("aracivme_lineEdit")
        validator = QtGui.QIntValidator(MainWindow)
        self.aracivme_lineEdit.setValidator(validator)
        self.yercekim_linEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.yercekim_linEdit.setGeometry(QtCore.QRect(580, 576, 113, 51))
        self.yercekim_linEdit.setStyleSheet("QLineEdit{\n"
"background-color:#CCCCCC94;\n"
"border:none;\n"
"color: rgb(204, 204, 204);\n"
"font-family: \"Open Sans\";\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;\n"
"padding:3px;\n"
"}")
        self.yercekim_linEdit.setObjectName("yercekim_linEdit")
        self.yercekim_linEdit.setValidator(validator)
        self.elmaatishiz_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.elmaatishiz_lineEdit.setGeometry(QtCore.QRect(580, 500, 113, 51))
        self.elmaatishiz_lineEdit.setStyleSheet("QLineEdit{\n"
"background-color:#CCCCCC94;\n"
"border:none;\n"
"color: rgb(204, 204, 204);\n"
"font-family: \"Open Sans\";\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;\n"
"padding:3px;\n"
"}")
        self.elmaatishiz_lineEdit.setObjectName("elmaatishiz_lineEdit")
        self.elmaatishiz_lineEdit.setValidator(validator)
        self.arachiz_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.arachiz_lineEdit.setGeometry(QtCore.QRect(580, 430, 113, 51))
        self.arachiz_lineEdit.setStyleSheet("QLineEdit{\n"
"background-color:#CCCCCC94;\n"
"border:none;\n"
"color: rgb(204, 204, 204);\n"
"font-family: \"Open Sans\";\n"
"font-size: 25px;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"line-height: normal;\n"
"padding:3px;\n"
"}")
        self.arachiz_lineEdit.setObjectName("arachiz_lineEdit")
        self.arachiz_lineEdit.setValidator(validator)
        self.simule_button = QtWidgets.QPushButton(self.centralwidget)
        self.simule_button.setGeometry(QtCore.QRect(90, 650, 611, 51))
        self.simule_button.setStyleSheet("QPushButton{\n"
"    background-image: url();\n"
"border-radius: 4px;\n"
"background: #01DC3E;\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: \"Open Sans\";\n"
"font-size: 18px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(27, 157, 27);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 120, 0);\n"
"}")
        self.simule_button.setObjectName("simule_button")
        self.simule_button.clicked.connect(self.dataControl)
        self.maksyukseklik_Label = QtWidgets.QLabel(self.centralwidget)
        self.maksyukseklik_Label.setGeometry(QtCore.QRect(1190, 640, 301, 71))
        self.maksyukseklik_Label.setStyleSheet("QLabel{\n"
"    background-image: url();\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: \"Open Sans\";\n"
"font-size: 48px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"width: 186px;\n"
"height: 130px;\n"
"}")
        self.maksyukseklik_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.maksyukseklik_Label.setObjectName("maksyukseklik_Label")
        self.havadaKalma_label = QtWidgets.QLabel(self.centralwidget)
        self.havadaKalma_label.setGeometry(QtCore.QRect(1560, 640, 301, 71))
        self.havadaKalma_label.setStyleSheet("QLabel{\n"
"    background-image: url();\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: \"Open Sans\";\n"
"font-size: 48px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"width: 186px;\n"
"height: 130px;\n"
"}")
        self.havadaKalma_label.setAlignment(QtCore.Qt.AlignCenter)
        self.havadaKalma_label.setObjectName("havadaKalma_label")
        self.animasyon_button = QtWidgets.QPushButton(self.centralwidget)
        self.animasyon_button.setGeometry(QtCore.QRect(1180, 750, 701, 51))
        self.animasyon_button.setStyleSheet("QPushButton{\n"
"    background-image: url();\n"
"border-radius: 4px;\n"
"    background-color: rgb(0, 0, 255);\n"
"color: #FFF;\n"
"text-align: center;\n"
"font-family: \"Open Sans\";\n"
"font-size: 18px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(6, 0, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 14, 104);\n"
"}")
        self.animasyon_button.setObjectName("animasyon_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "T"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "X"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "H"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Araç X"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.aracivme_lineEdit.setPlaceholderText(_translate("MainWindow", "m/s²..."))
        self.yercekim_linEdit.setPlaceholderText(_translate("MainWindow", "m/s²..."))
        self.elmaatishiz_lineEdit.setPlaceholderText(_translate("MainWindow", "m/s ..."))
        self.arachiz_lineEdit.setPlaceholderText(_translate("MainWindow", "m/s ..."))
        self.simule_button.setText(_translate("MainWindow", "Simüle Et!"))
        self.maksyukseklik_Label.setText(_translate("MainWindow", "0 M"))
        self.havadaKalma_label.setText(_translate("MainWindow", "0 Sn"))
        self.animasyon_button.setText(_translate("MainWindow", "Animasyonu Oynat"))
        self.animasyon_button.clicked.connect(self.animation)
    def close(self):
        MainWindow.close()
    def set_line_edit_validator(self, line_edit):
        validator = QtGui.QIntValidator(MainWindow)
        line_edit.setValidator(validator)
    def platform_cisim_hesapla(self,v_p, a_p, v_c, g):
        
        # Platformun hareket denklemi: x_p = v_p * t + 0.5 * a_p * t**2
        # Cismin y eksenindeki hareket denklemi: y_c = v_c * t - 0.5 * g * t**2
        # Cismin x eksenindeki hareket denklemi: x_c = v_p * t
        try:
                T = 2 * v_c / g

                sonuc = []

                # Her T süresinde platformun ve cismin konumlarını hesapla ve listeye ekle
                for t in range(int(T) + 1):
                    x_p = v_p * t + 0.5 * a_p * t**2
                    y_c = v_c * t - 0.5 * g * t**2
                    x_c = v_p * t
                    sonuc.append((t+1, x_p, y_c, x_c))
                return sonuc
        except Exception as e:
            print(e)
    def dataControl(self):
        _translate = QtCore.QCoreApplication.translate
        self.treeWidget.clear()
        if self.aracivme_lineEdit.text() != "" and self.yercekim_linEdit.text() != "" and self.elmaatishiz_lineEdit.text() != "" and self.arachiz_lineEdit.text() != "":
                v_p = int(self.arachiz_lineEdit.text())
                a_p = int(self.aracivme_lineEdit.text())
                v_c = int(self.elmaatishiz_lineEdit.text())
                g = int(self.yercekim_linEdit.text())
                veri = self.platform_cisim_hesapla(v_p,a_p,v_c,g)
                for i in range(len(veri)):
                    item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
                flag = 0
                h_data = []
                for i in veri:
                    t = i[0]
                    x = i[3]
                    h = i[2]
                    h_data.append(h)
                    arac_x = i[1]
                    self.treeWidget.topLevelItem(flag).setText(0, _translate("MainWindow", f"{t}"))
                    self.treeWidget.topLevelItem(flag).setText(1, _translate("MainWindow", f"{x}"))
                    self.treeWidget.topLevelItem(flag).setText(2, _translate("MainWindow", f"{h}"))
                    self.treeWidget.topLevelItem(flag).setText(3, _translate("MainWindow", f"{arac_x}"))
                    flag += 1   
                h_data = int(sorted(h_data,reverse=True)[0])
        
                self.maksyukseklik_Label.setText(_translate("MainWindow", f"{h_data} M"))
                self.havadaKalma_label.setText(_translate("MainWindow", f"{flag} S"))
        else:("Err")
    def animation(self):
        try:
            try:
                v_p = int(self.arachiz_lineEdit.text())
                a_p = int(self.aracivme_lineEdit.text())
                v_c = int(self.elmaatishiz_lineEdit.text())
                g = int(self.yercekim_linEdit.text())
                veri = self.platform_cisim_hesapla(v_p,a_p,v_c,g)  # 1 , 3 index
            except ValueError:
                QtWidgets.QMessageBox.warning(None,"Uyarı","Tüm alanları doldurunuz.")
                arac_x = veri[-1][1]
                cisim_x = veri[-1][3]
                sonuc = arac_x - cisim_x
                if sonuc == 0:
                     self.showMoreInfoDialog("Assets/dogrusaldusus.mp4","Elma Doğrusal Düşüyor")
                elif sonuc >= 0:
                     self.showMoreInfoDialog("Assets/geridusus.mp4","Elma Aracın Arkasına Düşüyor")
                else: self.showMoreInfoDialog("Assets/ileridusus.mp4","Elma Aracın Önüne Düşüyor")
        except Exception as e:
            print("Err:", e)
    def showMoreInfoDialog(self,video_path,title ):
        Dialog = QtWidgets.QDialog(MainWindow)
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 720)
        Dialog.setStyleSheet("background-image:url("");")
        Dialog.setWindowTitle(title)
        self.mediaPlayer = QMediaPlayer(Dialog, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)

        self.playButton = QPushButton("Play")
        self.playButton.clicked.connect(self.playClicked)
        layout.addWidget(self.playButton)

        self.positionSlider = QSlider(Qt.Horizontal)
        layout.addWidget(self.positionSlider)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        Dialog.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

        self.video_path = video_path
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.video_path)))
        Dialog.exec_()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def playClicked(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setText("Pause")
        else:
            self.playButton.setText("Play")

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    add_hotkey('esc',ui.close)
    MainWindow.show()
    sys.exit(app.exec_())