   
#Idee pour representer le plateau. 

class Pawn:

#Ajoute les détails pour créer le tableau dans la class Pawn.

    def __init__(self,x,y):                    #Pas de paramètre pour la matrice car elle aura une taille fixe.
       self.matrice = [[1,1,1,1,1,1,1],        # x --> sous-liste, y ---> élément de la sous-liste.
                       [1,0,0,0,0,0,1],    #matrice de taille 6x7.
                       [1,0,0,0,0,0,1],
                       [1,0,0,0,0,0,1],  
                       [1,0,0,0,0,0,1],
                       [1,1,1,1,1,1,1]]
        #Pas oublier d'initialiser le point dans la matrice.
        
    def __str__(self):
        plateau = ''
        for ligne in self.matrice: 
            plateau += str(ligne).replace('[','').replace(',','').replace(']','') #Permet de représenter le tableau dans la console.
            plateau += "\n"
        return plateau
        
    def check(self):
    """ Verifie si le pion peut bouger à la position (x,y) (ligne,colonne), retourne un booleen."""
        if self.matrice[x][y] == 1:         #1 --> mur , 0 ---> case vide, ne peut pas bouger lorsque c'est 1.
            return False
        else:
            return True
   
   def MoveRight() :  
    coordonateX = #coordonné dans la classe 
    coordonateY = #coordonné dans la classe  
    verification = check(coordonateX,coordonateY+1) 
    if verification == True :
        self.matrice[coordonateX][coordonateY] = 0 
        self.matrice[coordonateX][coordonateY+1] = 2
        self.y = coordonateY + 1    #Je change les coordonées du pion par les nouvelles obtenues après l'avoir bougé. -Marine
        return #coordonné du nouveau point du pion  
    else :
        message = "Impossible d'aller à droite!"
        return message

def MoveLeft() :
    coordonateX = #coordonné dans la classe     
    coordonateY = #coordonné dans la classe
    verification = check(coordonateX,coordonateY-1)
    if verification == True :
        self.matrice[coordonateX][coordonateY] = 0 
        self.matrice[coordonateX][coordonateY-1] = 2
        self.y = coordonateY - 1
        return #coordonné du nouveau point du pion dans la classe
    else :
        message = "Impossible d'aller à gauche!"
        return message

def MoveUp() :
    coordonateX = #coordonné dans la classe     
    coordonateY = #coordonné dans la classe
    verification = check(coordonateX-1,coordonateY)
    if verification == True :
        self.matrice[coordonateX][coordonateY] = 0 
        self.matrice[coordonateX-1][coordonateY] = 2
        self.x = coordonateX - 1
        return #coordonné du nouveau point du pion
    else :
        message = "Impossible d'aller en haut!"
        return message

def MoveDown() :                                
    coordonateX = #coordonné dans la classe
    coordonateY = #coordonné dans la classe
    verification = check(coordonateX+1,coordonateY)
    if verification == True :
        self.matrice[coordonateX][coordonateY] = 0 
        self.matrice[coordonateX+1][coordonateY] = 2
        self.x = coordonateX + 1 
        return #coordonné du nouveau point du pion
    else :
        message = "Impossible d'aller en bas!"
        return message
      
r = Pawn()
print(r)                
        

