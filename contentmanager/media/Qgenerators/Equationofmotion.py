import random
import math
from . import QGenerator


class EquationGenerator(QGenerator.QBase):
    def __init__(self):
        super().__init__()

    def EquationQuestion(self):
        question = ['', [], 0]
        choice = [1, 2, 3]
        index = random.choice(choice)
        if index == 1:
            time = random.randint(4, 10)
            q = "A body is dropped from a tower with zero velocity reaches the ground in" + \
                str(time) + 'seconds. What is the height of the tower'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = int(0.5*9.8*time*time)
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(9.8*time*time)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(0.5*9.8*time)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of them'
            question = [q, option, correctIndex]
        elif index == 2:
            v1 = random.randint(5, 10)
            v2 = random.randint(11, 20)
            t1 = random.randint(2, 8)
            t2 = random.randint(1, 5)
            q = 'elif the velocity of particle at an instant is'+str(v1)+'m/s and after '+str(
                t1) + 'seconds the velocity of the particle is'+str(v2)+'m/s, what is the velocity of the particle '+str(t2) + 'seconds before'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            a = v2-v1/t1
            option[indexvalue] = int(v2-a*t2)
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(v2-v1/t1)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(v2-v1/t2)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(v2-v1/t1-t2)
            question = [q, option, correctIndex]
        elif index == 3:
            q = 'Laws of motion is not valid at'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Non inertial'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Inertial'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'at rest'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'moving with uneliform velocity'
            question = [q, option, correctIndex]
        return question

    def generateQuestions(self):
        return (self.EquationQuestion())



def getInstance():
    return EquationGenerator()
