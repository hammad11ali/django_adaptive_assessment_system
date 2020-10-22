import random
import math
from . import QGenerator


class AccelerationGenerator(QGenerator.QBase):
    def __init__(self):
        super().__init__()

    def generateQuestions(self):
        question = ['', [], 0]
        choice = [1, 2, 3, 4, 5, 6, 7]
        index = random.choice(choice)
        if index == 1:
            q = 'A monkey sits on the pan of spring scale kept in an elevator. The reading of the spring will be maximum at'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Elevator accelerates upward'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Elevator accelerates downward'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Elevator is stationary'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Elevator cable breaks and freely fall on earth'
            question = [q, option, correctIndex]
        elif index == 2:
            q = 'Acceleration produced ina body by force varies'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'directly as the applied force'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'inversly as the applied force'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'remain constant'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 3:
            q = 'Decreasing velocity per unit time called'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'decelaration'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'acceleration'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'uneliform acceleration'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 4:
            velocity1 = random.randint(15, 25)
            velocity2 = random.randint(5, 10)
            q = 'A train is moving with a velocity of '+str(velocity1)+'m/s and a car is moving behind it by a velocity of '+str(
                velocity2)+'m/s in same direction. The relative velocity will be'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = velocity1-velocity2
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = velocity2+velocity1
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = velocity1
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = velocity2
            question = [q, option, correctIndex]
        elif index == 5:
            velocity1 = random.randint(15, 25)
            velocity2 = random.randint(5, 10)
            q = 'A train is moving with a velocity of '+str(velocity1)+'m/s and a car is moving behind it by a velocity of '+str(
                velocity2)+'m/s in opposite direction. The relative velocity will be'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = velocity1+velocity2
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = velocity2-velocity1
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = velocity1
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = velocity2
            question = [q, option, correctIndex]
        elif index == 6:
            q = 'The direction of acceleration is same as'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'velocity'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'speed'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'force'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'all of them'
            question = [q, option, correctIndex]
        elif index == 7:
            q = 'Acceleration is produced in a body by a varies of force'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'directly as a force'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'inversly as a force'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'independent'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of them'
            question = [q, option, correctIndex]
        return question
        


def getInstance():
    return AccelerationGenerator()
