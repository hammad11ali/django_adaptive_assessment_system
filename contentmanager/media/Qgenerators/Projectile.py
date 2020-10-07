import random
from . import QGenerator
import math


class EnergyQuestion(QGenerator.QBase):
    def __init__(self):
        super().__init__()

    def kineticEnergy(self):
        question = ["", [], 0]
        choice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        index = random.choice(choice)
        if index == 1:
            q = "A lelift is descending at a constant speed V. A passenger in the lelift drops a coin. The acceleration of the coin move towards a floor will be"
            option = ['', '', '', '']
            option[0] = 'g'
            option[1] = '-g'
            option[2] = 'Zero'
            option[3] = 'V+g'
            correctIndex = 0
            question = [q, option, correctIndex]
        elif index == 2:
            q = 'An object thrown upward with an initial velocity at certain angle with the horizental and moving freelyunder the gravity called'
            option = ['', '', '', '']
            option[0] = 'a rocket'
            option[1] = 'an aeroplane'
            option[2] = 'a projectile'
            option[3] = 'a ballon'
            correctIndex = 2
            question = [q, option, correctIndex]
        elif index == 3:
            weight = random.randint(1, 4)
            Energy = random.randint(2, 6)
            q = "A body of weight" + \
                str(weight)+" has a kinetic energy" + \
                str(Energy)+" when its speed is"
            mass = weight/9.8
            option = ['', '', '', '']
            option[0] = weight*Energy
            option[1] = int(2*Energy/mass)
            option[2] = int(math.sqrt((2*Energy/mass)))
            option[3] = int(math.sqrt((Energy/mass)))
            correctIndex = 2
            question = [q, option, correctIndex]
        elif index == 4:
            height = random.randint(10, 300)
            q = "An object is dropped from a height of " + \
                str(height) + " its velocity at the moment at touches the ground is"
            option = ['', '', '', '']
            option[0] = int(height/2)
            option[1] = int(height*2/3)
            t = math.sqrt((height/4.9))
            option[2] = int(9.8*t)
            option[3] = height
            correctIndex = 2
            question = [q, option, correctIndex]
        elif index == 5:
            projectileRange = random.randint(30, 70)
            angle = [15, 30, 45, 60, 75, 90]
            theetha = random.choice(angle)
            angle.remove(theetha)
            theetha1 = random.choice(angle)
            q = 'A range of Projectile is '+str(projectileRange)+' when Θ is iclined with horizental '+str(
                theetha)+' what is range when Θ becomes '+str(theetha1)+' '
            option = ['', '', '', '']
            r1 = math.sin(2*theetha)
            r2 = math.sin(2*theetha1)
            answer = r2/r1*projectileRange
            option[0] = int(projectileRange*r1)
            option[1] = int(projectileRange*r2)
            option[3] = int(answer)
            option[2] = int(projectileRange)
            correctIndex = 3
            question = [q, option, correctIndex]
        elif index == 6:
            q = "At the top of the trajectory of a projectile acceleration is "
            option = ['', '', '', '']
            option[0] = '-g'
            option[1] = 'g'
            option[2] = 'a'
            option[3] = 'v/t'
            correctIndex = 1
            question = [q, option, correctIndex]
            correctIndex = random.choice(choice)
        elif index == 7:
            q = 'A projectile attains  maximum  horizental range  when it is projected at an angle of '
            option = ['', '', '', '']
            option[0] = '30'
            option[1] = '45'
            option[2] = '60'
            option[3] = '90'
            correctIndex = 1
            question = [q, option, correctIndex]
        elif index == 8:
            q = 'The horizental range of projectile, at a certain place, depends upon'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'angle as well as velocity of projection'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'velocity of projection'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'mass of projectile'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'angle of projection'
            question = [q, option, correctIndex]
        elif index == 9:
            q = 'The Projectile motion is composed of'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'horizental and vertical motion'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'horizental motion'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'vertical motion'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of them'
            question = [q, option, correctIndex]
        elif index == 10:
            q = 'The motion of projectile is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'two dimension'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'one dimention'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'three dimention'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'four dimention'
            question = [q, option, correctIndex]
        elif index == 11:
            q = 'A typical rocket ejects the burnts gases at speed over'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = '40000ms^-1'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '4000ms^-1'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '400ms^-1'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '400000ms^-1'
            question = [q, option, correctIndex]
        elif index == 12:
            angles = [30, 45, 60, 90]
            angle1 = random.choice(angles)
            angles.remove(angle1)
            angle2 = random.choice(angles)
            height = random.randint(10, 25)
            q = 'Maximum height of a bullet when fixed at '+str(angle1)+' with horizental is '+str(
                height)+'. Then height will be when it is fired at '+str(angle2)+''
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            velocity = int(height*2*9.8/(math.sin(angle1)*math.sin(angle1)))
            option[indexvalue] = int(
                (velocity*math.sin(angle2)*math.sin(angle2))/(2*9.8))
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(
                velocity*math.sin(angle2)*math.sin(angle2))
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = velocity*math.sin(angle2)*math.sin(angle2)/9.8
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(velocity*math.sin(angle2)/9.8)
            question = [q, option, correctIndex]
        elif index == 13:
            q = 'During upward motion of projectile, the vertical component of velocity'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'decreasing'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'increasing'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'constant'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'independent'
            question = [q, option, correctIndex]
        elif index == 14:
            v = random.randint(400, 800)
            angles = [30, 45, 60, 90]
            angle = random.choice(angles)
            q = 'The horizental component of a projectile is moving with inital velocity of ' + \
                str(v)+'m/s at angle of '+str(angle)+'to x axis is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = int(v*math.sin(angle))
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = v
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = v*math.cos(angle)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Zero'
            question = [q, option, correctIndex]
        elif index == 15:
            q = 'Which of the following is dimensionless'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'angle'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'mass'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'density'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'temperature'
            question = [q, option, correctIndex]
        elif index == 16:
            q = 'The horizental and vertical rangewill be equalid angle of projection'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = '76'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '45'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '60'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '30'
            question = [q, option, correctIndex]
        elif index == 17:
            q = 'The projectile attain a maximum horizental range is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = '45'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '76'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '60'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '30'
            question = [q, option, correctIndex]
        return question

    def generateQuestions(self):
        return (self.kineticEnergy())


def getInstance():
    return  EnergyQuestion()
