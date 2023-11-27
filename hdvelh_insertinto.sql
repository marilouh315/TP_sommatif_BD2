/*
* Fichier de création des INSERT INTO des tables livres, disciplines_kai, armes, et chapitres 
* (pour les livres Livre 2 et Livre 3, par exemple)
*  
* Fichier : hdvelh_insertinto.sql
* Auteur : Marilou Héon
* Langage : SQL
* Date : 27 novembre 2023
*/

USE hdvelh_tpsommatif;

#INSERT INTO livres#####################################################################################
INSERT IGNORE INTO livres (titre_livre) VALUES ("Les Maîtres des Ténèbres - Loup Solitaire");
INSERT IGNORE INTO livres (titre_livre) VALUES ("Livre 2");
INSERT IGNORE INTO livres (titre_livre) VALUES ("Livre 3");

#INSERT INTO disciplines_kai############################################################################
INSERT IGNORE INTO disciplines_kai (nom_discipline) VALUES ("Camouflage");
INSERT IGNORE INTO disciplines_kai (nom_discipline) VALUES ("Chasse");
INSERT IGNORE INTO disciplines_kai (nom_discipline) VALUES ("Sixième sens");
INSERT IGNORE INTO disciplines_kai (nom_discipline) VALUES ("Orientation");
INSERT IGNORE INTO disciplines_kai (nom_discipline) VALUES ("Guérison");
INSERT IGNORE INTO disciplines_kai (nom_discipline) VALUES ("Maitrise des armes");
INSERT IGNORE INTO disciplines_kai (nom_discipline) VALUES ("Bouclier psychique");
INSERT IGNORE INTO disciplines_kai (nom_discipline) VALUES ("Puissance psychique");
INSERT IGNORE INTO disciplines_kai (nom_discipline) VALUES ("Communication animale");
INSERT IGNORE INTO disciplines_kai (nom_discipline) VALUES ("Maitrise psychique de la matière");

#INSERT INTO armes######################################################################################
INSERT IGNORE INTO armes (nom_arme) VALUES ("Poignard");
INSERT IGNORE INTO armes (nom_arme) VALUES ("Lance");
INSERT IGNORE INTO armes (nom_arme) VALUES ("Masse d'armes");
INSERT IGNORE INTO armes (nom_arme) VALUES ("Sabre");
INSERT IGNORE INTO armes (nom_arme) VALUES ("Marteau de guerre");
INSERT IGNORE INTO armes (nom_arme) VALUES ("Épée 5");
INSERT IGNORE INTO armes (nom_arme) VALUES ("Hache");
INSERT IGNORE INTO armes (nom_arme) VALUES ("Épee 7");
INSERT IGNORE INTO armes (nom_arme) VALUES ("Bâton");
INSERT IGNORE INTO armes (nom_arme) VALUES ("Glaive");

#INSERT INTO chapitres pour les Livre2 et Livre3######################################################################################
INSERT IGNORE INTO chapitres(no_chapitre, texte, id_livre) VALUES ('1', 'Voici le premier chapitre du Livre2', 2);
INSERT IGNORE INTO chapitres(no_chapitre, texte, id_livre) VALUES ('1', 'Chapitre 1 - Livre 3', 3);

