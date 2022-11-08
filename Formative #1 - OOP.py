# OOP Formative #1----
# Cole Patton
# Nov 8, 2022
#-----------------------------


class NPC:
    coolness = 50
    
    def __init__(self, health, name, age):
        self.health = health
        self.name = name
        self.age = age
    
    def walk(self):
        print(f"{self.name} is walking")
    
    def sit(self):
        print(f"{self.name} is sitting")
    
    def show(self):
        print(f"{self.name} has {self.health} hitpoints and is {self.age} years old")


class Friend(NPC):
    def __init__(self, health, name, age, helping):
        super().__init__(health, name, age)
        self.helping = helping
    
    def help(self):
        print(f"{self.name}, {self.helping}, is here to help!")
        
    @staticmethod
    def think():
        print("Your friend thinks")
        
class Enemy(NPC):
    
    def __init__(self, health, name, age, attacking):
        super().__init__(health, name, age)
        self.attacking = attacking
    
    def attack(self):
        print(f"{self.name}, {self.attacking}, is not here to help! He's an enemy!")
        
    @classmethod
    def lose_cool(cls):
        cls.coolness -= 10
        print(f"The enemy now has only {cls.coolness} coolness!")
        
        
        

f = Friend(100, "Alfred", 25, "yes")

f.walk()
f.sit()
f.show()
f.help()
f.think()
print('')
e = Enemy(75, "By-Tor", 45, "no")
e.walk()
e.sit()
e.show()
e.attack()
print(f"He currently has {NPC.coolness} coolness")
e.lose_cool()

        
    