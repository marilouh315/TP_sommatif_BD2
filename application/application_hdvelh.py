import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QComboBox, QListView, QPushButton, QWidget, QListWidgetItem, QMessageBox, QSpinBox
# Importer la classe Ui_MainWindow du fichier hdvelh2.py
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

        self.button_sauvegarder.clicked.connect(self.sauvegarder)

        self.button_charger.clicked.connect(self.chargerSauvegarde)

        self.pushButton_supprimer.clicked.connect(self.supprimer_sauvegarde)

        self.connection = mysql.connector.connect(
            user='hdvelhUsager2',
            password='mdp',
            host='localhost',
            database='hdvelh_tpsommatif'
        )

    #Fonction qui se déclenche lors de l'ouverture de la fenêtre
    def showEvent(self, event):
        self.ajouter_disciplines_comboBox()
        self.ajouter_armes_comboBox()
        self.ajouter_livres_comboBox()
        self.ajouter_joueurs_comboBox()

    #Fonction qui se déclenche lors de la fermeture de la fenêtre
    def closeEvent(self, event):
        self.connection.close()
        event.accept()


##FONCTIONS DEBUT (showEvent)###########################################################################################################################################
    #Fonction qui ajoute les disciplines de la base de donnée dans le comboBox des disciplines
    def ajouter_disciplines_comboBox(self):
        try:            
            cursor = self.connection.cursor()
            cursor.execute("SELECT nom_discipline FROM disciplines_kai")
            resultats = cursor.fetchall()

            if resultats:
                for resultat in resultats:
                    self.comboBox_discipline.addItem(resultat[0])

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui vérifie les ajouts de l'usager (Si l'usager ne choisit pas un doublon ou s'il en a choisi plus que 5)
    #et ajoute les disciplines choisies dans un QListWidget
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

    #Fonction qui ajoute les armes de la base de donnée dans le comboBox des armes
    def ajouter_armes_comboBox(self):
        try:            
            cursor = self.connection.cursor()
            cursor.execute("SELECT nom_arme FROM armes")
            resultats = cursor.fetchall()

            if resultats:
                for resultat in resultats:
                    self.comboBox_arme.addItem(resultat[0])

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui vérifie les ajouts de l'usager (Si l'usager ne choisit pas un doublon ou s'il en a choisi plus que 5)
    #et ajoute les armes choisies dans un QListWidget
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

    #Fonction qui ajoute les livres de la base de donnée dans le comboBox des livres
    def ajouter_livres_comboBox(self):
        try:            
            cursor = self.connection.cursor()
            cursor.execute("SELECT titre_livre FROM livres")
            resultats = cursor.fetchall()

            if resultats:
                for resultat in resultats:
                    self.comboBox_livre.addItem(resultat[0])

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui ajoute les joueurs entrés dans le comboBox des sauvegardes
    def ajouter_joueurs_comboBox(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT nom_joueur FROM joueur")
            resultats = cursor.fetchall() 

            if resultats:
                for resultat in resultats:
                    self.comboBox_sauvegarde.addItem(resultat[0])

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")



######FIN FONCTIONS DÉBUT###################################################################################################################################

#####FONCTIONS DE CHAPITRE##########################################################################################################################################
    #Fonction qui affiche les informations du livre et le premier chapitre de celui-ci
    #Déclenchée par un click selon le livre sélectionné
    def commencerHistoire(self):
        self.label_histoireChapitre_2.clear()
        self.comboBox_histoire.clear()
        livre_selectionne = self.comboBox_livre.currentText()
        try:
            cursor = self.connection.cursor()

            query_select_idChapitre = 'SELECT MIN(id_chapitre) FROM chapitres c INNER JOIN livres l ON c.id_livre = l.id_livre WHERE l.titre_livre = %s'
            cursor.execute(query_select_idChapitre, (livre_selectionne,))
            _id_premier_chapitre = cursor.fetchone()[0]

            select_histoire = "SELECT c.texte, l.titre_livre, c.no_chapitre FROM chapitres c INNER JOIN livres l ON c.id_livre = l.id_livre WHERE l.titre_livre = %s AND c.id_chapitre = %s"
            cursor.execute(select_histoire, (livre_selectionne, _id_premier_chapitre,) )
            resultats = cursor.fetchall()

            if resultats:
                for resultat in resultats:
                    self.textBrowser_histoire.setText(resultat[0])

                    self.label_titreLivre.setWordWrap(True)
                    self.label_titreLivre.setMaximumWidth(771)
                    self.label_titreLivre.setText(resultat[1])

                    self.label_histoireChapitre_2.setText(resultat[2])

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui affiche le premier chapitre (1) seulement d'un livre sélectionné dans le comboBox des choix de chapitre 
    def afficher_premierChapitre(self, titre_livre_selectionne):
        try:
            cursor = self.connection.cursor()
            select_histoire = "SELECT c.no_chapitre FROM chapitres c INNER JOIN livres l ON c.id_livre = l.id_livre	WHERE c.no_chapitre = %s AND titre_livre = %s"
            cursor.execute(select_histoire, ('1', titre_livre_selectionne,) )
            resultats = cursor.fetchall()  

            if resultats:
                for resultat in resultats:
                    self.comboBox_histoire.addItem(resultat[0])
                  

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui affiche les informations du livre selon la position du joueur dans le livre et affiche ces informations
    def cest_parti(self):
        chapitre_selectionne = self.comboBox_histoire.currentText()
        livre_selectionne = self.comboBox_livre.currentText()
        if self.comboBox_histoire.count() == 0:
            self.afficher_premierChapitre(livre_selectionne)

        else:
            try:
                cursor = self.connection.cursor()
                select_histoire = "SELECT c.texte, c.no_chapitre FROM livres l INNER JOIN chapitres c ON l.id_livre = c.id_livre INNER JOIN liens_chapitres lc ON c.id_chapitre = lc.no_chapitre_origine WHERE c.no_chapitre = %s AND l.titre_livre = %s"
                cursor.execute(select_histoire, (chapitre_selectionne, livre_selectionne,) )
                resultats = cursor.fetchall()  

                if resultats:
                    for resultat in resultats:
                        self.textBrowser_histoire.setText(resultat[0])

                        self.label_histoireChapitre_2.setText(resultat[1])
                        valeur_chapitreActuel = self.label_histoireChapitre_2.text()
                        self.afficher_chapitresDestination(valeur_chapitreActuel)

            except mysql.connector.Error as err:
                print(f"Erreur MySQL : {err}")

    #Fonction qui affiche les choix de chapitre selon la position du joueur dans le livre (selon son chapitre)
    def afficher_chapitresDestination(self, valeur_chapitreActuel):
        self.comboBox_histoire.clear()
        try:
            cursor = self.connection.cursor()
            select_histoire = 'SELECT lc.no_chapitre_destination FROM chapitres c INNER JOIN liens_chapitres lc ON c.id_chapitre = lc.no_chapitre_origine	WHERE lc.no_chapitre_origine = %s'
            cursor.execute(select_histoire, (valeur_chapitreActuel,) )
            resultats = cursor.fetchall()  

            if resultats:
                for resultat in resultats:
                    self.comboBox_histoire.addItem(str(resultat[0]))

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")



###FIN CHAPITRES#########################################################################################################################################

###SAUVEGARDE############################################################################################################################################
    #Fonction qui se déclenche lorsqu'on clique sur le bouton Nouvelle Partie
    def nouvellePartie(self):
        self.clear_all_widgets()
        nomSaisi = self.lineEdit_nom.text()
        #Pour savoir si l'usager a entré un nom pour la sauvegarde. Si oui, il va effectuer l'insertion du nom dans la BD
        if not nomSaisi:
            QMessageBox.warning(self, 'CHAMP VIDE', 'Pour sauvegarder, il faut un nom de sauvegarde')
            return
        else:
            self.label_nomGrand.setText(nomSaisi)
            self.insererJoueur(nomSaisi)
            self.initialisation_inserts(nomSaisi)

    #Fonction qui clear les widgets voulus
    def clear_all_widgets(self):
        self.textBrowser_histoire.clear()
        self.comboBox_histoire.clear()
        self.listWidget_disciplines.clear()
        self.listWidget_armes.clear()
        self.textEdit_objet_sac.clear()
        self.textEdit_repas_sac.clear()
        self.textEdit_os_sac.clear()
        self.spinBox_bourse_sac.clear()
        self.label_histoireChapitre_2.clear()

    #Fonction qui se déclenche lorsqu'on clique sur le bouton sauvegarde et qui effectue des updates de mes tables voulues
    def sauvegarder(self):
        v_nom_joueur_grand = self.label_nomGrand.text()
        if v_nom_joueur_grand == "Nom personnage" or v_nom_joueur_grand == "":
            QMessageBox.warning(self, 'ERREUR DE SAUVEGARDE', 'Vous n\'avez pas de noms de sauvegarde. Vous devez en avoir un afin de procéder.')
            return 

        v_nom_joueur = self.lineEdit_nom.text()
        v_titreLivre = self.comboBox_livre.currentText()
        v_chapitreActuel = self.label_histoireChapitre_2.text()

        v_objets = self.textEdit_objet_sac.toPlainText()
        v_repas = self.textEdit_repas_sac.toPlainText()
        v_objets_speciaux = self.textEdit_os_sac.toPlainText()
        v_bourse = self.spinBox_bourse_sac.value()


        self.update_sac(v_objets, v_repas, v_objets_speciaux, v_bourse, v_nom_joueur)
        
        self.update_id_inventaire(v_nom_joueur_grand)

        for index in range(self.listWidget_disciplines.count()):
            item = self.listWidget_disciplines.item(index)
            if item.text():
                item_discipline_selectionne = item.text()
                self.update_disciplines(item_discipline_selectionne, v_nom_joueur)

        for index in range(self.listWidget_armes.count()):
            item = self.listWidget_armes.item(index)
            if item.text():
                item_arme_selectionne = item.text()
                self.update_armes(item_arme_selectionne, v_nom_joueur)
                
        self.update_sauvegarde(v_chapitreActuel, v_titreLivre, v_nom_joueur)
        QMessageBox.warning(self, 'SAUVEGARDE', 'Sauvegarde réussie!')

    #Fonction qui se déclenche lorsqu'on charge la sauvegarde (clique sur le bouton Charger). Il affiche les données selon le nom du joueur (nom de la sauvegarde)
    def chargerSauvegarde(self):
        nom_sauvegarde = self.comboBox_sauvegarde.currentText()
        self.label_nomGrand.setText(nom_sauvegarde)

        try:
            cursor = self.connection.cursor()

            select_sauvegarde = 'SELECT s.id_sauvegarde, s.id_chapitre, s.id_livre, s.id_fiche_personnage, s.id_joueur FROM sauvegardes s INNER JOIN joueur j ON s.id_joueur = j.id_joueur WHERE j.nom_joueur = %s'
            cursor.execute(select_sauvegarde, (nom_sauvegarde,))
            resultats_sauvegarde = cursor.fetchall()

            if resultats_sauvegarde:
                premiere_ligne = resultats_sauvegarde[0]

                id_sauvegarde = premiere_ligne[0]
                id_chapitre = premiere_ligne[1]
                id_livre = premiere_ligne[2]
                id_fiche_personnage = premiere_ligne[3]
                id_joueur = premiere_ligne[4]

                _ins_no_chapitre = self.obtenir_no_chapitre(id_chapitre)
                self.label_histoireChapitre_2.setText(_ins_no_chapitre)

                _ins_titre_livre = self.obtenir_titre_livre(id_livre)
                self.label_titreLivre.setWordWrap(True)
                self.label_titreLivre.setMaximumWidth(771)
                self.label_titreLivre.setText(_ins_titre_livre)

                _ins_texte_chapitre = self.obtenir_texte_chapitre(id_chapitre, _ins_titre_livre)
                self.textBrowser_histoire.setText(_ins_texte_chapitre)
                valeur_chapitreActuel = self.label_histoireChapitre_2.text()
                self.afficher_chapitresDestination(valeur_chapitreActuel)
            
            select_sac = 'SELECT id_sac_a_dos, id_inventaire FROM fiche_personnage WHERE id_fiche_personnage = %s'
            cursor.execute(select_sac, (id_fiche_personnage,))
            resultats_sac = cursor.fetchall()
            
            if resultats_sac:
                premiere_ligne = resultats_sac[0]
                id_sac_a_dos = premiere_ligne[0]
                id_inventaire = premiere_ligne[1]

                _ins_objet = self.obtenir_objet(id_sac_a_dos)
                self.textEdit_objet_sac.setPlainText(_ins_objet)
                _ins_repas = self.obtenir_repas(id_sac_a_dos)
                self.textEdit_repas_sac.setPlainText(_ins_repas)
                _ins_objspec = self.obtenir_objspec(id_sac_a_dos)
                self.textEdit_os_sac.setPlainText(_ins_objspec)
                _ins_bourse = self.obtenir_bourse(id_sac_a_dos)
                self.spinBox_bourse_sac.setValue(_ins_bourse or 0)

            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")



###FIN SAUVEGARDE############################################################################################################################################

###DEBUT OBTENTION VALEURS TEXTES DES ID############################################################################################################################################
    #Fonction qui obtient le no de chapitre selon le id_chapitre
    #@id_chapitre Le id d'un chapitre
    def obtenir_no_chapitre(self, id_chapitre):
        try:
            cursor = self.connection.cursor()

            select_no_chapitre = 'SELECT no_chapitre FROM chapitres WHERE id_chapitre = %s'
            cursor.execute(select_no_chapitre, (id_chapitre,))
            resultat = cursor.fetchone()
            if resultat:
                no_chapitre = resultat[0]
                return no_chapitre
            
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui obtient le titre d'un livre selon le id d'un livre
    #@id_livre Le id d'un livre
    def obtenir_titre_livre(self, id_livre):
        try:
            cursor = self.connection.cursor()

            select_titre_livre = 'SELECT titre_livre FROM livres WHERE id_livre = %s'
            cursor.execute(select_titre_livre, (id_livre,))
            resultat = cursor.fetchone()
            if resultat:
                titre_livre = resultat[0]
                return titre_livre

            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui obtient le texte d'un chapitre selon le id d'un chapitre et le titre d'un livre
    #@id_chapitre Le id d'un chapitre 
    #@titre_livre Le titre d'un livre
    def obtenir_texte_chapitre(self, id_chapitre, titre_livre):
        try:
            cursor = self.connection.cursor()
            select_texteChap = "SELECT texte FROM chapitres c INNER JOIN livres l ON c.id_livre = l.id_livre WHERE c.id_chapitre = %s AND l.titre_livre = %s";
            cursor.execute(select_texteChap, (id_chapitre, titre_livre,))
            resultat = cursor.fetchone()
            if resultat:
                texte = resultat[0]
                return texte

            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui obtient un objet selon le id d'un sac à dos
    #@id_sac Le id d'un sac à dos
    def obtenir_objet(self, id_sac):
        try:
            cursor = self.connection.cursor()

            select_objet = 'SELECT objet FROM sac_a_dos WHERE id_sac_a_dos = %s'
            cursor.execute(select_objet, (id_sac,))
            resultat = cursor.fetchone()
            if resultat:
                objet = resultat[0]
                return objet

            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui obtient un repas selon le id d'un sac à dos
    #@id_sac Le id d'un sac à dos
    def obtenir_repas(self, id_sac):
        try:
            cursor = self.connection.cursor()

            select_repas = 'SELECT repas FROM sac_a_dos WHERE id_sac_a_dos = %s'
            cursor.execute(select_repas, (id_sac,))
            resultat = cursor.fetchone()
            if resultat:
                repas = resultat[0]
                return repas

            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui obtient des objets spéciaux selon le id d'un sac à dos
    #@id_sac Le id d'un sac à dos
    def obtenir_objspec(self, id_sac):
        try:
            cursor = self.connection.cursor()

            select_objspec = 'SELECT objets_speciaux FROM sac_a_dos WHERE id_sac_a_dos = %s'
            cursor.execute(select_objspec, (id_sac,))
            resultat = cursor.fetchone()
            if resultat:
                objspec = resultat[0]
                return objspec

            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui obtient la valeur de la bourse selon le id d'un sac à dos
    #@id_sac Le id d'un sac à dos
    def obtenir_bourse(self, id_sac):
        try:
            cursor = self.connection.cursor()

            select_bourse = 'SELECT valeur_bourse FROM sac_a_dos WHERE id_sac_a_dos = %s'
            cursor.execute(select_bourse, (id_sac,))
            resultat = cursor.fetchone()
            if resultat:
                if resultat is not None:
                    bourse = resultat[0]
                    return bourse
                else:
                    bourse = ""
                    return bourse

            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")



###FIN OBTENTION VALEURS TEXTES DES ID############################################################################################################################################

###DEBUT APPELS FONCTIONS / PROCEDURE############################################################################################################################################
    #Fonction qui insère un joueur en utilisant la procédure insert_joueur
    #@nom_joueur Le nom d'un joueur
    def insererJoueur(self, nom_joueur):
        try:
            cursor = self.connection.cursor()

            # Vérifier si le nom de joueur existe déjà
            cursor.execute('SELECT 1 FROM joueur WHERE nom_joueur = %s', (nom_joueur,))
            existe_deja = cursor.fetchone()

            if existe_deja:
                QMessageBox.warning(self, 'DUPLICAT NOMS', 'Ce nom de joueur existe déjà. Veuillez choisir un autre nom.')
                return
            else:
                # Insérer le nom dans la table
                procedure_insert_joueur = 'CALL insert_joueur(%s)'
                cursor.execute(procedure_insert_joueur, (nom_joueur,))
                self.connection.commit()
                self.comboBox_sauvegarde.addItem(nom_joueur)
                QMessageBox.information(self, 'SUCCÈS', 'Nom inséré avec succès!')

            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui effectue des inserts avec des nulls selon le nom d'un joueur (nom de sauvegarde)
    #@nom_joueur Le nom d'un joueur
    def initialisation_inserts(self, nom_joueur):
        try:
            cursor = self.connection.cursor()
            
            procedure_initialisation = 'CALL initialiser_insert(%s)'
            cursor.execute(procedure_initialisation, (nom_joueur,))
            self.connection.commit()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui update les informations (si reçues) d'un sac à dos selon le nom d'un joueur
    #@_objet Objet du sac à dos
    #@_objet Repas du sac à dos
    #@_objet Objet spécial du sac à dos
    #@_objet Valeur de la bourse du sac à dos
    #@nom_joueur Le nom d'un joueur
    def update_sac(self, _objet, _repas, _objets_speciaux, _bourse, _nom_joueur):
        try:
            cursor = self.connection.cursor()

            query_select_id_sac = 'SELECT sad.id_sac_a_dos FROM sac_a_dos sad INNER JOIN fiche_personnage fp ON sad.id_sac_a_dos = fp.id_sac_a_dos INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage INNER JOIN joueur j ON s.id_joueur = j.id_joueur WHERE j.nom_joueur = %s'
            cursor.execute(query_select_id_sac, (_nom_joueur,))
            resultat_id_sac = cursor.fetchone()
            if resultat_id_sac is not None:
                _id_sac_a_dos = resultat_id_sac[0]
                query_update = 'UPDATE sac_a_dos SET objet = COALESCE(%s, objet), repas = COALESCE(%s, repas), objets_speciaux = COALESCE(%s, objets_speciaux), valeur_bourse = COALESCE(%s, valeur_bourse) WHERE id_sac_a_dos = %s'
                cursor.execute(query_update, (_objet, _repas, _objets_speciaux, _bourse, _id_sac_a_dos,)) 
                self.connection.commit()
            else:
                print("Aucun id sac trouvé")       
            
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui update les informations (si reçues) de la fiche personnage, soit le id de l'inventaire selon le nom d'un joueur
    #Le id inventaire doit avoir le même id que le joueur sélectionné
    #@nom_joueur Le nom d'un joueur
    def update_id_inventaire(self, _nom_joueur):
        try:
            cursor = self.connection.cursor()
            select_id_joueur = 'SELECT id_joueur FROM joueur WHERE nom_joueur = %s'
            cursor.execute(select_id_joueur, (_nom_joueur,))
            _id_joueur = cursor.fetchone()[0]

            select_fiche = 'SELECT fp.id_fiche_personnage FROM fiche_personnage fp INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage INNER JOIN joueur j ON s.id_joueur = j.id_joueur WHERE j.id_joueur = %s'
            cursor.execute(select_fiche, (_id_joueur,)) 
            _id_fiche = cursor.fetchone()[0]  

            select_id_inventaire = 'SELECT id_inventaire FROM inventaire_general WHERE id_inventaire = %s'
            cursor.execute(select_id_inventaire, (_id_joueur,))
            id_inventaire_exists = cursor.fetchone()

            if not id_inventaire_exists:
                insert_inventaire = 'INSERT INTO inventaire_general (id_inventaire) VALUES (%s)'
                cursor.execute(insert_inventaire, (_id_joueur,))
                self.connection.commit()

            query_update_id_inventaire = 'UPDATE fiche_personnage SET id_inventaire = COALESCE(%s, id_inventaire) WHERE id_fiche_personnage = %s'
            cursor.execute(query_update_id_inventaire, (_id_joueur, _id_fiche,))
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui update les disciplines de la table inventaire_disciplines selon le nom de joueur
    #@_nom_disciplines Le nom des disciplines
    #@nom_joueur Le nom d'un joueur
    def update_disciplines(self, _nom_disciplines, _nom_joueur):
        try:
            cursor = self.connection.cursor()

            query_select_id_inventaire = 'SELECT id_inventaire FROM fiche_personnage fp INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage INNER JOIN joueur j ON s.id_joueur = j.id_joueur WHERE j.nom_joueur = %s'
            cursor.execute(query_select_id_inventaire, (_nom_joueur,))
            _id_inventaire = cursor.fetchone()[0]

            query_select_id_discipline = 'SELECT id_discipline FROM disciplines_kai dk WHERE dk.nom_discipline = %s'
            cursor.execute(query_select_id_discipline, (_nom_disciplines,))
            _id_discipline = cursor.fetchone()[0]
            
            query_update_inv_disciplines = 'UPDATE inventaire_disciplines SET id_discipline = COALESCE(%s, id_discipline) WHERE id_inventaire_discipline = %s'
            cursor.execute(query_update_inv_disciplines, (_id_discipline, _id_inventaire,))
            self.connection.commit()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui update les armes de la table inventaire_armes selon le nom de joueur
    #@_nom_armes Le nom des armes
    #@nom_joueur Le nom d'un joueur
    def update_armes(self, _nom_armes, _nom_joueur):
        try:
            cursor = self.connection.cursor()

            query_select_id_inventaire = 'SELECT id_inventaire FROM fiche_personnage fp INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage INNER JOIN joueur j ON s.id_joueur = j.id_joueur WHERE j.nom_joueur = %s'
            cursor.execute(query_select_id_inventaire, (_nom_joueur,))
            _id_inventaire = cursor.fetchone()[0]

            query_select_id_arme = 'SELECT id_arme FROM armes a WHERE a.nom_arme = %s'
            cursor.execute(query_select_id_arme, (_nom_armes,))
            _id_arme = cursor.fetchone()[0]
            
            query_update_inv_armes = 'UPDATE inventaire_armes SET id_arme = COALESCE(%s, id_arme) WHERE id_inventaire_arme = %s'
            cursor.execute(query_update_inv_armes, (_id_arme, _id_inventaire,))
            self.connection.commit()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui update les sauvegardes selon le nom de joueur
    #@_no_chapitre Le no de chapitre
    #@_titre_livre Le titre du livre
    #@nom_joueur Le nom d'un joueur
    def update_sauvegarde(self, _no_chapitre, _titre_livre, _nom_joueur):
        try:
            cursor = self.connection.cursor()
            
            query_select_id_joueur = 'SELECT id_joueur FROM joueur WHERE nom_joueur = %s'
            cursor.execute(query_select_id_joueur, (_nom_joueur,))
            resultat_joueur = cursor.fetchone()
            if resultat_joueur is not None:
                _id_joueur = resultat_joueur[0]
            else:
                _id_joueur = ""
            
            query_select_id_livre = 'SELECT id_livre FROM livres WHERE titre_livre = %s'
            cursor.execute(query_select_id_livre, (_titre_livre,))
            resultat_livre = cursor.fetchone()
            if resultat_livre is not None:
                _id_livre = resultat_livre[0]
            else:
                _id_livre = ""

            query_select_id_chapitre = 'SELECT id_chapitre FROM chapitres c	INNER JOIN livres l ON c.id_livre = l.id_livre WHERE no_chapitre = %s  AND l.id_livre = %s';
            cursor.execute(query_select_id_chapitre, (_no_chapitre, _id_livre,))
            resultat_chapitre = cursor.fetchone()
            if resultat_chapitre is not None:
                _id_chapitre = resultat_chapitre[0]
            else:
                _id_chapitre = ""
            
            query_update_sauvegarde = 'UPDATE sauvegardes SET id_chapitre = COALESCE(%s, id_chapitre), id_livre = COALESCE(%s, id_livre) WHERE id_joueur = %s'
            cursor.execute(query_update_sauvegarde, (_id_chapitre, _id_livre, _id_joueur,))
            self.connection.commit()
            cursor.close()

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

    #Fonction qui supprime la sauvegarde selon le nom du joueur (nom de la sauvegarde)
    def supprimer_sauvegarde(self):
        sauvegarde_selectionnee = self.comboBox_sauvegarde.currentText()
        try:
            cursor = self.connection.cursor()

            query_select_id_joueur = 'SELECT id_joueur FROM joueur WHERE nom_joueur = %s'
            cursor.execute(query_select_id_joueur, (sauvegarde_selectionnee,))
            _id_joueur = cursor.fetchone()[0]

            # Supprimer la sauvegarde associée au joueur
            delete_sauvegarde = 'DELETE FROM sauvegardes WHERE id_joueur = %s'
            cursor.execute(delete_sauvegarde, (_id_joueur,))

            delete_joueur = 'DELETE FROM joueur WHERE id_joueur = %s'
            cursor.execute(delete_joueur, (_id_joueur,))

            self.connection.commit()
            cursor.close()

            index_a_supprimer = self.comboBox_sauvegarde.findText(sauvegarde_selectionnee)
            if index_a_supprimer != -1:
                self.comboBox_sauvegarde.removeItem(index_a_supprimer)

        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
