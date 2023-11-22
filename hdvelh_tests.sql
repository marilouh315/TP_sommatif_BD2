USE hdvelh_tpsommatif;
SELECT * FROM livres l;
SELECT * FROM disciplines_kai dk;
SELECT * FROM armes a ;
SELECT * FROM chapitres c ;
SELECT * FROM liens_chapitres lc;
/*
SELECT * FROM chapitres WHERE id_livre = 2;
SELECT l.titre_livre, c.texte, c.no_chapitre FROM chapitres c 
	INNER JOIN livres l ON c.id_livre = l.id_livre 
	WHERE l.id_livre = 1 AND id_chapitre = 1;


SELECT c.texte, lc.no_chapitre_destination FROM livres l
	INNER JOIN chapitres c ON l.id_livre = c.id_livre 
	INNER JOIN liens_chapitres lc ON c.id_chapitre = lc.no_chapitre_origine
	WHERE c.no_chapitre  = '1';


SELECT lc.no_chapitre_destination, lc.no_chapitre_origine FROM chapitres c
	INNER JOIN liens_chapitres lc ON c.id_chapitre = lc.no_chapitre_origine
	WHERE lc.no_chapitre_origine = "1";
	

SELECT id_chapitre FROM chapitres c
	INNER JOIN livres l ON c.id_livre = l.id_livre 
	WHERE c.no_chapitre = '2' AND l.titre_livre = 'Les Maîtres des Ténèbres - Loup Solitaire';

SELECT id_livre FROM livres l
	WHERE l.titre_livre = 'Les Maîtres des Ténèbres - Loup Solitaire';

SELECT c.texte, l.titre_livre, c.no_chapitre FROM chapitres c 
INNER JOIN livres l ON c.id_livre = l.id_livre 
WHERE l.titre_livre = 'Les Maîtres des Ténèbres - Loup Solitaire' AND c.id_chapitre = '1';
*/



DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS insert_sac(IN _value_objet VARCHAR(100), IN _value_repas VARCHAR(100), IN _value_objets_speciaux VARCHAR(100), IN _value_bourse INTEGER)
BEGIN 
	INSERT INTO sac_a_dos (objet, repas, objets_speciaux, valeur_bourse)
	VALUES (_value_objet, _value_repas, _value_objets_speciaux, _value_bourse);

END $$
DELIMITER ;
CALL insert_sac('Fleurs', 'Poulet', 'Pommes dorées', 9);

SELECT * FROM sac_a_dos;

SELECT * FROM disciplines_kai dk;




DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS insert_joueur(IN _nom_joueur VARCHAR(255))
BEGIN 
	INSERT INTO joueur (nom_joueur)
	VALUES (_nom_joueur);
END $$
DELIMITER ;

SELECT * FROM joueur j ;



DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS insert_disciplines (IN _nom_discipline VARCHAR(255), IN _nom_joueur VARCHAR(255))
BEGIN
	DECLARE _value_id_joueur INTEGER;
	DECLARE _value_id_inventaire INTEGER;
	DECLARE _value_id_fiche INTEGER;
	DECLARE _value_id_discipline INTEGER;

	SET _value_id_joueur =(SELECT id_joueur FROM joueur WHERE nom_joueur = _nom_joueur);

	SET _value_id_inventaire =(SELECT id_inventaire FROM inventaire_general ig 
									INNER JOIN fiche_personnage fp ON ig.id_inventaire = fp.id_inventaire
									INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage
									WHERE s.id_joueur = _value_id_joueur);
								
	SET _value_id_fiche =(SELECT id_fiche_personnage FROM fiche_personnage fp INNER JOIN sauvegardes s ON fp.id_fiche_personnage = s.id_fiche_personnage WHERE s.id_joueur = _value_id_joueur);
							
	SET _value_id_discipline =(SELECT id_discipline FROM disciplines_kai WHERE nom_discipline = _nom_discipline);

	IF _value_id_inventaire IS NULL THEN
		INSERT INTO inventaire_general() 
       	VALUES();
        SET _value_id_inventaire = LAST_INSERT_ID();

        -- Associez l'inventaire au joueur
        UPDATE fiche_personnage
        SET id_inventaire = _value_id_inventaire
        WHERE id_fiche_personnage = _value_id_fiche;
    END IF;
 
	
	INSERT INTO inventaire_disciplines (id_discipline)
	VALUES(_value_id_inventaire, _value_id_discipline);
END $$
DELIMITER ;




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

SELECT * FROM sauvegardes s ;
SELECT * FROM joueur j;

/*
DELIMITER $$

CREATE PROCEDURE IF NOT EXISTS insert_sauvegarde(
	IN _no_chapitre VARCHAR(15),
	IN _titre_livre VARCHAR(100),
	IN _nom_joueur VARCHAR(255),
	IN _nom_discipline VARCHAR(255),
	IN _nom_arme VARCHAR(255)
)
BEGIN
	DECLARE _value_id_chapitre INTEGER;
	DECLARE _value_id_livre INTEGER;
	DECLARE _value_id_joueur INTEGER;
	DECLARE _value_id_discipline INTEGER;
	DECLARE _value_id_arme INTEGER;
	DECLARE _value_id_sac INTEGER;
	DECLARE _value_id_fiche INTEGER;


	SET _value_id_chapitre =(SELECT id_chapitre FROM chapitres c INNER JOIN livres l ON c.id_livre = l.id_livre WHERE c.no_chapitre = _no_chapitre AND l.titre_livre = _titre_livre);
	
	SET _value_id_livre =(SELECT id_livre FROM livres l	WHERE l.titre_livre = _titre_livre);
	
	SET _value_id_joueur =(SELECT id_joueur FROM joueur j WHERE j.nom_joueur = _nom_joueur);
	
	SET _value_id_discipline =(SELECT id_discipline FROM disciplines_kai d WHERE nom_discipline = _nom_discipline);
	
	SET _value_id_arme =(SELECT id_arme FROM armes a WHERE nom_arme = _nom_arme);
	
	SET _value_id_sac =(SELECT id_sac_a_dos FROM sac_a_dos s WHERE objet = _value_objet AND repas = _value_repas AND objets_speciaux = _value_objets_speciaux AND valeur_bourse = _value_bourse);
		
	INSERT INTO fiche_personnage (id_discipline, id_arme, id_sac_a_dos)
	VALUES (_value_id_discipline, _value_id_arme, _value_id_sac);
	
	SET _value_id_fiche =(LAST_INSERT_ID());

	INSERT INTO sauvegardes (id_chapitre, id_livre, id_fiche_personnage, id_joueur) 
 	VALUES (_value_id_chapitre, _value_id_livre, _value_id_fiche, _value_id_joueur);
END $$

DELIMITER ; 

CALL insert_sauvegarde('1', 'Les Maîtres des Ténèbres - Loup Solitaire', 'marilou', 'Camouflage');
*/



