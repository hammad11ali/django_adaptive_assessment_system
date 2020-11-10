from . import QGenerator
import random
import math


class ResultantVector(QGenerator.QBase):

    def __init__(self):
        super().__init__()

    def twoForces(self):
        print("ajhdha")
        firstForce = random.randint(3, 10)
        secondForce = random.randint(5, 15)
        firstAngle = random.randint(30, 70)
        secodAngle = random.randint(30, 70)
        question = ["", [], 0]
        index = [1, 2]
        choice = random.choice(index)
        if choice == 1:
            q = "Two Forces of "+str(firstForce)+" and"+str(secondForce)+" on a body if the force are included at "+str(
                firstAngle)+" and "+str(secodAngle)+" respectively with x-axis then x component of resultant is :"
            firstAnswer = math.sqrt((firstForce*math.cos(firstAngle))**2)
            secondAnswer = math.sqrt((secondForce*math.cos(secodAngle))**2)
            correctAnswer = firstAnswer+secondAnswer
            option = ["", "", "", ""]
            choices = [0, 1, 2, 3]
            correctIndex = random.choice(choices)
            option[correctIndex] = correctAnswer
            choices.remove(correctIndex)
            incorrectIndex = random.choice(choices)
            choices.remove(incorrectIndex)
            option[incorrectIndex] = firstForce
            incorrectIndex = random.choice(choices)
            choices.remove(incorrectIndex)
            option[incorrectIndex] = secondForce
            incorrectIndex = random.choice(choices)
            choices.remove(incorrectIndex)
            option[incorrectIndex] = firstForce+secondForce
            question = [q, option, option[correctIndex]]

        elif choice == 2:
            q = "Two Forces of "+str(firstForce)+" and"+str(secondForce)+" on a body if the force are included at "+str(
                firstAngle)+" and "+str(secodAngle)+" respectively with y-axis then y component of resultant is :"
            firstAnswer = math.sqrt((firstForce*math.cos(firstAngle))**2)
            secondAnswer = math.sqrt((secondForce*math.cos(secodAngle))**2)
            correctAnswer = firstAnswer+secondAnswer
            option = ["", "", "", ""]
            choices = [0, 1, 2, 3]
            correctIndex = random.choice(choices)
            option[correctIndex] = correctAnswer
            choices.remove(correctIndex)
            incorrectIndex = random.choice(choices)
            choices.remove(incorrectIndex)
            option[incorrectIndex] = firstForce
            incorrectIndex = random.choice(choices)
            choices.remove(incorrectIndex)
            option[incorrectIndex] = secondForce
            incorrectIndex = random.choice(choices)
            choices.remove(incorrectIndex)
            option[incorrectIndex] = firstForce+secondForce
            question = [q, option, option[correctIndex]]
        return question

    def rangeVector(self):
        firstForce = random.randint(3, 20)
        secondForce = random.randint(5, 15)
        question = ["", [], 0]
        q = "A vector of magnitude "+str(firstForce)+" is added to a vector magnitude "+str(
            secondForce)+" while orientation are changeable. What is its range "
        correctAnswer = str(abs(firstForce-secondForce)) + \
            " to " + str(firstForce+secondForce)
        option = ["", "", "", ""]
        choices = [0, 1, 2, 3]
        correctIndex = random.choice(choices)
        option[correctIndex] = correctAnswer
        choices.remove(correctIndex)
        incorrectIndex = random.choice(choices)
        choices.remove(incorrectIndex)
        option[incorrectIndex] = str(firstForce) + " to "+str(secondForce)
        incorrectIndex = random.choice(choices)
        choices.remove(incorrectIndex)
        option[incorrectIndex] = str(secondForce+secondForce)+" to Zero"
        incorrectIndex = random.choice(choices)
        choices.remove(incorrectIndex)
        option[incorrectIndex] = str(
            firstForce+secondForce) + " to "+str(firstForce)
        question = [q, option, option[correctIndex]]
        return question

    def zeroAngle(self):
        firstForce = random.randint(3, 20)
        secondForce = random.randint(5, 15)
        question = ["", [], 0]
        q = "Two Forces of "+str(firstForce)+" and "+str(secondForce) + \
            " act on a body such that angle between forces is zero then magnitude will be: "
        firstAnswer = math.sqrt((firstForce)**2)
        secondAnswer = math.sqrt((secondForce)**2)
        correctAnswer = firstAnswer+secondAnswer
        option = ["", "", "", ""]
        choices = [0, 1, 2, 3]
        correctIndex = random.choice(choices)
        option[correctIndex] = correctAnswer
        choices.remove(correctIndex)
        incorrectIndex = random.choice(choices)
        choices.remove(incorrectIndex)
        option[incorrectIndex] = firstForce
        incorrectIndex = random.choice(choices)
        choices.remove(incorrectIndex)
        option[incorrectIndex] = secondForce
        incorrectIndex = random.choice(choices)
        choices.remove(incorrectIndex)
        option[incorrectIndex] = firstForce+secondForce-2
        question = [q, option, option[correctIndex]]
        return question

    def generateQuestions(self):
        choices = [1, 2, 3]
        index = random.choice(choices)
        if index == 1:
            return (self.twoForces())
        elif index == 2:
            return (self.rangeVector())
        elif index == 3:
            return (self.zeroAngle())


def getInstance():
    return ResultantVector()
