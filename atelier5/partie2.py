#classe etudiant
class Etudiant:
   
    #constructeur
    def __init__(self,nom,prenom,age,cne,moyenne):
          self.nom=nom
          self.prenom=prenom
          self.age=age
          self.cne=cne
          self.moyenne=moyenne
          
          
          

#Fonction de tri selon l'age et la moyenne (methode tri a bule exporter depuis exercice 6 du 1ere atelier)

def TRIABULLE_AGE(liste):  # INVERSER CHAQUE 2 ELEMENTS SUCCESSIVE
  permut = True
  while (permut==True):
    permut = False    # ON VA QUITTER LA FONCTION SI ON A PAS ENCORE DE PERMITATION
    for j in range(0,len(liste)-1):
      if (liste[j].age < liste[j+1].age) :   # LE TRI DANS CE CAS FAIT D'UNE MANIERE CROISSANTE
       tmp = liste[j+1]
       liste[j+1] = liste[j]       # tmp EST UN VARIABLE DANS LEQUEL ON VA CHANGER LE CONTENUE DE CHAQUE COUPLE SUCCESSIVE
       liste[j] = tmp
       permut = True
       
       
       
def TRIABULLE_MOY(liste):  # INVERSER CHAQUE 2 ELEMENTS SUCCESSIVE
  permut = True
  while (permut==True):
    permut = False    # ON VA QUITTER LA FONCTION SI ON A PAS ENCORE DE PERMITATION
    for j in range(0,len(liste)-1):
      if (liste[j].moyenne > liste[j+1].moyenne) :   # LE TRI DANS CE CAS FAIT D'UNE MANIERE CROISSANTE
       tmp = liste[j+1]
       liste[j+1] = liste[j]       # tmp EST UN VARIABLE DANS LEQUEL ON VA CHANGER LE CONTENUE DE CHAQUE COUPLE SUCCESSIVE
       liste[j] = tmp
       permut = True
       
       
#fonction main

#lise vide
Etu_list=[]

#Remplissage du liste au hasard
Etu_list.append(Etudiant("Said","Nassim",30,"KB121314",12.40))
Etu_list.append(Etudiant("Ouadie","Dada",20,"KB123314",17.80))
Etu_list.append(Etudiant("Siham","Wissal",34,"KB212134",9.40))
Etu_list.append(Etudiant("Omar","Barcelona",33,"KB111344",20.00))
Etu_list.append(Etudiant("Moncef","Issa",50,"KB221144",18.60))
Etu_list.append(Etudiant("Ayoub","Madrid",42,"KB621355",15.44))
Etu_list.append(Etudiant("Ismail","Titouani",19,"KB327344",8.49))
    
#Tri du liste selon l'age(Decroissante)
TRIABULLE_AGE(Etu_list)
print("==============================Tri selon l\'age (Decroissante)===================================")
for etudiant in Etu_list:
    print("Nom : ",etudiant.nom)
    print("Preom : ",etudiant.prenom)
    print("CNE : ",etudiant.cne)
    print("Age: ",etudiant.age,"ans")
    print("Moyenne : ",etudiant.moyenne)
    print("-----------------------------------------------------------------------------------------------")
print("===============================================================================================")

#Ordonner la liste selon la moyenne(Croissante)
TRIABULLE_MOY(Etu_list)
print("==============================Tri selon la moyenne(Croissante)=================================")
for etudiant in Etu_list:
    print("Nom : ",etudiant.nom)
    print("Preom : ",etudiant.prenom)
    print("CNE : ",etudiant.cne)
    print("Age: ",etudiant.age,"ans")
    print("Moyenne : ",etudiant.moyenne)
    print("-----------------------------------------------------------------------------------------------")
print("===============================================================================================")
