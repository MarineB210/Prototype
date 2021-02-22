def canMove(self):

    """ Verifie si le pion peut bouger à la ligne y et colonne x, retourne un booleen."""

    if map[y][x] == 1: #1 --> mur , 0 ---> case vide
        return False
    else:
        return True 
        
        
#Idee pour representer la matrice. 

class Plateau:

#créer un plateau et méthodes permettant de l'actualiser.
    def __init__(self): #Pour le moment je ne rajoute pas de paramètre car le plateau aura une taille fixe.
       self.matrice = [[1,1,1,1,1,1,1],
                       [1,0,0,0,0,0,1],    #matrice de taille 7x7
                       [1,0,0,0,0,0,1],
                       [1,0,0,0,0,0,1],    #Créer une méthode qui va créer un pion dans la matrice ? Peut etre rajouter x et y 
                       [1,0,0,0,0,0,1],
                       [1,1,1,1,1,1,1]]
        
    def __str__(self):
        plateau = str(self.matrice)
        plateau = plateau.replace('[','').replace(',','').replace(']','')  #!!! Ajouter un retour à la ligne après chaque liste !!!
        return plateau
        
                
r = Plateau()
print(r)                
        

