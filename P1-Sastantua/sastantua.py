# Le nombre donné en paramètre de la fonction principale correspond aux nombres d'étages de la pyramide.
# Si ce nombre <= 0, rien ne doit être dessiné.
# Aussi, en partant du sommet :
	# Le passage d'un bloc à un autre se fait en ajoutant n étoiles de chaque côté de la base du bloc précédent.
	# Ce nombre n s'incrémente de 1 tous les 2 étages parcourus et commence à 2.
	# Le nombre d'étage d'un bloc augmente de 1 par nouveau bloc et commence à 3.
# Une porte est placée sur le bloc qui constitue la base. Elle a la même hauteur que le nombre de blocs et sa largeur = hauteur si le nombre de blocs est impair, largeur = hauteur + 1 si le nombre de blocs est pair.. (elle est au milieu)
# Une poignée est placée sur la porte si sa largeur et sa hauteur sont au moins égales à 3.
# La poignée est placée sur la porte horizontalement à (largeur de la porte - 1) si la largeur est <3, sinon elle est placée à (largeur de la porte).
# La poignée est placée sur la porte verticalement à (la moitié de la hauteur de la porte) ème ligne en partant du bas  dans le cas d'une hauteur impaire, et à ((la division entière de la hauteur de la porte par 2) + 1) ème ligne en partant du bas dans le cas d'une hauteur paire.



# Définition des fonctions principales. (les noms de variables utilisés sont ceux utilisés dans la partie de définition des variables globales, un descriptif de l'utilité de chaque variable se trouve donc dans cette partie)
def CalculerNbEspacesInitial(nombreBlocs, hauteurSommet, incrHauteurSommet, incrEtoilesParLigne, incrEtoilesParEtage, incrIncrEtoilesParEtage, compteurNonIncr, incrCompteurNonIncr):
	"""
	Permet de calculer le nombre d'espaces blanc qui doivent se trouver entre le bord gauche de la console et l'étoile qui représente le sommet de la pyramide.

	Paramètres
	----------

	nombreBlocs : Le nombre de blocs constituant la pyramide. (int)
	hauteurSommet : La hauteur du sommet. (int)
	incrHauteurSommet : L'incrément sur la hauteur des blocs à chaque changement de bloc. (int)
	incrEtoilesParLigne : Le nombre d'étoiles que l'on rajoute à la fois à gauche et à droite de la ligne précédente dans le passage d'une ligne à l'autre dans un même bloc. (int)
	incrEtoilesParEtage : Le nombre initial d'étoiles que l'on rajoute à la fois à gauche et à droite de la ligne précédente dans le passage d'une ligne à l'autre quand on change de bloc. (int)
	incrIncrEtoilesParEtage : L'incrément de incrEtoilesParEtage.(int)
	compteurNonIncr : Le nombre d'étages sans incrémenter incrEtoilesParEtage. (int)
	incrCompteurNonIncr : L'incrément de incrCompteurNonIncr. (int)

	"""
	nbEspacesInitial = -1 # Ce nombre d'espaces correspond au nombre d'étoiles de la partie gauche de la base de la pyramide. (commence à -1 car on va incrémenter ce nombre pour la première ligne alors qu'il n'y a pas d'étoiles à gauche du centre, puisqu'il n'y a qu'une seule étoile)
	compteurVersCompteurNonIncr = 0 # Compteur vers la variable compteurNonIncr.

	for compteurVersNombreBlocs in range(0, nombreBlocs): # Boucler sur le nombre d'étages de la pyramide.
		for compteurVersHauteurSommet in range(0, hauteurSommet): # Pour chaque étage, boucler sur sa hauteur.
			nbEspacesInitial += incrEtoilesParLigne # Une étoile correspond à un espace, puisqu'on veut le nombre d'étoiles de la partie gauche de la base pour avoir le nombre d'espaces à gauche du sommet.
		if compteurVersCompteurNonIncr == compteurNonIncr: # Doit-on incrémenter l'incrément du nombre d'étoiles lors du passage d'un étage à l'autre.
			incrEtoilesParEtage += incrIncrEtoilesParEtage # Incrémentation de l'incrémentation du nombre d'étoiles lors du passage d'un étage à l'autre.
			compteurVersCompteurNonIncr = 0 # Reset du compteur.
			compteurNonIncr += incrCompteurNonIncr # Incrément du nombre d'étages à passer avant d'incrémenter l'incrément du nombre d'étoiles lors du passage d'un étage à l'autre.
		if compteurVersNombreBlocs < nombreBlocs - 1: # Si on n'est pas au dernier bloc. (le compteur commence à 0, mais le nombre de bloc vaut au minimum 1)
			nbEspacesInitial += incrEtoilesParEtage	 # Passage d'un étage à un autre, donc incrément du nombre d'espaces par un certain nombre.
		hauteurSommet += incrHauteurSommet # A chaque étage supplémentaire, la hauteur de étages augmente.
		compteurVersCompteurNonIncr += 1 # Incrémentation du compteur vers la variable compteurNonIncr.
	return nbEspacesInitial # Renvoyer le nombre d'espaces à gauche du sommet de la pyramide.



def ConstruireSastantua(nombreBlocs, hauteurSommet, incrHauteurSommet, incrEtoilesParLigne, incrEtoilesParEtage, incrIncrEtoilesParEtage, incrCompteurNonIncr, compteurNonIncr, hauteurPorte, largeurPorte, positionHorizontalePoignee, positionVerticalePoignee, nbEspacesInitial):
	ligneCourante = "" # Variable que l'on va afficher pour chaque ligne.
	etoilesLigneCourante = "*" # Nombre d'étoiles que comportera la ligne courante.
	espacesLigneCourante = "" # Nombre d'espaces que comportera la ligne courante.
	compteurVersCompteurNonIncr = 1

	# GESTION DES ETAGES.
	for compteurVersNombreBlocs in range(0, nombreBlocs): # Boucler sur le nombre d'étages de la pyramide.

		# GESTION DES LIGNES QUI COMPOSENT UN ETAGE.
		for compteurVersHauteurSommet in range(0, hauteurSommet): # Pour chaque étage, boucler sur sa hauteur.

			# GESTION DES ESPACES AVANT CHAQUE LIGNE AFFICHEE.
			for compteurVersNbEspacesInitial in range(0, nbEspacesInitial): # Boucler sur le nombre d'espace et créer ces espaces dans la ligne courante.
				espacesLigneCourante += " "

			# GESTION DE L'AFFICHAGE DE LA LIGNE COURANTE.
			ligneCourante = espacesLigneCourante + etoilesLigneCourante # Création de la ligne à afficher, composée d'un nombre d'espaces et d'un nombre d'étoiles.

			# Affichage particulier pour la porte du dernier étage. Remplacer certaines * par |.
			if compteurVersNombreBlocs == nombreBlocs - 1: # Si on est à l'étage constituant la base.
				barresLigneCourante = "" # Créer la ligne qui comporte à la fois les * et les |.
				if compteurVersHauteurSommet >= 2: # La porte part du bas de l'étage jusque hauteurEtage - 2.
					for compteurVersLongueurEtoilesLigneCourante in range(0, (int(len(etoilesLigneCourante) // 2)) - int(largeurPorte // 2)):
						barresLigneCourante += "*"
					for compteurVersLargeurPorte in range(0, largeurPorte):
						if nombreBlocs >= 3 and compteurVersLargeurPorte == positionHorizontalePoignee - 1 and compteurVersHauteurSommet == positionVerticalePoignee + 1: # Placement de la poignée. (range var jusque largeurPorte - 1, il faut donc encore retirer 1 pour placer la poignée sur largeurPorte - 1)
							barresLigneCourante += "$"
						else:
							barresLigneCourante += "|"
					for compteurVersLongueurEtoilesLigneCourante in range(0, (int(len(etoilesLigneCourante) // 2)) - int(largeurPorte // 2)):
						barresLigneCourante += "*"
					ligneCourante = espacesLigneCourante + barresLigneCourante
					
			print(ligneCourante) # Affichage de la ligne courante, le chariot passe à la ligne sur la console.
			espacesLigneCourante = "" # Reset du nombre d'espaces de la ligne, vu que celui-ci va être décrémenté au fil des lignes parcourues.
			ligneCourante = "" # Reset de la ligne courante. (le nombre d'étoiles et le nombre d'espaces vont changer à chaque ligne)
			
			# GESTION DE L'AUGMENTATION DU NOMBRE D'ETOILES DANS LE PASSAGE D'UNE LIGNE A L'AUTRE POUR DES LIGNES SE TROUVANT DANS UN MEME ETAGE.
			for compteurVersIncrEtoilesParLigne in range(0, incrEtoilesParLigne * 2): # Ajouter 2 * incrEtoilesParLigne étoiles à la ligne suivante.
				etoilesLigneCourante += "*"
			nbEspacesInitial -= incrEtoilesParLigne # Chaque ligne parcourue dans un même étage possède un nombre d'espaces en moins que la précédente égal au nombre d'étoiles que cette ligne gagne de chaque côté du centre de cette ligne.
		hauteurSommet += incrHauteurSommet

		for compteurVersIncrEtoilesParEtage in range(0, incrEtoilesParEtage * 2): # Ajouter 2 * incrEtoilesParEtage étoiles à la ligne suivante, car on passe à un autre étage.
			etoilesLigneCourante += "*" # Ajout d'un certain nombre d'étoiles qui dépend de l'incrément du nombre d'étoiles lors du passage d'un étage à un autre.
		nbEspacesInitial -= incrEtoilesParEtage # La première ligne de l'étage suivant possède un nombre d'espaces en moins qui dépend de l'incrément du nombre d'étoiles lors du passage d'un étage à un autre.
		if compteurVersCompteurNonIncr == compteurNonIncr: #  Faut-il augmenter le nombre d'étoiles que l'on ajoute à la première ligne d'un nouvel étage?
			incrEtoilesParEtage += incrIncrEtoilesParEtage
			compteurVersCompteurNonIncr = 0
		compteurVersCompteurNonIncr += 1



# Définition des variables globales pour les tests. (commencent par g)
gNombreBlocs = 5 # Le nombre de blocs constituant la pyramide.

gHauteurSommet = 3 # La hauteur du sommet.
gIncrHauteurSommet = 1 # L'incrément sur la hauteur des blocs à chaque changement de bloc.

gIncrEtoilesParLigne = 1 # Le nombre d'étoiles que l'on rajoute à la fois à gauche et à droite de la ligne précédente dans le passage d'une ligne à l'autre dans un même bloc.
gIncrEtoilesParEtage = 2 # Le nombre initial d'étoiles que l'on rajoute à la fois à gauche et à droite de la ligne précédente dans le passage d'une ligne à l'autre quand on change de bloc.
gIncrIncrEtoilesParEtage = 1 # L'incrément de incrEtoilesParEtage.

gIncrCompteurNonIncr = 0 # L'incrément de compteurNonIncr. (optionnel et pas demandé pour l'exercice, mais je prévois la future évolution du projet)
gCompteurNonIncr = 2 # Le nombre d'étages sans incrémenter incrEtoilesParEtage.

gHauteurPorte =  gNombreBlocs # La hauteur de la porte.
gLargeurPorte = gHauteurPorte + 1 if gHauteurPorte % 2 == 0 else gHauteurPorte # La largeur de la porte.

gPositionHorizontalePoignee =  gLargeurPorte - 1 if gLargeurPorte > 3 else gLargeurPorte # La position horizontale de la poignée sur la porte.
gPositionVerticalePoignee = (gHauteurPorte // 2) + 1 # La position verticale de la poignée sur la porte.



# Calcul de l'espace entre le bord gauche de la console et l'étoile du sommet de la pyramide.
# Une fois que l'on a cet espace, on va pouvoir le décrémenter afin d'obtenir l'espace à mettre dans chaque ligne.
gNbEspacesInitial = CalculerNbEspacesInitial(gNombreBlocs, gHauteurSommet, gIncrHauteurSommet, gIncrEtoilesParLigne, gIncrEtoilesParEtage,  gIncrIncrEtoilesParEtage,gCompteurNonIncr, gIncrCompteurNonIncr)
ConstruireSastantua(gNombreBlocs, gHauteurSommet, gIncrHauteurSommet, gIncrEtoilesParLigne, gIncrEtoilesParEtage, gIncrIncrEtoilesParEtage, gIncrCompteurNonIncr, gCompteurNonIncr, gHauteurPorte, gLargeurPorte, gPositionHorizontalePoignee, gPositionVerticalePoignee, gNbEspacesInitial)
