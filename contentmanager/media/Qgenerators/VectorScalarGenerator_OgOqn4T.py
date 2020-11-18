from . import QGenerator
import random


class VectorScalarGenerator(QGenerator.QBase):
    def __init__(self):
        super().__init__()
        self.scalar = ["time", "Volume", "speed", "mass", "temperature", "distance", "Entropy", "Energy", "Work",
                       "Area", "Power", "Current", "Cost", "Size", "Length", "Caleries", "Density", "Reflective Index"]
        self.vector = ["Acceleration", "velocity", "Momentum", "Force", "Weight",
                       "Displacement", "Lift", "Torque", "Electric Field", "Thrust", "Drag"]

    def whichOne(self, correct, incorrect, relation):
        question = ["", [], 0]
        q = "Which one is "+relation + ":"
        choices = [0, 1, 2, 3]
        correctIndex = random.choice(choices)
        option = ["", "", "", ""]
        option[correctIndex] = correct
        choices.remove(correctIndex)
        for i in range(0, 3):
            incorrectIndex = random.choice(choices)
            choices.remove(incorrectIndex)
            option[incorrectIndex] = incorrect[i]
        detail=""+correct+" is a "+relation+". It is basic information related to vector and scalar"
        question = [q, option, correctIndex,detail]
        return question

    def generateQuestions(self):
        choices = [1, 2]
        scalarchoices = [1, 2, 3, 4, 5, 6, 7, 8,
                         9, 10, 11, 12, 13, 14, 15, 16, 17]
        vectorchoices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        index = random.choice(choices)
        incorrect = []
        if index == 1:
            correctIndex = random.choice(scalarchoices)
            scalarchoices.remove(correctIndex)
            relation = "Scalar"
            correct = self.scalar[correctIndex]
            for i in range(0, 3):
                deriveIndex = random.choice(vectorchoices)
                vectorchoices.remove(deriveIndex)
                incorrect.append(self.vector[deriveIndex])
            return(self.whichOne(correct, incorrect, relation))
        elif index == 2:
            correctIndex = random.choice(vectorchoices)
            vectorchoices.remove(correctIndex)
            relation = "Vector"
            correct = self.vector[correctIndex]
            for i in range(0, 3):
                deriveIndex = random.choice(scalarchoices)
                scalarchoices.remove(deriveIndex)
                incorrect.append(self.scalar[deriveIndex])
            return(self.whichOne(correct, incorrect, relation))


def getInstance():
    return VectorScalarGenerator()
