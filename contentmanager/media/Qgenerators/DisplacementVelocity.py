import random
from . import QGenerator
import math


class Displacement_VelocityGenerator(QGenerator.QBase):
    def __init__(self):
        super().__init__()

    def VelocityDispacement(self):
        question = ["", [], 0]
        choice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        index = random.choice(choice)
        if index == 1:
            len1 = random.randint(100, 200)
            len2 = random.randint(150, 250)
            speed1 = random.randint(30, 60)
            speed2 = random.randint(40, 80)
            q = 'A '+str(len1)+'m long train is moving with the speed'+str(speed1)+'m/s. A train B is moving with the speed '+str(
                speed2)+'m/s in opposite direction and length of train is '+str(len2)+'m. At which time these train crosses each other'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = int(len1+len2/speed2+speed1)
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(len1/speed1)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(len2/speed2)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(len1+len2/speed1)
            question = [q, option, correctIndex]
        elif index == 2:
            distance = random.randint(5, 12)
            speed1 = random.randint(2, 6)
            speed2 = random.randint(4, 8)
            q = 'A body waalks to his school at a distance of '+str(distance)+'km with the speed of '+str(
                speed1)+'km/h and walks back at a constant speed of '+str(speed2)+'km/h . His average speed expressed in km/h'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            t1 = distance/speed1
            t2 = distance/speed2
            option[indexvalue] = int(distance*2/t1+t2)
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(distance/t1)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(distance/t2)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = distance
            question = [q, option, correctIndex]
        elif index == 3:
            speed1 = random.randint(20, 60)
            speed2 = random.randint(40, 80)
            q = 'A car travels first half distance between two places with a speed of ' + \
                str(speed1)+'km/h and remaining half with the speed of ' + \
                str(speed2)+'km/h. Then the average speed is'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            distance = 10
            t1 = distance/speed1
            t2 = distance/speed2
            option[indexvalue] = int(distance*2/t1+t2)
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(distance/t1)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(distance/t2)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = distance
            question = [q, option, correctIndex]
        elif index == 4:
            mass1 = random.randint(10, 20)
            mass2 = random.randint(5, 15)
            q = 'Two bodies of masses '+str(mass1)+'kg and '+str(
                mass2)+'kg are dropped from the roof.A point 20cm above the ground both the body have same '
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = 'Velocity'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Momentum'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'Kinetic Energy'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 5:
            flow = random.randint(2, 5)
            velocity = random.randint(5, 15)
            q = 'Suppose the  water flows out from the pipe at '+str(flow)+'kgs^-1 and its velocity changes from '+str(
                velocity)+'ms^-1 to zero on striking the wall then force exerted by water onwall will be'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = flow*velocity
            # flow(vf-vi)
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(velocity/2*3)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(flow*3/2)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of these'
            question = [q, option, correctIndex]
        elif index == 6:
            q = 'elif speed of electron is 5×10^5m/s. how long does it takes one electron to traverse 1m'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = '2x10^-6s'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '1x10 ^ -6s'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = '2x10^-7s'
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = 'none of them'
            question = [q, option, correctIndex]
        elif index == 7:
            mag1 = random.randint(5, 20)
            mag2 = random.randint(10, 15)
            q = 'elif magnitude of first dispacement is '+str(mag1)+'m an magnitude of second displacement is '+str(
                mag2)+'m and which is perpendicular to each other then resultant dispalcement will be'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = int(math.sqrt(mag1*mag1+mag2*mag2))
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = (mag1*mag1+mag2 * mag2)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(math.sqrt(mag1+mag2))
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = (mag1+mag2)
            question = [q, option, correctIndex]
        elif index == 8:
            q = 'What ratios are the distances traveled by a body falling from rest in the first, second, and third seconds in'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = '1:3:5'
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = "1:2:3"
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = "1:4:9"
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = "1:5:11"
            question = [q, option, correctIndex]
        elif index == 9:
            distance = random.randint(100, 200)
            v1 = random.randint(5, 15)
            v2 = random.randint(3, 10)
            q = 'A train of length '+str(distance)+'m is moving towards north direction with speed '+str(
                v1)+'m/s and a parrot is moving towards south with the speed of '+str(v2)+'m/s . The time taken ti cross parrot to train'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = int(distance/(v1+v2))
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(distance/v1)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(distance/v2)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = v1*v2
            question = [q, option, correctIndex]
        elif index == 10:
            distance1 = random.randint(50, 90)
            distance2 = random.randint(10, 30)
            q = 'A train cover ' + \
                str(distance1)+'km in half hour. Then time taken by it to travel ' + \
                str(distance2)+'km will be'
            choices = [0, 1, 2, 3]
            indexvalue = random.choice(choices)
            option = ['', '', '', '']
            option[indexvalue] = int(distance2/(distance1/30))
            correctIndex = indexvalue
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(distance2/30)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int(distance1/30)
            choices.remove(indexvalue)
            indexvalue = random.choice(choices)
            option[indexvalue] = int((distance1+distance2)/30)
            question = [q, option, correctIndex]
        return question

    def generateQuestions(self):
        return (self.VelocityDispacement())



def getInstance():
    return Displacement_VelocityGenerator()
