class Point:
    """represente un point"""
    def __init__(self, x=2, y=3): # variables par defaut
       
        try:
           if self.x is not int(x) or self.y is not int(y):
               raise ValueError ("Les coordonnées du pion ne sont pas acceptables")
        except ValueError:
            print("Le pion ne peut être initialiser avec ces données")
        if self.matrice [x][y] == 1:
            print("Le pion ne peut pas représenter le mur")
        if self.x >= 6 or self.y >=7:
            print("Le pion ne peut pas être en dehors du plateau")
        if self.x < 0 or self.y < 0:
            print("Le pion ne peut être initialiser avec ces données")

        else:
            self.x = x
            self.y = y

    def __str__(self):
        return '%g,%g' % (self.x, self.y)
