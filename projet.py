class Point:
    """represente un point"""
    def __init__(self, x, y): #
        self.x = x
        self.y = y

    def __str__(self):
        return '%g,%g' % (self.x, self.y)# pas certaine a refaire
