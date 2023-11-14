USE hdvelh_tpsommatif;

SELECT lc.no_chapitre_destination FROM liens_chapitres lc
	INNER JOIN chapitres c ON lc.no_chapitre_origine = c.id_chapitre 
	WHERE c.id_chapitre = 5;

SELECT * FROM disciplines_kai;

SELECT * FROM armes;

SELECT * FROM liens_chapitres;

SELECT * FROM livres;

SELECT * FROM chapitres;
 