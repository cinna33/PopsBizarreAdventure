# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:54:44 2019

@author: Pumkin
"""
import math as m
from random import randrange
import os
#Mise à 0 de toutes les variables
mise=0
case=0
argent=0
c=1 #Déf du choix (cf l.82)
#Définition de la fonction qui permet de vérfier s'il triche ou non
def triche(j):
    if j==mise: #Définition de la variable i
        i=1
    if j==case:
        i=2
    while j == str(j): #Vérification de la variable pour savoir si c'est une lettre
        try:
            j=int(j)
        except: #Forçage du programme pour mettre un nombre
            print("Ce que vous venez de dire n'a aucun sens, recommencez")
            if i==1: #Cas de la mise
                j=input("Votre mise: ")
            if i==2: #Cas de la case
                j=input("Votre case: ")
    j=int(j) #Ceci est pour si le joueur est fairplay
    if i==1: #Case de la mise donc juste vérification si le nombre est négatif
        while j<0:
            print("Depuis quand les $ sont négatifs ?")
            j = input("Arrête de faire le con: ")
            while j == str(j): #Encore vérification de la variable si lettre 
                try:
                    j = int(j)
                except:
                    print("ARRÊTE")
                    j = input("M.I.S.E.: ")
    if i==2: #Cas de la case donc on vérifie si la case est négative ou supérieur à 49
        while j<0 or j>49:
            print("Cette case n'existe pas")
            j = input("Arrête de faire le con: ")
            while j == str(j): #Encore vérification de la variable si lettre 
                try:
                    j = int(j)
                except:
                    print("ARRÊTE")
                    j = input("C.A.S.E.: ")
    j = int(j)                
    return j    
#Présentation du ZCasino aux joueurs
print("Bienvenue au ZCasino, une version simplifiée donc rien de compliqué")
print("Misez une somme d'argent (en $) sur une des 50 cases de la roulette allant de 0 à 49")
print("Si on tombe sur le numéro que vous avez misé, on vous rend 3 fois la somme que vous avez misé")
print("Sinon si elle est de la même couleur que la case que vous avez misé à la base (les cases pairs sont noires et les impairs rouges), Nous vous rendons la moitié de votre mise")
print("Sinon nous gardons tout ... à vous de jouer")
while c == 1: #Conditions pour recommencer le jeu
    mise = input ("La somme que vous misez (les nombres décimaux seront arrondis) : ")
    mise = triche(mise)
    argent-=mise
    print("Vous avez misé",mise,"$ et vous avez à présent", argent, "$")
    #Maintenant faut que le joueur choisisse une case et recommence le prcessus d'avant
    case = input("Maintenant choisissez une case (les nombres décimaux seront aussi arrondis): ")
    case = triche(case)
    print("Vous avez misé sur la case", case)
    print("On lance la roulette")
    case2=randrange(50) #Lancement aléatoire de la case
    print("Vous êtes tombé sur la case", case2)
    if case2==case: #Le joueur est tombé sur la case qu'il voulait
        mise=mise*3
        argent+=mise
        print("Bravo vous avez gagné", mise,"$ et vous avez dès à présent", argent, "$")
    elif case2!=case and case%2==case2%2: #Pas tombé sur la case qu'il voulait mais même couleur
        mise=mise/2
        mise=m.ceil(mise)    
        argent+=mise
        print("Dommage, vous n'êtes pas tombé sur la case que vous avez choisi... Néanmoins, vous regagnez la moitié de ce que vous avez misé parce que la case est la même couleur que celle que vous avez misé donc vous gagnez", mise, "$ et maintenant avez", argent, "$")
    else: #Pas du tombé sur ce qu'il voulait
        print("Ah mince, vous avez totalement perdu ... Nous sommes désolé mais le ZCasino est gagnant cette fois. Vous avez maintenant", argent, "$")
    print("Voulez-vous rejouer ?") #Choix donné pour rejouer
    c = input("Oui/Non (y/n): ") #Joueur choisit entre oui et non
    while not c.lower() in ("oui","non","yes","no","y","n"):
        print ("hein")
        c = input("Parle français stp oui ou non : ")
    if c.lower() in ("oui","yes","y"): #Oui donc la partie recommence
        c=1
        print("D'accord recommençons une partie")
    elif c.lower() in ("non", "no", "n"): #Non donc la partie se finit
        c=2
        print("En ce cas, vous repartez avec", argent, "$. à bientot. Ah et souvenez vous : le ZCasino est toujours gagnant :)")        
        os.system("pause")