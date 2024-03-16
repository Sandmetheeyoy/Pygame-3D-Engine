# Addition of enemies and stuff



class Enemy: # parent template
    def __init__(self, length_stand, length_prep, length_fire, health_):
        self.health = health_
        self.states = [
            {"ID" : "DUDE_STANDING", "LENGTH" : length_stand, "RETURN STATE" : "DUDE_STANDING"},
            {"ID" : "DUDE_PREPGUN",  "LENGTH" : length_prep, "RETURN STATE" : "DUDE_FIRING"},
            {"ID" : "DUDE_FIRING", "LENGTH" : length_fire, "RETURN STATE" : "DUDE_STANDING"}
        ]

class machinegunDUDE(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(70, 1, 60, 90) # inherits
