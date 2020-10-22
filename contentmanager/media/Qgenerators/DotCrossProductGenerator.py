import random
from . import QGenerator

class DostCrossGenerator(QGenerator.QBase):
    
    
    def __init__(self):
        super().__init__()

    
    def CrossDotProduct(self):
        question=["",[],0]
        chices=[1,2,3,4,5]
        index=random.choice(chices)
        if index==1:
            q="Vector Product of Two vector is also known as :"
            option=["","","",""]
            option[0]="Dot Product"
            option[1]="Cross Product"
            option[2]="Self Product"
            option[3]="Point Product"
            correctIndex=1
            question=[q,option,correctIndex]
        elif index==2:
            q="Multiplication of Two product is :"
            option=["","","",""]
            option[0]="2 Type"
            option[1]="3 Type"
            option[2]="1 Type"
            option[3]="4 Type"
            correctIndex=0
            question=[q,option,correctIndex]
        elif index==3:
            q="Cross product of A B at angle 0 degree:"
            option=["","","",""]
            option[0]="AB"
            option[1]="A.B"
            option[2]="AxB"
            option[3]="A"
            correctIndex=0
            question=[q,option,correctIndex]
        elif index==4:
            q="Dot product of A B at angle 180 degree:"
            option=["","","",""]
            option[0]="-AB"
            option[1]="A.B"
            option[2]="AxB"
            option[3]="A"
            correctIndex=0
            question=[q,option,correctIndex]
        elif index==5:
            q="Cross product of two same vectors is equal to:"
            option=["","","",""]
            option[0]="0"
            option[1]="1"
            option[2]="j"
            option[3]="j.j"
            correctIndex=0
            question=[q,option,correctIndex]
        return question
    def generateQuestions(self):
        return (self.CrossDotProduct())


def getInstance():
    return DostCrossGenerator()

