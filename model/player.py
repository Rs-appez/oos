class Player:

    participaton = 0

    win = 0
    draw = 0
    loose =  0


    def __init__(self, name,id ):
        self.id = id
        self.name = name
        self.participaton += 1
        
    def __str__(self):
        return f"{self.name} avec {self.countPoint()} points"

    def __eq__(self, other):
        return self.id == other.id
    
    def countPoint(self):
        bonus= 0
        
        if(self.participaton >1):
            if(self.participaton >2):
                bonus = 3
            else:
                bonus=2
        
        
        return self.win*3 + self.draw*2 + self.loose + bonus

    @staticmethod
    def triPts(e):
        return e.countPoint()