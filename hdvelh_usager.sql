/*
* Fichier pour la création de mon usager avec des droits restreints
*  
* Fichier : hdvelh_usager.sql
* Auteur : Marilou Héon
* Langage : SQL
* Date : 27 novembre 2023
*/

USE hdvelh_tpsommatif; 

DROP USER IF EXISTS 'hdvelhUsager2'; 

CREATE USER 'hdvelhUsager2' IDENTIFIED BY 'mdp';

GRANT SELECT ON hdvelh_tpsommatif.armes TO 'hdvelhUsager2';
GRANT SELECT ON hdvelh_tpsommatif.disciplines_kai TO 'hdvelhUsager2';
GRANT SELECT, INSERT, UPDATE, DELETE ON hdvelh_tpsommatif.fiche_personnage TO 'hdvelhUsager2';
GRANT SELECT ON hdvelh_tpsommatif.liens_chapitres TO 'hdvelhUsager2';
GRANT SELECT, INSERT, DELETE ON hdvelh_tpsommatif.inventaire_armes TO 'hdvelhUsager2';
GRANT SELECT, INSERT, DELETE ON hdvelh_tpsommatif.inventaire_disciplines TO 'hdvelhUsager2';
GRANT SELECT ON hdvelh_tpsommatif.livres TO 'hdvelhUsager2';
GRANT SELECT, INSERT, UPDATE, DELETE ON hdvelh_tpsommatif.sauvegardes TO 'hdvelhUsager2';
GRANT SELECT ON hdvelh_tpsommatif.chapitres TO 'hdvelhUsager2';
GRANT SELECT, INSERT, DELETE ON hdvelh_tpsommatif.joueur TO 'hdvelhUsager2';
GRANT SELECT, INSERT, DELETE ON hdvelh_tpsommatif.sac_a_dos TO 'hdvelhUsager2';
