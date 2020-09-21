from . import QGenerator
import random


class SignificantGenerator(QGenerator.QBase):
    def __init__(self):
        super().__init__()
        self.facts = [('.42000', 5), ('2.3400', 5), ('1.30', 3), ('0.0032', 2), ('1.3213', 5),
                      ('1.23007', 6), ('0.0892109', 6), ('0.098706', 5), ('2.0870', 5), ('0.0876108', 6)]

    def generateQuestions(self):
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sf = random.choice(choices)
        fact = [self.facts[sf]]
        choices.remove(sf)
        incorrect = []
        for i in range(0, 3):
            si = random.choice(choices)
            row = [self.facts[si][1]]
            choices.remove(si)
            incorrect.append(row)
        return self.How(fact, incorrect)


def getInstance():
    return SignificantGenerator()
