class Spaceship:
    """Base spaceship class"""

    def __init__(self, posx, posy, health, number_of_bullets, weapon_type, speed):
        self.posx = posx
        self.posy = posy
        self.health = health
        self.number_of_bullets = number_of_bullets
        self.weapon_type = weapon_type
        self.speed = speed
    
    def move_left(self):
        self.posx -= self.speed
    
    def move_right(self):
        self.posx += self.speed
    
    def move_up(self):
        self.posy += self.speed

    def move_down(self):
        self.posy -= self.speed
    
    def shoot(self):
        pass

    def die(self):
        pass

class Player(Spaceship)
    pass