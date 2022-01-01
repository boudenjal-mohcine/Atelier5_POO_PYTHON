#classe point
class Point:
   
    #constructeur
    def __init__(self,x1=0.0,y1=0.0):
          self.x=x1
          self.y=y1

      
#classe seguement
class Seguement:
      
      #instances du classe Point
      orig=Point()
      extrem=Point()
      
      #constructeur
      def __init__(self,orgx,orgy,extrx,extry):
          self.orig.x=orgx
          self.orig.y=orgy
          self.extrem.x=extrx
          self.extrem.y=extry
      
      #affichage
      def display(self):
       print("seguement d'origine (",self.orig.x,",",self.orig.y,") et d'extremité (",self.extrem.x,",",self.extrem.y,")")


#fonction main
      
p=Seguement(1,2,3,4)
p.display()
