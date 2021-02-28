class Point:
    """represente un point"""
    def __init__(self, x, y): 
       
        try:
            self.x = int(x)
            self.y = int(y)
            
        except ValueError:
            print("Le pion ne peut être initialiser avec ces données")
        if self.matrice [x][y] == 1
            print("Le pion ne peut pas représenter le mur!")
        if self.matrice[x][y] >= 1
            print("Le pion ne peut pas être représenter avec ces données")
        else:
            self.x = x
            self.y = y

    def __str__(self):
        return '%g,%g' % (self.x, self.y)
