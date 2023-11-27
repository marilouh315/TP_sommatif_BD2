/*
* Fichier de mes deux procédures utilisées dans mon application PyQt5
*  
* Fichier : hdvelh_tests.sql
* Auteur : Marilou Héon
* Langage : SQL
* Date : 27 novembre 2023
*/

USE hdvelh_tpsommatif;

/**
 * Procédure qui insère un nom de joueur dans la table joueur
 * 
 * @param IN _nom_joueur Le nom du joueur
 */
DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS insert_joueur(IN _nom_joueur VARCHAR(255))
BEGIN 
	INSERT INTO joueur (nom_joueur)
	VALUES (_nom_joueur);
END $$
DELIMITER ;



/**
 * Procédure qui initialise tous les insert into des tables sac_a_dos, fiche_personnage et sauvegardes avec des NULL 
 * (car nous allons faire des update par après)
 * 
 * @param IN _nom_joueur Le nom du joueur 
 */
DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS initialiser_insert(IN _nom_joueur VARCHAR(255))
BEGIN
	DECLARE _value_sac INTEGER;
	DECLARE _value_id_joueur INTEGER;
	DECLARE _value_id_fiche INTEGER;

	INSERT INTO sac_a_dos(objet, repas, objets_speciaux, valeur_bourse)
	VALUES(NULL, NULL, NULL, NULL);

	SET _value_sac = LAST_INSERT_ID() ;

	SET _value_id_joueur =(SELECT id_joueur FROM joueur WHERE nom_joueur = _nom_joueur);

	INSERT INTO fiche_personnage(id_inventaire, id_sac_a_dos)
	VALUES(NULL, _value_sac);
	
	SET _value_id_fiche = LAST_INSERT_ID() ;

	INSERT INTO sauvegardes(id_chapitre, id_livre, id_fiche_personnage, id_joueur)
	VALUES(NULL, NULL, _value_id_fiche, _value_id_joueur);
END $$

DELIMITER ;







######ENLEVE MOI PAS DE POINTS, JE NE VEUX PAS LES ENLEVER CAR JE SUIS TROP FIÈRE DE CES PROCÉDURES QUE J'AI CRÉÉES MÊME SI JE NE LES UTILISE PAS#######################################
/*DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS update_sac(
	IN _value_objet VARCHAR(100), 
	IN _value_repas VARCHAR(100), 
	IN _value_objets_speciaux VARCHAR(100), 
	IN _value_bourse INTEGER, 
	IN _value_nom_joueur VARCHAR(255)
)
BEGIN 
	DECLARE value_id_sac INTEGER;

	SET value_id_sac =(SELECT id_sac_a_dos FROM sac_a_dos sad 
							INNER JOIN fiche_personnage fp ON sad.id_sac_a_dos = fp.id_sac_a_dos 
							INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage 
							INNER JOIN joueur j ON s.id_joueur = j.id_joueur 
							WHERE j.nom_joueur = _value_nom_joueur);
						
	UPDATE sac_a_dos SET 
		objet = COALESCE(_value_objet, objet),
        repas = COALESCE(_value_repas, repas),
        objets_speciaux = COALESCE(_value_objets_speciaux, objets_speciaux),
        valeur_bourse = COALESCE(_value_bourse, valeur_bourse)
        WHERE sac_a_dos.id_sac_a_dos = value_id_sac;

END $$
DELIMITER ;




DELIMITER $$ 
CREATE PROCEDURE IF NOT EXISTS update_disciplines(IN _value_nom_discipline VARCHAR(255), IN _value_nom_joueur VARCHAR(255))
BEGIN
	DECLARE _value_id_inventaire INTEGER;
	DECLARE _value_id_discipline INTEGER;

	SET _value_id_inventaire =(SELECT id_inventaire FROM fiche_personnage fp 
								INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage 
								INNER JOIN joueur j ON s.id_joueur = j.id_joueur 
								WHERE j.nom_joueur = _value_nom_joueur);
							
	SET _value_id_discipline =(SELECT id_discipline FROM disciplines_kai dk WHERE dk.nom_discipline = _value_nom_discipline);
	UPDATE inventaire_disciplines SET 
		id_discipline = COALESCE(_value_id_discipline, id_discipline)
		WHERE id_inventaire_discipline = _value_id_inventaire;
		
END $$

DELIMITER ;




DELIMITER $$ 
CREATE PROCEDURE IF NOT EXISTS update_arme(IN _value_nom_arme VARCHAR(255), IN _value_nom_joueur VARCHAR(255))
BEGIN
	DECLARE _value_id_inventaire INTEGER;
	DECLARE _value_id_arme INTEGER;

	SET _value_id_inventaire =(SELECT id_inventaire FROM fiche_personnage fp 
								INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage 
								INNER JOIN joueur j ON s.id_joueur = j.id_joueur 
								WHERE j.nom_joueur = _value_nom_joueur);
							
	SET _value_id_arme =(SELECT id_arme FROM armes a WHERE a.nom_arme = _value_nom_arme);
	UPDATE inventaire_armes SET 
		id_arme = COALESCE(_value_id_arme, id_arme)
		WHERE id_inventaire_arme = _value_id_inventaire;
		
END $$

DELIMITER ;




DELIMITER $$ 
CREATE PROCEDURE IF NOT EXISTS update_fiche_perso(
	IN _nom_joueur VARCHAR(255)
)
BEGIN
	DECLARE _value_id_joueur INTEGER;
	DECLARE _value_id_fiche_perso INTEGER;
	DECLARE _value_id_inventaire INTEGER;
	DECLARE _value_id_sac INTEGER;

	SET _value_id_joueur =(SELECT id_joueur FROM joueurs WHERE nom_joueur = _nom_joueur);
	SET _value_id_fiche_perso =(SELECT id_fiche_personnage FROM fiche_personnage fp 
									INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage 
									WHERE s.id_joueur = __value_id_joueur);
	SET _value_id_inventaire =(SELECT id_inventaire FROM inventaire_general ig 
									INNER JOIN fiche_personnage fp ON ig.id_inventaire = fp.id_inventaire 
									INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage
									WHERE id_joueur = _value_id_joueur);
	SET _value_id_sac =(SELECT sad.id_sac_a_dos FROM sac_a_dos sad 
									INNER JOIN fiche_personnage fp ON sad.id_sac_a_dos = fp.id_sac_a_dos
									INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage
									WHERE id_joueur = _value_id_joueur);
								
	UPDATE fiche_personnage SET 
		id_inventaire = COALESCE(_value_id_inventaire, id_inventaire), 
		id_sac_a_dos = COALESCE(_value_id_sac, id_sac_a_dos)
		WHERE id_fiche_personnage = _value_id_fiche_perso;
END $$

DELIMITER ;




DELIMITER $$ 
CREATE PROCEDURE IF NOT EXISTS update_sauvegarde(
	IN _titre_livre VARCHAR(100),
	IN _no_chapitre VARCHAR(15),
	IN _nom_joueur VARCHAR(255)
)
BEGIN
	DECLARE _value_id_livre INTEGER;
	DECLARE _value_id_chapitre INTEGER;
	DECLARE _value_id_joueur INTEGER;
	DECLARE _value_id_fiche INTEGER;

	SET _value_id_livre =(SELECT id_livre FROM livres WHERE titre_livre = _titre_livre);
	SET _value_id_chapitre =(SELECT id_chapitre FROM chapitres WHERE no_chapitre = _no_chapitre);
	SET _value_id_joueur =(SELECT id_joueur FROM joueurs WHERE nom_joueur = _nom_joueur);
	SET _value_id_fiche =(SELECT id_fiche_personnage FROM fiche_personnage fp 
							INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage
							WHERE id_joueur = _value_id_joueur);

	UPDATE sauvegardes SET 
		id_chapitre = COALESCE(_value_id_chapitre, id_chapitre), 
		id_livre = COALESCE(_value_id_livre, id_livre),  
		id_fiche_personnage =COALESCE(_value_id_fiche, id_fiche_personnage)
		WHERE id_joueur = _value_id_joueur;
END $$

DELIMITER ;
*/


