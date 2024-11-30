class Warrior:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage
        target.health = max(target.health, 0)

class Gnom:
    def __init__(self):
        self.name = "Gnom"
        self.health = 50
        self.damage = 8

    def attack(self, target):
        target.health -= self.damage
        target.health = max(target.health, 0)

class Mag:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage
    
    def attack(self, target):
        target.health -= self.damage
        target.health = max(target.health, 0)

class Archer:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage
    
    def attack(self, target):
        target.health -= self.damage
        target.health = max(target.health, 0)