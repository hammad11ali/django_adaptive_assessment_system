import random
from . import QGenerator
import math


class WorkdoneQuestion(QGenerator.QBase):
    def __init__(self):
        super().__init__()

    def generateQuestions(self):
        question = ['', [], 0]
        choice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                  13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        index = random.choice(choice)
        if index == 1:
            q = 'A labourer carrying a load on his head moves from rest  on the horizental road to another point where he comes to rest. The toal work done is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'zero work'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'maximum work'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'minimum work'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 2:
            q = 'Which of the following force cannot do any work'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Centripetal force'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Electric force'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Frictional force'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Gravitational force'
            question = [q, option, correctIndex]
        elif index == 3:
            q = 'Work is quantity'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Scalar'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Vector'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'non-pysical'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 4:
            q = 'In the force applied to parallel to the direction of motion, then the work done is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Negative'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Positive'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'zero'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 5:
            q = 'A field in which  the work done is moving a body along closed path is zero called'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Conservative Field'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Nuclear Field'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Gravitational field'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none conservative field'
            question = [q, option, correctIndex]
        elif index == 6:
            q = 'Work done in lower and bucket into the well is: '
            # q = 'In the force applied to parallel to the direction of motion, then the work done is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Negative'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Positive'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'zero'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 7:
            distance = random.randint(10, 50)
            force = random.randint(5, 10)
            angles = [30, 60, 90]
            angle = random.choice(angles)
            q = 'elif the distance is '+str(distance)+'m and applied force on body is '+str(
                force)+'N at an angle of '+str(angle)+' then the total work done is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = int(force*distance*math.cos(angle))
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(force*distance*math.sin(angle))
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Both '
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 8:
            q = 'Work has dimension as that of: '
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Torque'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Angular Momentum'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Linear Momentum'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Power'
            question = [q, option, correctIndex]
        elif index == 9:
            q = 'Tick the conservation force '
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Elasitc spring'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Tension in string'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Frictional Force'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Ait resistance force'
            question = [q, option, correctIndex]
        elif index == 10:
            q = 'Most of the geysers occur in'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Volcanic region'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Magnetic region'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Northen region'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 11:
            q = 'The field in which work done in moving a body between two points independent of path called'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Non Conservative'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Conservative'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Electric Field'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Potential Field'
            question = [q, option, correctIndex]
        elif index == 12:
            q = 'elif force and displacement are in opposite direction then work done will be '
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Negative'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Positive'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'zero'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 13:
            m = random.randint(2, 5)
            d = random.randint(1, 5)
            t = random.randint(30, 60)
            q = 'A '+str(m)+'kg block is held '+str(d) + \
                'm above the floor for '+str(t)+'seconds, the work done is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'zero'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = m*d
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = m*d*t
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = m*t
            question = [q, option, correctIndex]
        elif index == 14:
            q = 'Which force is non conservative '
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Frictional force'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Gravitational force'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Electric force'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Elastic spring force'
            question = [q, option, correctIndex]
        elif index == 15:
            q = 'Work done on a body by a gravity in lelifting it up on a certain height is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Negative'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Positive'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Maximum'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'minimun'
            question = [q, option, correctIndex]
        elif index == 16:
            q = 'When a body moves against the force of friction on a horizental plane, the work done by a body is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Negative'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Positive'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Maximum'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'minimun'
            question = [q, option, correctIndex]
        elif index == 17:
            q = 'Work done on an object is independent of'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Initial Velocity of the body'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Displacement'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Force applid'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Angle'
            question = [q, option, correctIndex]
        elif index == 18:
            q = 'The work done by a force, keeping an object in circular motion with constant speed'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Zero J'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '1 J'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '0.1 J'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '0.01 J'
            question = [q, option, correctIndex]
        elif index == 19:
            q = 'When force and displacement are perpendicular to each other then work will be'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Zero'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Maximum'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Minimum'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'moderate'
            question = [q, option, correctIndex]
        elif index == 20:
            q = 'The work done by a moving body between two points in a conservative field is independent of the'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Path followed by a body'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Power'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Direction'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Force applied'
            question = [q, option, correctIndex]
        elif index == 21:
            q = 'Maximum work is done when force and displacement are'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Parallel'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'AntiParallel'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Perpendicular'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'None'
            question = [q, option, correctIndex]
        elif index == 22:
            q = 'The unit of work in CGS is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Erg'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'joule'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'dyne'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'watt'
            question = [q, option, correctIndex]
        elif index == 23:
            q = 'When two protons are broght close to each other potential energy will be'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Increase'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Decrease'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'remain same'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'decrease or same'
            question = [q, option, correctIndex]
        elif index == 24:
            q = '1J is equal to'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = '10^7 Erges'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '10^6 Erges'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '10^5 Erges'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '10^8 Erges'
            question = [q, option, correctIndex]
        elif index == 25:
            q = 'The angle between centripetal force and displacement when body moves in a circular path is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = '180'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '90'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '45'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '60'
            question = [q, option, correctIndex]
        elif index == 26:
            q = 'Area under the force displacement graph is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'work'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Power'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'heat'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Energy'
            question = [q, option, correctIndex]
        return question


def getInstance():
    return WorkdoneQuestion()

''
