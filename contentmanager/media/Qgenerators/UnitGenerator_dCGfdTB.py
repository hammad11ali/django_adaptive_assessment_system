from . import QGenerator
import random


class UnitGenerator(QGenerator.QBase):
    def __init__(self):
        super().__init__()
        self.facts = [("Name", "Formula", "Unit", "Dimension"),
                      ("Potential Difference", "IR", "Volt", "[ML2T-3I-1]"),
                      ("Current", "V/R", "Ampere", "[I-1]"),
                      ("Energy", "1/2 *mv2", "Newtonmeter", "[ML2T-2]"),
                      ("Power", "w/ΔT", "Watt", "[ML2T-3]"),
                      ("Torque", "rfsinθ", "Newtonmeter", "[ML2T-2]"),
                      ("Work", "F*d", "Newtonmeter", "[ML2T-2]"),
                      ("Force", "ma", "Newton", "[MLT-2]"),
                      ("Momentum", "mv", "Kgm/s", "[MLT-1]"),
                      ("Acceleration", "ΔV/ΔT", "m/s2", "[LT-2]"),
                      ("Velocity", "Δd/Δt", "m/s", "[LT-1]"),
                      ("Angular Acceleration", "Δw/ΔT", "rad/s2", "[T-2]"),
                      ("Angular Velocity", "θ/ΔT", "rad/s", "[T-1]"),
                      ("Gravitational Constant",
                       "Fr2/m1m2", "m3/kgs2", "[M-1L3T-2]"),
                      ("Angular Momentum", "rxp", "kgm2/s", "[ML2T-1]")]

    def generateQuestions(self):
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        sf = random.randrange(1, len(self.facts))
        sr = random.randrange(1, len(self.facts[0]))
        fact = [self.facts[sf][sr], self.facts[sf][0]]
        relation = self.facts[0][sr]
        choices.remove(sf)
        incorrect = []
        for i in range(0, 3):
            si = random.choice(choices)
            row = [self.facts[si][sr], self.facts[si][0]]
            choices.remove(si)
            incorrect.append(row)

        # Select Question to Generate
        q = random.randrange(0, 3)
        if q == 0:
            return self.isOf(fact, relation, incorrect)
        elif q == 1:
            return self.whichIs(fact, relation, incorrect)
        elif q == 2:
            return self.whatIs(fact, relation, incorrect)
        else:
            return "nothing"


def getInstance():
    return UnitGenerator()
