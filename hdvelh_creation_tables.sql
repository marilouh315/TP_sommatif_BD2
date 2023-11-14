
DROP DATABASE IF EXISTS hdvelh_tpsommatif;
CREATE DATABASE hdvelh_tpsommatif;
USE hdvelh_tpsommatif; 

#CREATION TABLES###############################################################################################
CREATE TABLE IF NOT EXISTS disciplines_kai (
	id_discipline INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom_discipline VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS armes (
	id_arme INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom_arme VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS sac_a_dos (
	id_sac_a_dos INTEGER PRIMARY KEY AUTO_INCREMENT,
	objet VARCHAR(100) NOT NULL, 
	repas VARCHAR(100) NOT NULL, 
	objets_speciaux VARCHAR(100) NOT NULL, 
	valeur_bourse INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS joueur (
	id_joueur INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom_joueur VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS livres (
	id_livre INTEGER PRIMARY KEY AUTO_INCREMENT,
	titre_livre VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS chapitres (
	id_chapitre INTEGER PRIMARY KEY AUTO_INCREMENT,
	no_chapitre VARCHAR(15) NOT NULL,
	texte TEXT NOT NULL,
	id_livre INTEGER NOT NULL,
	FOREIGN KEY (id_livre) REFERENCES livres (id_livre)
);

CREATE TABLE IF NOT EXISTS liens_chapitres (
	id_lien_chapitre INTEGER PRIMARY KEY AUTO_INCREMENT,
	no_chapitre_origine INTEGER NOT NULL,
	no_chapitre_destination INTEGER NOT NULL, 
	FOREIGN KEY (no_chapitre_origine) REFERENCES chapitres (id_chapitre),
	FOREIGN KEY (no_chapitre_destination) REFERENCES chapitres (id_chapitre)
);

CREATE TABLE IF NOT EXISTS fiche_personnage (
	id_fiche_personnage INTEGER PRIMARY KEY AUTO_INCREMENT,
	nom_personnage VARCHAR(255) NOT NULL,
	id_discipline INTEGER NOT NULL,
	id_arme INTEGER NOT NULL, 
	id_sac_a_dos INTEGER NOT NULL,
	FOREIGN KEY (id_discipline) REFERENCES disciplines_kai (id_discipline),
	FOREIGN KEY (id_arme) REFERENCES armes (id_arme),
	FOREIGN KEY (id_sac_a_dos) REFERENCES sac_a_dos (id_sac_a_dos)
);

CREATE TABLE IF NOT EXISTS sauvegardes (
	id_sauvegarde INTEGER PRIMARY KEY AUTO_INCREMENT,
	id_chapitre INTEGER NOT NULL,
	id_livre INTEGER NOT NULL,
	id_fiche_personnage INTEGER NOT NULL,
	id_joueur INTEGER NOT NULL,
	FOREIGN KEY (id_chapitre) REFERENCES chapitres (id_chapitre),
	FOREIGN KEY (id_livre) REFERENCES livres (id_livre),
	FOREIGN KEY (id_fiche_personnage) REFERENCES fiche_personnage (id_fiche_personnage), 
	FOREIGN KEY (id_joueur) REFERENCES joueur (id_joueur)
);


















