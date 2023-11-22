import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QComboBox, QListView, QPushButton, QWidget, QListWidgetItem, QMessageBox, QSpinBox
# Importer la classe Ui_MainWindow du fichier demo.py
from hdvelh2 import Ui_MainWindow

# En paramêtre de la classe MainWindow on va hériter des fonctionnalités
# de QMainWindow et de notre interface Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_discipline.clicked.connect(self.ajouter_discipline_listWidget)
        self.button_arme.clicked.connect(self.ajouter_arme_listWidget)
        
        self.spinBox_bourse_sac.setMaximum(50)  
        self.spinBox_bourse_sac.setValue(9)  

        self.comboBox_livre.activated.connect(self.commencerHistoire)

        self.button_histoire.clicked.connect(self.cest_parti)

        self.pushButton_nouvellePartie.clicked.connect(self.nouvellePartie)


    def showEvent(self, event):
        self.ajouter_disciplines_comboBox()
        self.ajouter_armes_comboBox()
        self.ajouter_livres_comboBox()
        self.ajouter_joueurs_comboBox()

        


##FONCTIONS DEBUT (showEvent)###########################################################################################################################################
    def ajouter_disciplines_comboBox(self):
        try:
            connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='hdvelh_tpsommatif'
            )
            
            cursor = connection.cursor()
            cursor.execute("SELECT nom_discipline FROM disciplines_kai")
            resultats = cursor.fetchall()
            connection.close()

            if resultats:
                for resultat in resultats:
                    self.comboBox_discipline.addItem(resultat[0])

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    def ajouter_discipline_listWidget(self):
        if self.listWidget_disciplines.count() >= 5:
            QMessageBox.warning(self, 'LIMITE ATTEINTE', 'Vous ne pouvez pas ajouter plus de 5 disciplines.')
            return
    
        discipline_selectionnee = self.comboBox_discipline.currentText()

        for index in range(self.listWidget_disciplines.count()):
            item = self.listWidget_disciplines.item(index)
            if item.text() == discipline_selectionnee:
                QMessageBox.warning(self, 'DISCIPLINE DÉJÀ SÉLECTIONNÉE', 'Cette discipline a déjà été sélectionnée.')
                return

        if discipline_selectionnee:
            item = QListWidgetItem(discipline_selectionnee)
            self.listWidget_disciplines.addItem(item)

        




    def ajouter_armes_comboBox(self):
        try:
            connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='hdvelh_tpsommatif'
            )
            
            cursor = connection.cursor()
            cursor.execute("SELECT nom_arme FROM armes")
            resultats = cursor.fetchall()  
            connection.close()

            if resultats:
                for resultat in resultats:
                    self.comboBox_arme.addItem(resultat[0])

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    def ajouter_arme_listWidget(self):
        if self.listWidget_armes.count() >= 2:
            QMessageBox.warning(self, 'LIMITE ATTEINTE', 'Vous ne pouvez pas ajouter plus de 2 armes.')
            return
    
        arme_selectionnee = self.comboBox_arme.currentText()

        for index in range(self.listWidget_armes.count()):
            item = self.listWidget_armes.item(index)
            if item.text() == arme_selectionnee:
                QMessageBox.warning(self, 'ARME DÉJÀ SÉLECTIONNÉE', 'Cette arme a déjà été sélectionnée.')
                return

        if arme_selectionnee:
            item = QListWidgetItem(arme_selectionnee)
            self.listWidget_armes.addItem(item)

        for index in range(self.listWidget_armes.count()):
            item = self.listWidget_armes.item(index)
            if item.text():
                item_arme_selectionne = item.text()
                print(item_arme_selectionne) #Afficher l'item selectionne dans le QListWidget




    def ajouter_livres_comboBox(self):
        try:
            connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='hdvelh_tpsommatif'
            )
            
            cursor = connection.cursor()
            cursor.execute("SELECT titre_livre FROM livres")
            resultats = cursor.fetchall()  
            connection.close()

            if resultats:
                for resultat in resultats:
                    self.comboBox_livre.addItem(resultat[0])

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")


    def ajouter_joueurs_comboBox(self):
        try:
            connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='hdvelh_tpsommatif'
            )
            
            cursor = connection.cursor()
            cursor.execute("SELECT nom_joueur FROM joueur")
            resultats = cursor.fetchall()  
            connection.close()

            if resultats:
                for resultat in resultats:
                    self.comboBox_sauvegarde.addItem(resultat[0])

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")



######FIN FONCTIONS DÉBUT###################################################################################################################################

#####FONCTIONS DE CHAPITRE##########################################################################################################################################
    def commencerHistoire(self):
        livre_selectionne = self.comboBox_livre.currentText()
        try:
            connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='hdvelh_tpsommatif'
            )
            
            cursor = connection.cursor()
            select_histoire = "SELECT c.texte, l.titre_livre, c.no_chapitre FROM chapitres c INNER JOIN livres l ON c.id_livre = l.id_livre WHERE l.titre_livre = %s AND c.id_chapitre = %s"
            cursor.execute(select_histoire, (livre_selectionne, '1',) )
            resultats = cursor.fetchall()  
            connection.close()

            if resultats:
                for resultat in resultats:
                    self.textBrowser_histoire.setText(resultat[0])

                    self.label_titreLivre.setWordWrap(True)
                    self.label_titreLivre.setMaximumWidth(771)
                    self.label_titreLivre.setText(resultat[1])

                    self.label_histoireChapitre_2.setText(resultat[2])

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")



    def afficher_premierChapitre(self, titre_livre_selectionne):
        try:
            connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='hdvelh_tpsommatif'
            )
            
            cursor = connection.cursor()
            select_histoire = "SELECT c.no_chapitre FROM chapitres c INNER JOIN livres l ON c.id_livre = l.id_livre	WHERE c.no_chapitre = %s AND titre_livre = %s"
            cursor.execute(select_histoire, ('1', titre_livre_selectionne,) )
            resultats = cursor.fetchall()  
            connection.close()

            if resultats:
                for resultat in resultats:
                    self.comboBox_histoire.addItem(resultat[0])
                  

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")


    def cest_parti(self):
        chapitre_selectionne = self.comboBox_histoire.currentText()
        livre_selectionne = self.comboBox_livre.currentText()
        if self.comboBox_histoire.count() == 0:
            self.afficher_premierChapitre(livre_selectionne)

        else:
            try:
                connection = mysql.connector.connect(
                    user='root',
                    password='',
                    host='localhost',
                    database='hdvelh_tpsommatif'
                )
                
                cursor = connection.cursor()
                select_histoire = "SELECT c.texte, c.no_chapitre FROM chapitres c INNER JOIN liens_chapitres lc ON c.id_chapitre = lc.no_chapitre_origine WHERE c.no_chapitre = %s"
                cursor.execute(select_histoire, (chapitre_selectionne,) )
                resultats = cursor.fetchall()  
                connection.close()

                if resultats:
                    for resultat in resultats:
                        self.textBrowser_histoire.setText(resultat[0])

                        self.label_histoireChapitre_2.setText(resultat[1])
                        valeur_chapitreActuel = self.label_histoireChapitre_2.text()
                        self.afficher_chapitresDestination(valeur_chapitreActuel)


            except mysql.connector.Error as err:
                print(f"Erreur MySQL : {err}")


    def afficher_chapitresDestination(self, valeur_chapitreActuel):
        self.comboBox_histoire.clear()
        try:
            connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='hdvelh_tpsommatif'
            )
            
            cursor = connection.cursor()
            select_histoire = 'SELECT lc.no_chapitre_destination FROM chapitres c INNER JOIN liens_chapitres lc ON c.id_chapitre = lc.no_chapitre_origine	WHERE lc.no_chapitre_origine = %s'
            cursor.execute(select_histoire, (valeur_chapitreActuel,) )
            resultats = cursor.fetchall()  
            connection.close()

            if resultats:
                for resultat in resultats:
                    self.comboBox_histoire.addItem(str(resultat[0]))


        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

###FIN CHAPITRES#########################################################################################################################################




###SAUVEGARDE############################################################################################################################################
    def nouvellePartie(self):
        nomSaisi = self.lineEdit_nom.text()
        #Pour savoir si l'usager a entré un nom pour la sauvegarde. Si oui, il va effectuer l'insertion du nom dans la BD
        if not nomSaisi:
            QMessageBox.warning(self, 'CHAMP VIDE', 'Pour sauvegarder, il faut un nom de sauvegarde')
            return
        else:
            self.label_nomGrand.setText(nomSaisi)
            self.comboBox_sauvegarde.addItem(nomSaisi)
            self.insererJoueur(nomSaisi)
            self.initialisation_inserts(nomSaisi)



###FIN SAUVEGARDE############################################################################################################################################


###DEBUT APPELS FONCTIONS / PROCEDURE############################################################################################################################################
    def insererJoueur(self, nom_joueur):
        print("Valeurs à insérer :", nom_joueur)

        try:
            connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='hdvelh_tpsommatif'
            )
            
            cursor = connection.cursor()
            
            procedure_insert_joueur = 'CALL insert_joueur(%s)'
            cursor.execute(procedure_insert_joueur, (nom_joueur,))
            connection.commit()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")



    def initialisation_inserts(self, nom_joueur):
        try:
            connection = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='hdvelh_tpsommatif'
            )
            
            cursor = connection.cursor()
            
            procedure_initialisation = 'CALL initialiser_insert(%s)'
            cursor.execute(procedure_initialisation, (nom_joueur,))
            connection.commit()
            cursor.close()
            connection.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")





        




app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
