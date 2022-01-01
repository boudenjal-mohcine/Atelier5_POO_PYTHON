#classe rectangle
class Rectangle:
      
  #attribut nom
  nom='rectangle'
  
  #constructeur
  def __init__(self,l,L):
    self.longueur=L
    self.largeur=l
 
  #methode d'affichage
  def affichage(self):
    print('un(e)',self.nom,'de longeur:',self.longueur,'m et du largeur:',self.largeur,'m')
    for a in range(0,self.largeur,1):
       for b in range(0,self.longueur,1):
          print("*",end=" ")
       print(end="\n")
    
      
  
  #methode de calcule de surface
  def surface(self):
    print("la surface du", self.nom, "est",self.longueur*self.largeur,"metres au carre")

#classe carre
class Carre(Rectangle):
      
  #attribut nom
  nom="carre"
  
  
#fonction principale

#declaration des deux objets
rect=Rectangle(8,14)
carr=Carre(10,10)

#affichage des informations du rectangle et calcule de surface
print("================================================================================")
rect.affichage()
rect.surface()
print("================================================================================")
#affichage des informations du rectangle et calcule de surface
carr.affichage()
carr.surface()
print("================================================================================")