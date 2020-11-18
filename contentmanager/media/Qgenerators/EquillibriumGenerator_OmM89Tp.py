from . import QGenerator
import random


class EquillbriumGenerator(QGenerator.QBase):

    def __init__(self):
        super().__init__()

    def Equillibrium(self):
        question = ["", [], 0,""]
        chices = [1, 2, 3, 4, 5]
        index = random.choice(chices)
        if index == 1:
            q = " A body at rest or moving with uniform velocity will have acceleration :"
            option = ["", "", "", ""]
            option[0] = "1"
            option[1] = "max"
            option[2] = "min"
            option[3] = "0"
            correctIndex = 3
            detail="When body is moving with uniform velocity then it means chnage of velocity is 0. We know change of velocity is acceleration so acceleration will be zero."
            question = [q, option, correctIndex,detail]
        elif index == 2:
            q = "To satisfy first condition of equilibrium, if rightward forces are positive, leftward forces must be :"
            option = ["", "", "", ""]
            option[0] = "Positive"
            option[1] = "Negative"
            option[2] = "double"
            option[3] = "halved"
            detail="To satisfy first condition net force must be zero so if force act on rightward direction is positive then force on leftward direction must be negative then net force will be zero."
            correctIndex = 1
            question = [q, option, correctIndex,detail]
        elif index == 3:
            q = "Sum of all the forces acting on a body is zero. This condition represents equilibrium's:"
            option = ["", "", "", ""]
            option[0] = "first Condition"
            option[1] = "Seccond Condition"
            option[2] = "Third Condition"
            option[3] = "Fourth Condition"
            detail="Net force must be zero is first condition of equillibrium."
            correctIndex = 0
            question = [q, option, correctIndex,detail]
        elif index == 4:
            q = " If a body is in rest or in uniform velocity, it is said to be in:"
            option = ["", "", "", ""]
            option[0] = "rest"
            option[1] = "Uniform"
            option[2] = "Equillibrium"
            option[3] = "constant Force"
            detail="If body is in rest or move with uniform velocity then body is in equillibrium."
            correctIndex = 2
            question = [q, option, correctIndex,detail]
        elif index == 5:
            q = "To satisfy the first condition of equilibrium, if upward forces are positive then downward forces must bes:"
            option = ["", "", "", ""]
            option[0] = "Positive"
            option[1] = "Negative"
            option[2] = "double"
            option[3] = "halved"
            correctIndex = 1
            detail="To satisfy first condition net force must be zero so if force act on upward direction is positive then force on downward direction must be negative then net force will be zero."
            question = [q, option, correctIndex,detail]
        return question

    def generateQuestions(self):
        return (self.Equillibrium())


def getInstance():
    return EquillbriumGenerator()
