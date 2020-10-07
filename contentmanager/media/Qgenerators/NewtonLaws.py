import random
import math
from . import QGenerator


class NewtonLawGenerator(QGenerator.QBase):
    def __init__(self):
        super().__init__()

    def NewtonLaw(self):
        question = ['', [], 0]
        choice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        index = random.choice(choice)
        if index == 1:
            q = 'Swinging becomes possible because newtow Law'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Third'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'second'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'First'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 2:
            q = 'In the expression Fxt the Force f is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'average force'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'instantaneous force'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'total force'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'all of them'
            question = [q, option, correctIndex]
        elif index == 3:
            force = random.randint(4, 10)
            mass = random.randint(4, 15)
            time = random.randint(4, 8)
            q = 'A force of '+str(force)+' dynes on a body of mass '+str(
                mass)+' g which at rest, for an interval of '+str(time)+'s then impulse is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = ''+str(force*time)+' 10^-5'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = ''+str(force)+'10^-5'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = ''+str(force*mass/time)+'10^-5'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = ''+str(mass)+'10^-5'
            question = [q, option, correctIndex]
        elif index == 4:
            q = 'For a fixed force, larger is the mass of the body its acceleration will be'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'decrease'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'increase'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'constant'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'independent'
            question = [q, option, correctIndex]
        elif index == 5:
            q = 'Newton first law is also called'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Law of inertial'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Law of momentum'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Law of torques'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Law of force'
            question = [q, option, correctIndex]
        elif index == 6:
            mass = random.randint(5, 15)
            a = random.randint(10, 25)
            q = 'A mass of ' + \
                str(mass)+'kg and its acceleration is ' + \
                str(a)+'then force will be'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = mass*a
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(mass*a/2)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = mass
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = a
            question = [q, option, correctIndex]
        elif index == 7:
            m = random.randint(1, 5)
            a = random.randint(2, 10)
            q = 'A body of mass ' + \
                str(m)+'kg is falling when an acceleration is ' + \
                str(a)+'m/s^2 . Its apprent weight will be'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Zero'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = m
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = m*a
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = a
            question = [q, option, correctIndex]
        elif index == 8:
            q = 'A dirty carpet is to be cleaned by heating. This is according which law of motion'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'First'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Second'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Third'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'None'
            question = [q, option, correctIndex]
        elif index == 9:
            q = 'Newtons law are adequate at'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Low compared with the speed of light'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Equal to speed of light'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Greater then speed of light'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'all of them'
            question = [q, option, correctIndex]
        elif index == 10:
            time = random.randint(4, 8)
            q = 'Distance covered by freely falling body in'+str(time)+' is '
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = time*9.8
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = time*5
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = time
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Zero'
            question = [q, option, correctIndex]
        return question

    def generateQuestions(self):
        return (self.NewtonLaw())


def getInstance():
    return NewtonLawGenerator()
