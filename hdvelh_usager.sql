/*
* Fichier pour la création de mon usager avec des droits restreints
*  
* Fichier : hdvelh_usager.sql
* Auteur : Marilou Héon
* Langage : SQL
* Date : 27 novembre 2023
*/

DROP USER IF EXISTS 'hdvelhUsager';

CREATE USER 'hdvelhUsager'@'%' IDENTIFIED BY 'mdp';

GRANT SELECT, INSERT, UPDATE, DELETE ON hdvelh_tpsommatif.* TO 'hdvelhUsager'@'localhost';

FLUSH PRIVILEGES;
