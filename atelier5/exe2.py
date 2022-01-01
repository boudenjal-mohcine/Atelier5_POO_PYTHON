#classe vecteur
class Vecteur2D:
  def __init__(self,x1=0,y1=0):
     self.x=x1
     self.y=y1

#methode affichage
  def display(self):
    print('(',self.x,',',self.y,')')

#methode d'addition
  def add(self,vect):
    result=Vecteur2D()
    result.x=self.x+vect.x
    result.y=self.y+vect.y
    result.display();

   
#main function

#vecteur a(2,4)
a = Vecteur2D(2,4)

#vecteur b(3,6)
b = Vecteur2D(3,6)

#affichage des vecteurs a et b
print("a =",end=" ")
a.display()

print("b =",end=" ")
b.display()

#addition a+b
print("a + b =",end=" ")
a.add(b)
