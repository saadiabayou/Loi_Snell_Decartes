#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:04:20 2021

@author: Saadia Bayou
"""




""" Nous condsidérons deux milieux différents,
    nous supposons que la lumière traverse ses deux milieux avec un phénomène de diffraction
    Ce programme permet d'afficher les milieux étudiés et leurs indice de rafractions respectifes 
    selon certaine conditions de tempéarture et de pression """



print("\nNous considérons 5 milieux et leurs indices de refraction respectifs :\n" )

# Données  

# Liste milieux
milieu=["vide","atmosphère","air","verre","eau"]

#  Indices de refraction  - conditions de T et p

# vide
n_vide=1 
# atmosphère
n_atm=1.0013
# air
n_air=1.000293
#verre
n_verre=1.52 
# eau
n_eau=1.333

# Liste indices
n_milieu=[n_vide,n_atm,n_air,n_verre,n_eau]


def id_milieu(l):
    """ Cette fonction affiche la liste des milieux """
    print("\n" "La listes des ",len(l)," milieux considérés est :\n" )
    for i in range(len(l)) :
         print(i+1,"-",l[i])
    return print ("\nliste milieux =", l)

print(id_milieu(milieu))
    

  
def n_milieu(m):
    """ Cette fonction permet la selection  du milieu et donne l'indice de refraction correspondant"""
    for m in milieu :   

        m=input("Entrer le milieu : ")
    
        if m=="vide":
           return  print("L'indice du vide est:", n_vide)
        elif m=="atmosphère":
            return print("L'indice de l'atmosphère est:", n_atm)
        elif m=="verre":
            return print("indice du verre est:", n_verre)
        elif m=="air":
            return print("indice de l'air est:", n_air)
        elif m=="eau":
            return print("L'indice de l'eau est:", n_eau) 
        else:
            return "Indice de milieu inconnu"

print(n_milieu(m))
    


