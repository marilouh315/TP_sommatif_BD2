# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hdvelh.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_titreLivre = QtWidgets.QLabel(self.centralwidget)
        self.label_titreLivre.setGeometry(QtCore.QRect(670, 10, 381, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_titreLivre.setFont(font)
        self.label_titreLivre.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titreLivre.setObjectName("label_titreLivre")
        self.label_nomGrand = QtWidgets.QLabel(self.centralwidget)
        self.label_nomGrand.setGeometry(QtCore.QRect(740, 100, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_nomGrand.setFont(font)
        self.label_nomGrand.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nomGrand.setObjectName("label_nomGrand")
        self.label_fichePersonnage = QtWidgets.QLabel(self.centralwidget)
        self.label_fichePersonnage.setGeometry(QtCore.QRect(90, 10, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_fichePersonnage.setFont(font)
        self.label_fichePersonnage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fichePersonnage.setObjectName("label_fichePersonnage")
        self.groupBox_histoire = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_histoire.setGeometry(QtCore.QRect(470, 350, 781, 501))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_histoire.setFont(font)
        self.groupBox_histoire.setObjectName("groupBox_histoire")
        self.textBrowser_histoire = QtWidgets.QTextBrowser(self.groupBox_histoire)
        self.textBrowser_histoire.setGeometry(QtCore.QRect(20, 30, 501, 451))
        self.textBrowser_histoire.setObjectName("textBrowser_histoire")
        self.label_histoire = QtWidgets.QLabel(self.groupBox_histoire)
        self.label_histoire.setGeometry(QtCore.QRect(580, 190, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_histoire.setFont(font)
        self.label_histoire.setAlignment(QtCore.Qt.AlignCenter)
        self.label_histoire.setObjectName("label_histoire")
        self.comboBox_histoire = QtWidgets.QComboBox(self.groupBox_histoire)
        self.comboBox_histoire.setGeometry(QtCore.QRect(540, 240, 231, 31))
        self.comboBox_histoire.setObjectName("comboBox_histoire")
        self.button_histoire = QtWidgets.QPushButton(self.groupBox_histoire)
        self.button_histoire.setGeometry(QtCore.QRect(590, 280, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_histoire.setFont(font)
        self.button_histoire.setObjectName("button_histoire")
        self.groupBox_disciplines = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_disciplines.setGeometry(QtCore.QRect(10, 50, 441, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_disciplines.setFont(font)
        self.groupBox_disciplines.setObjectName("groupBox_disciplines")
        self.comboBox_discipline = QtWidgets.QComboBox(self.groupBox_disciplines)
        self.comboBox_discipline.setGeometry(QtCore.QRect(20, 50, 271, 31))
        self.comboBox_discipline.setObjectName("comboBox_discipline")
        self.button_discipline = QtWidgets.QPushButton(self.groupBox_disciplines)
        self.button_discipline.setGeometry(QtCore.QRect(310, 50, 101, 28))
        self.button_discipline.setObjectName("button_discipline")
        self.listView_discipline = QtWidgets.QListView(self.groupBox_disciplines)
        self.listView_discipline.setGeometry(QtCore.QRect(20, 100, 391, 111))
        self.listView_discipline.setObjectName("listView_discipline")
        self.label_condition_discipline = QtWidgets.QLabel(self.groupBox_disciplines)
        self.label_condition_discipline.setGeometry(QtCore.QRect(30, 20, 261, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_condition_discipline.setFont(font)
        self.label_condition_discipline.setObjectName("label_condition_discipline")
        self.groupBox_armes = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_armes.setGeometry(QtCore.QRect(10, 280, 441, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_armes.setFont(font)
        self.groupBox_armes.setObjectName("groupBox_armes")
        self.comboBox_arme = QtWidgets.QComboBox(self.groupBox_armes)
        self.comboBox_arme.setGeometry(QtCore.QRect(20, 40, 281, 31))
        self.comboBox_arme.setObjectName("comboBox_arme")
        self.button_arme = QtWidgets.QPushButton(self.groupBox_armes)
        self.button_arme.setGeometry(QtCore.QRect(320, 40, 93, 28))
        self.button_arme.setObjectName("button_arme")
        self.listView_arme = QtWidgets.QListView(self.groupBox_armes)
        self.listView_arme.setGeometry(QtCore.QRect(20, 80, 391, 51))
        self.listView_arme.setObjectName("listView_arme")
        self.label_condition_arme = QtWidgets.QLabel(self.groupBox_armes)
        self.label_condition_arme.setGeometry(QtCore.QRect(30, 20, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_condition_arme.setFont(font)
        self.label_condition_arme.setObjectName("label_condition_arme")
        self.groupBox_sac = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_sac.setGeometry(QtCore.QRect(10, 430, 441, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_sac.setFont(font)
        self.groupBox_sac.setObjectName("groupBox_sac")
        self.textEdit_objet_sac = QtWidgets.QTextEdit(self.groupBox_sac)
        self.textEdit_objet_sac.setGeometry(QtCore.QRect(150, 30, 261, 87))
        self.textEdit_objet_sac.setObjectName("textEdit_objet_sac")
        self.textEdit_repas_sac = QtWidgets.QTextEdit(self.groupBox_sac)
        self.textEdit_repas_sac.setGeometry(QtCore.QRect(150, 130, 261, 87))
        self.textEdit_repas_sac.setObjectName("textEdit_repas_sac")
        self.textEdit_os_sac = QtWidgets.QTextEdit(self.groupBox_sac)
        self.textEdit_os_sac.setGeometry(QtCore.QRect(150, 240, 261, 87))
        self.textEdit_os_sac.setObjectName("textEdit_os_sac")
        self.spinBox_bourse_sac = QtWidgets.QSpinBox(self.groupBox_sac)
        self.spinBox_bourse_sac.setGeometry(QtCore.QRect(150, 360, 261, 31))
        self.spinBox_bourse_sac.setObjectName("spinBox_bourse_sac")
        self.label_objet_sac = QtWidgets.QLabel(self.groupBox_sac)
        self.label_objet_sac.setGeometry(QtCore.QRect(20, 40, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_objet_sac.setFont(font)
        self.label_objet_sac.setObjectName("label_objet_sac")
        self.label_repas_sac = QtWidgets.QLabel(self.groupBox_sac)
        self.label_repas_sac.setGeometry(QtCore.QRect(20, 140, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_repas_sac.setFont(font)
        self.label_repas_sac.setObjectName("label_repas_sac")
        self.label_os_sac = QtWidgets.QLabel(self.groupBox_sac)
        self.label_os_sac.setGeometry(QtCore.QRect(20, 250, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_os_sac.setFont(font)
        self.label_os_sac.setObjectName("label_os_sac")
        self.label_bourse = QtWidgets.QLabel(self.groupBox_sac)
        self.label_bourse.setGeometry(QtCore.QRect(20, 340, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_bourse.setFont(font)
        self.label_bourse.setObjectName("label_bourse")
        self.comboBox_livre = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_livre.setGeometry(QtCore.QRect(610, 230, 231, 31))
        self.comboBox_livre.setObjectName("comboBox_livre")
        self.lineEdit_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nom.setGeometry(QtCore.QRect(610, 180, 231, 31))
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.comboBox_sauvegarde = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_sauvegarde.setGeometry(QtCore.QRect(920, 230, 291, 31))
        self.comboBox_sauvegarde.setObjectName("comboBox_sauvegarde")
        self.button_charger = QtWidgets.QPushButton(self.centralwidget)
        self.button_charger.setGeometry(QtCore.QRect(920, 280, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_charger.setFont(font)
        self.button_charger.setObjectName("button_charger")
        self.pushButton_nouvellePartie = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_nouvellePartie.setGeometry(QtCore.QRect(520, 280, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_nouvellePartie.setFont(font)
        self.pushButton_nouvellePartie.setObjectName("pushButton_nouvellePartie")
        self.label_livre = QtWidgets.QLabel(self.centralwidget)
        self.label_livre.setGeometry(QtCore.QRect(510, 220, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_livre.setFont(font)
        self.label_livre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_livre.setObjectName("label_livre")
        self.label_nomPetit = QtWidgets.QLabel(self.centralwidget)
        self.label_nomPetit.setGeometry(QtCore.QRect(510, 170, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_nomPetit.setFont(font)
        self.label_nomPetit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_nomPetit.setObjectName("label_nomPetit")
        self.label_charger = QtWidgets.QLabel(self.centralwidget)
        self.label_charger.setGeometry(QtCore.QRect(980, 170, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_charger.setFont(font)
        self.label_charger.setAlignment(QtCore.Qt.AlignCenter)
        self.label_charger.setObjectName("label_charger")
        self.button_sauvegarder = QtWidgets.QPushButton(self.centralwidget)
        self.button_sauvegarder.setGeometry(QtCore.QRect(690, 280, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_sauvegarder.setFont(font)
        self.button_sauvegarder.setObjectName("button_sauvegarder")
        self.pushButton_supprimer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_supprimer.setGeometry(QtCore.QRect(1070, 280, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_supprimer.setFont(font)
        self.pushButton_supprimer.setObjectName("pushButton_supprimer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titreLivre.setText(_translate("MainWindow", "Titre Livre"))
        self.label_nomGrand.setText(_translate("MainWindow", "Nom personnage"))
        self.label_fichePersonnage.setText(_translate("MainWindow", "Fiche personnage"))
        self.groupBox_histoire.setTitle(_translate("MainWindow", "Histoire"))
        self.label_histoire.setText(_translate("MainWindow", "Choix de direction :"))
        self.button_histoire.setText(_translate("MainWindow", "C\'est parti !"))
        self.groupBox_disciplines.setTitle(_translate("MainWindow", "Disciplines Kai"))
        self.button_discipline.setText(_translate("MainWindow", "Ajouter"))
        self.label_condition_discipline.setText(_translate("MainWindow", "5 disciplines maximum"))
        self.groupBox_armes.setTitle(_translate("MainWindow", "Inventaire Armes"))
        self.button_arme.setText(_translate("MainWindow", "Ajouter"))
        self.label_condition_arme.setText(_translate("MainWindow", "2 armes maximum"))
        self.groupBox_sac.setTitle(_translate("MainWindow", "Sac à dos"))
        self.label_objet_sac.setText(_translate("MainWindow", "Objets:"))
        self.label_repas_sac.setText(_translate("MainWindow", "Repas:"))
        self.label_os_sac.setText(_translate("MainWindow", "Objets spéciaux:"))
        self.label_bourse.setText(_translate("MainWindow", "Bourse:"))
        self.button_charger.setText(_translate("MainWindow", "Charger"))
        self.pushButton_nouvellePartie.setText(_translate("MainWindow", "Nouvelle partie"))
        self.label_livre.setText(_translate("MainWindow", "Livre :"))
        self.label_nomPetit.setText(_translate("MainWindow", "Nom :"))
        self.label_charger.setText(_translate("MainWindow", "Charger partie :"))
        self.button_sauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.pushButton_supprimer.setText(_translate("MainWindow", "Supprimer"))
