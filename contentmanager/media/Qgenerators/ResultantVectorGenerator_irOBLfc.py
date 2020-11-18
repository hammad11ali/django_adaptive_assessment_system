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
        question = ["", [], 0,detail]
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
            detail="X component of resultant force can be calculated as sqrt of ("+firstForce+" * cos("+firstAngle+"))^2+("+secondForce+" * cos("+secondAngle+"))^2. Answer will be "+option[correctIndex]+""
            question = [q, option, option[correctIndex],detail]

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
            detail="Y component of resultant force can be calculated as sqrt of ("+firstForce+" * sin("+firstAngle+"))^2+("+secondForce+" * sin("+secondAngle+"))^2. Answer will be "+option[correctIndex]+""
            question = [q, option, option[correctIndex],detail]
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
        detail="Range can be calculated by the following formula is: (First force - Second force) to (First force + Second force). So correct answer will be "+correctAnswer+""
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
        detail="Magnitude of resulatant force will be sqrt of ("+firstForce+")^2"+
        "("+firstForce+")^2. Correct answer is "+correctAnswer+""
        question = [q, option, option[correctIndex],detail]
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
