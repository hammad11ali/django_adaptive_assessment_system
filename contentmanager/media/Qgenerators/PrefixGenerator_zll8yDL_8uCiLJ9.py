from . import QGenerator
import random


    def __init__(self):
        super().__init__()
        self.facts = [('Name', 'Unit'), ('atto', '10^-18'),
                      ('femto', '10^-15'), ('pico', '10^-12'), ('nano',
                                                                '10^-9'), ('micro', '10^-6'), ('mili', '10^-3'),
                      ('centi', '10^-2'), ('deci', '10^-1'), ('deca',
                                                              '10^+1'), ('kilo', '10^+3'), ('mega', '10^+6'),
                      ('giga', '10^+9'), ('tera', '10^+12'), ('peta',
                                                              '10^+15'), ('exa', '10^+18')
                      ]

    def generateQuestions(self):
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        sf = random.randrange(1, len(self.facts))
        fact = [self.facts[sf][1], self.facts[sf][0]]
        choices.remove(sf)
        incorrect = []
        for i in range(0, 3):
            si = random.choice(choices)
            row = [self.facts[si][1], self.facts[si][0]]
            choices.remove(si)
            incorrect.append(row)
        return self.simple(fact, incorrect)


def getInstance():
    return PrefixGenerator()
