

class Player:

    participaton = 0

    win = 0
    draw = 0
    loose = 0


    def __init__(self, name,id ):
        self.id = id
        self.name = name
        self.participaton += 1
        
    def __str__(self):
        return f"{self.id} : {self.name} [{self.win}-{self.loose}-{self.draw}] {self.countPoint()} points"
    def name(self):
        return self.name
    
    def __eq__(self, other):
        return self.id == other.id
    
    def countPoint(self):
        bonus= 0
        if self.participaton > 1:
            bonus = self.participaton
        return (self.win*3 + self.draw*2 + self.loose + bonus)

    @staticmethod
    def triPts(e):
        return e.countPoint()