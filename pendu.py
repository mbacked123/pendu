# -*-coding:utf-8-*
import os
from donnees import*
from fonctions import*
scores=recup_scores()
joueur = recuperer_joueur()
if joueur not in scores.keys():
    scores[joueur]=0
continuer_partie='o'
while continuer_partie!='n':
    print ("jour {0}:{1} points".format(joueur, scores[joueur]))
    mot_a_trouver=choisir_mot()
    lettres_trouvees=[]
    mot_trouve=recup_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chance=nb_coup
    while mot_a_trouver!=mot_trouve and nb_chance>0:
        print ("mot a trouver {0} (encore {1} chances)" .format(mot_trouve, nb_chance))
        lettre=recup_lettre()
        if lettre in lettres_trouvees:
            print "vous avez deja choisi cette lettre"
        elif lettre in mot_a_trouver:
            lettres_trouvees.append(lettre)
            print "Bien joue"
        else:
            print"non cette lettre ne se trouve pas dans le mot"
        mot_trouve=recup_mot_masque(mot_a_trouver, lettres_trouvees)
        print mot_trouve
        nb_chance-=1
    if mot_a_trouver==mot_trouve:
        print"Felicitation vous avez trouve le mot {0}".format(mot_a_trouver)
    else:
        print"PENDU.vous avez perdu"
    scores[joueur]+=nb_chance
    continuer_partie=raw_input("souhaiter-vous continuer O/N : ")
    continuer_partie=continuer_partie.lower()
enregistrer_scores(scores)
print "Vous finissez la partie avec {0} points.".format(scores[joueur])	
		
os.system("pause")
