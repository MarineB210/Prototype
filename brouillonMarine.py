   
#Idee pour representer le plateau. 

class Pawn:

#Ajoute les détails pour créer le tableau dans la class Pawn.

    def __init__(self):                    #Pas de paramètre pour la matrice car elle aura une taille fixe.
       self.matrice = [[1,1,1,1,1,1,1],
                       [1,0,0,0,0,0,1],    #matrice de taille 7x7.
                       [1,0,0,0,0,0,1],
                       [1,0,0,0,0,0,1],  
                       [1,0,0,0,0,0,1],
                       [1,1,1,1,1,1,1]]
        
    def __str__(self):
        plateau = ''
        for ligne in self.matrice: 
            plateau += str(ligne).replace('[','').replace(',','').replace(']','') #Permet de représenter le tableau dans la console.
            plateau += "\n"
        return plateau
        
    def check(self):

    """ Verifie si le pion peut bouger à la ligne y et colonne x, retourne un booleen."""

    if self.matrice[y][x] == 1:         #1 --> mur , 0 ---> case vide, ne peut pas bouger lorsque c'est 1.
        return False
    else:
        return True
   
   def MoveRight() :
    coordonateX = #coordonné dans la classe
    coordonateY = #coordonné dans la classe
    verification = check(coordonateX,coordonateY+1)
    if verification == true :
        self.matrice[coordonateX][coordonateY] = 0 
        self.matrice[coordonateX][coordonateY+1] = 2
        return #coordonné du nouveau point du pion
    else :
        message = "Impossible d'aller à droite!"
        return message

def MoveLeft() :
    coordonateX = #coordonné dans la classe
    coordonateY = #coordonné dans la classe
    verification = check(coordonateX,coordonateY-1)
    if verification == true :
        self.matrice[coordonateX][coordonateY] = 0 
        self.matrice[coordonateX][coordonateY-1] = 2
        return #coordonné du nouveau point du pion dans la classe
    else :
        message = "Impossible d'aller à gauche!"
        return message

def MoveUp() :
    coordonateX = #coordonné dans la classe
    coordonateY = #coordonné dans la classe
    verification = check(coordonateX-1,coordonateY)
    if verification == true :
        self.matrice[coordonateX][coordonateY] = 0 
        self.matrice[coordonateX-1][coordonateY] = 2
        return #coordonné du nouveau point du pion
    else :
        message = "Impossible d'aller en haut!"
        return message

def MoveDown() :
    coordonateX = #coordonné dans la classe
    coordonateY = #coordonné dans la classe
    verification = check(coordonateX+1,coordonateY)
    if verification == true :
        self.matrice[coordonateX][coordonateY] = 0 
        self.matrice[coordonateX+1][coordonateY] = 2
        return #coordonné du nouveau point du pion
    else :
        message = "Impossible d'aller en bas!"
        return message

    """def moveRight(self):                    #même code pour le moveLeft.
        """..."""
        if pass:
            """..."""
            self.matrice[self.y][self.x] = 0
            self.x = x
            self.matrice[self.y][self.x] = 2
            """..."""

    def moveUp(self):                       #même code pour le moveDown.
        """..."""
        if pass:
           """..."""
            self.matrice[self.y][self.x] = 0
            self.y = y
            self.matrice[self.y][self.x] = 2
            """... """                           """
        
    def addPawn(self):
        """ Ajoute le pion dans la matrice"""
        
        
    
    
                
r = Pawn()
print(r)                
        

