# -*-coding:utf-8-*
import os
import pickle
from random import choice
from donnees import*

def recup_scores():
    if os.path.exists(nom_fichier_score):
	    fichier_scores=open("nom_fichier_score", "rb")
	    mon_deplickler=pickle.Unpickler(fichier_scores)
	    scores=mon_deplickler.load()
	    fichier_scores.close()
    else:
        scores={}
    return scores
def enregistrer_scores(scores):
    fichier_scores=open("nom_fichier_score", "wb")
    mon_pickler=pickler.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()
def recuperer_joueur():
    joueur=raw_input("taper nom du joueur: ")
    joueur=joueur.capitalize()
    if not joueur.isalnum() or len(joueur)<4:
        print "ce nom n'est pas valide"
        return recuperer_joueur()
    else:
        return joueur
def recup_lettre():
    lettre=raw_input("taper votre lettre: ")
    if len(lettre)>1 or not lettre.isalpha():
        print "saisie invalide"
        return recup_lettre()
    else:
        return lettre
def choisir_mot():
    return choice(liste_mots)		
def recup_mot_masque(mot_complet, lettres_trouvees):
    mot_masque=""
    for l in mot_complet:
        if l in lettres_trouvees:
            mot_masque+=l
            
        else:
            mot_masque+="*"

        return mot_masque
	
