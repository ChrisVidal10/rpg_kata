class Character:

    __max_health = 1000

    def __init__(self):
        self.health = 100
        self.level = 1
        self.alive = True

    def take_damage(self, damage_amount):
        self.health -= min(damage_amount, self.health)
        self.recalculate_live()

    def recalculate_live(self):
        if self.health <= 0:
            self.alive = False

    def take_health(self, health_amount):
        if self.alive:
            if self.health + health_amount <= self.__max_health:
                self.health += health_amount
            else:
                self.health = self.__max_health