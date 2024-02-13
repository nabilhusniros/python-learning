import random
class Person:
    def __init__(self, firstname, lastname, health, status):
        '''initialize attribiute to be used in/available for all
        class method in this class, and for class objects created
        by this class'''

        self.firsname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        'All people introduce themselves'
        print('Hello my name is {} {} '.format(self.firsname, self.lastname))

    def emote(self):
        emotion = random.randrange(1, 3)
        if emotion == 1:
            print('{} is happy today'.format(self.firsname))
        elif emotion == 2:
            print('{} is sad right now'.format(self.firsname))

    def status_change(self):
        if self.health == 100:
            print('{} is healthy!'.format(self.firsname))
        elif self.health >= 76:
            print('{} is a little jade today'.format(self.firsname))
        elif self.health <= 51:
            print('{} feels unweel'.format(self.firsname))
        elif self.health <= 40:
            print('{} goes to the doctor'.format(self.firsname))
        else:
            print('{} is unconscious'.format(self.firsname))

Maria = Person('Maria', 'Santiago', 95, status=True)
Rey = Person('Rey', 'John', 88, status=False)
Lee = Person('Lee', 'Tang', 72, status=True)

print('{} is my friend {}'.format(Maria.firsname, Maria.status))
print('{} is my friend {}'.format(Rey.firsname, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()

class Enemy(Person):
    def __init__(self, weapon, firsname, lastname, health, status):
        super().__init__(firsname, lastname, health, status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
            print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print('{}, you are tired and weak'.format(other.firsname))

    def steal(self, other):
        print('ha ha ha, {}, I have your stuff!'.format(other.firsname))
        if other.status == True:
            other.status == False

Alex = Enemy('rock', 'Alex', 'Wayne', 75, status=False)
Alex.hurt(Maria)
Alex.insult(Lee)
Alex.steal(Rey)
