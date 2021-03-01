
class Pawn:

#Ajoute les détails pour créer le tableau dans la class Pawn.

    def __init__(self,x,y):                    #Pas de paramètre pour la matrice car elle aura une taille fixe.
        self.matrice = [[1,1,1,1,1,1,1],       # x --> sous-liste, y ---> élément de la sous-liste.
                        [1,0,0,0,0,0,1],       #matrice de taille 6x7.
                        [1,0,0,0,0,0,1],
                        [1,0,0,0,0,0,1],  
                        [1,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1]]

        if type(x) != int or type(y) != int:
            print("Le pion ne peut avoir ces données, le pion a pris (2,3) par défaut")     
            self.x = 3
            self.y = 2
        elif self.matrice[x][y] == 1 :
            self.x = 3
            self.y = 2
            print("Le pion ne peut pas représenter le mur, le pion a pris (2,3) par défaut")
        elif x >= 5 or y >= 6:
            self.x = 3
            self.y = 2
            print("Le pion ne peut pas être en dehors du plateau, le pion a pris (2,3) par défaut")
        else:
            self.x = x
            self.y = y
        self.matrice[self.x][self.y] = 2
        print(self)
 
    def __str__(self):
        plateau = ''
        for ligne in self.matrice: 
            plateau += str(ligne).replace('[','').replace(',','').replace(']','') #Permet de représenter le plateau dans la console.
            plateau += "\n"
        return plateau
        
   
    def MoveRight(self) :  
        coordonateX = self.x       #coordonné dans la classe     #gérer le cas où le piont n'est pas initialisé.
        coordonateY = self.y      #coordonné dans la classe  
        if self.matrice[coordonateX][coordonateY+1] == 1:         #1 --> mur , 0 ---> case vide, ne peut pas bouger lorsque c'est 1.
            verification = False
        else:
            verification = True
        if verification == True :
            self.matrice[coordonateX][coordonateY] = 0 
            self.matrice[coordonateX][coordonateY+1] = 2
            self.y = coordonateY + 1        #Change coordonées du pion par les nouvelles obtenues après déplacement.
            print(self)     #Affiche le plateau après avoir bougé le pion. 
        else :
            message = "Impossible d'aller à droite!"
            print(self)
            return message

    def MoveLeft(self) :
        coordonateX = self.x     
        coordonateY = self.y
        if self.matrice[coordonateX][coordonateY-1] == 1:         #1 --> mur , 0 ---> case vide, ne peut pas bouger lorsque c'est 1.
            verification = False
        else:
            verification = True
        if verification == True :
            self.matrice[coordonateX][coordonateY] = 0 
            self.matrice[coordonateX][coordonateY-1] = 2
            self.y = coordonateY - 1
            print(self) #Affiche le plateau après avoir bougé le pion.
        else :
            message = "Impossible d'aller à gauche!"
            print(self)
            return message

    def MoveUp(self) :
        coordonateX = self.x    
        coordonateY = self.y
        if self.matrice[coordonateX-1][coordonateY] == 1:         #1 --> mur , 0 ---> case vide, ne peut pas bouger lorsque c'est 1.
            verification = False
        else:
            verification = True
        if verification == True :
            self.matrice[coordonateX][coordonateY] = 0 
            self.matrice[coordonateX-1][coordonateY] = 2
            self.x = coordonateX - 1
            print(self)     #Affiche le plateau après avoir bougé le pion. 
        else :
            message = "Impossible d'aller en haut!"
            print(self)
            return message

    def MoveDown(self) :                                
        coordonateX = self.x
        coordonateY = self.y
        if self.matrice[coordonateX+1][coordonateY] == 1:         #1 --> mur , 0 ---> case vide, ne peut pas bouger lorsque c'est 1.
            verification = False
        else:
            verification = True
        if verification == True :
            self.matrice[coordonateX][coordonateY] = 0 
            self.matrice[coordonateX+1][coordonateY] = 2
            self.x = coordonateX + 1 
            print(self) #Affiche le plateau après avoir bougé le pion.
        else :
            message = "Impossible d'aller en bas!"
            print(self)
            return message