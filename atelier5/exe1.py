#classe vecteur
class Vecteur2D:
  def __init__(self,x1=0,y1=0):
     self.x=x1
     self.y=y1


#main function

#vecteur "a" sans parametres
a = Vecteur2D()

#vecteur "b" avec deux parametres
b = Vecteur2D(2,4)

#affichage des deux vecteurs
for vect in {a,b}:
  print('(',vect.x,',',vect.y,')')
