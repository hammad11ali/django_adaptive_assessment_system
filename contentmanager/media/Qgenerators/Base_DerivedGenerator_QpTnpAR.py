from . import QGenerator
import random
class Base_DeriveGenerator(QGenerator.QBase):
    def __init__(self):
        super().__init__()
        self.baseUnit=[("Meter","Length"),("Kilogram","Mass"),("Second","Time"),("Amphere","Current"),("Kelvin","Temperature"),("Candela","Intensity of Light"),("Mole","Amount of Substance")]
        self.deriveUnit=[("Newton","Force"),("Joule","Work"),("Watt","Power"),("Volt","Potential difference"),("Hertz","Frequency"),("Radian","Angle"),("Pascal","Pressure"),("Coulumb","Electric charge"),("Ohm","Resistance")]
    def whichOne(self,correct,incorrect,relation):
        question=["",[],0]
        q="Which one is "+relation+ ":"
        choices=[0,1,2,3]
        correctIndex=random.choice(choices)
        option=["","","",""]
        option[correctIndex]=correct
        choices.remove(correctIndex)
        for i in range (0,3):
            incorrectIndex=random.choice(choices)
            choices.remove(incorrectIndex)
            option[incorrectIndex]=incorrect[i]
        question=[q,option,correctIndex]
        return question
    
    def generateQuestions(self):
        choices=[0,1,2,3,4,5,6,7]
        baseChoice=[0,1,2,3,4,5,6]
        deriveChoice=[0,1,2,3,4,5,6,7,8]
        index=random.choice(choices)
        incorrect=[]
        if index==0:
            correctIndex=random.choice(baseChoice)
            relation="Base Unit"
            correct=self.baseUnit[correctIndex][0]
            for i in range (0,3):
                deriveIndex=random.choice(deriveChoice)
                deriveChoice.remove(deriveIndex)
                incorrect.append(self.deriveUnit[deriveIndex][0])
            return(self.whichOne(correct,incorrect,relation))
        elif index==1:
            correctIndex=random.choice(deriveChoice)
            relation="Derive Unit"
            correct=self.deriveUnit[correctIndex][0]
            for i in range (0,3):
                baseIndex=random.choice(baseChoice)
                baseChoice.remove(baseIndex)
                incorrect.append(self.baseUnit[baseIndex][0])
            return(self.whichOne(correct,incorrect,relation))
        elif index==2:
            correctIndex=random.choice(deriveChoice)
            relation="not base Unit"
            correct=self.deriveUnit[correctIndex][0]
            for i in range (0,3):
                baseIndex=random.choice(baseChoice)
                baseChoice.remove(baseIndex)
                incorrect.append(self.baseUnit[baseIndex][0])
            return(self.whichOne(correct,incorrect,relation))
        elif index==3:
            correctIndex=random.choice(baseChoice)
            relation="not Derive Unit"
            correct=self.baseUnit[correctIndex][0]
            for i in range (0,3):
                deriveIndex=random.choice(deriveChoice)
                deriveChoice.remove(deriveIndex)
                incorrect.append(self.deriveUnit[deriveIndex][0])
            return(self.whichOne(correct,incorrect,relation))
        elif index==4:
            correctIndex=random.choice(baseChoice)
            relation="Base quantity"
            correct=self.baseUnit[correctIndex][1]
            for i in range (0,3):
                deriveIndex=random.choice(deriveChoice)
                deriveChoice.remove(deriveIndex)
                incorrect.append(self.deriveUnit[deriveIndex][1])
            return(self.whichOne(correct,incorrect,relation))
        elif index==5:
            correctIndex=random.choice(deriveChoice)
            relation="Derive Quzntity"
            correct=self.deriveUnit[correctIndex][1]
            for i in range (0,3):
                baseIndex=random.choice(baseChoice)
                baseChoice.remove(baseIndex)
                incorrect.append(self.baseUnit[baseIndex][1])
            return(self.whichOne(correct,incorrect,relation))
        elif index==6:
            correctIndex=random.choice(deriveChoice)
            relation="not base quantity"
            correct=self.deriveUnit[correctIndex][1]
            for i in range (0,3):
                baseIndex=random.choice(baseChoice)
                baseChoice.remove(baseIndex)
                incorrect.append(self.baseUnit[baseIndex][1])
            return(self.whichOne(correct,incorrect,relation))
        elif index==7:
            correctIndex=random.choice(baseChoice)
            relation="not Derive Quantity"
            correct=self.baseUnit[correctIndex][1]
            for i in range (0,3):
                deriveIndex=random.choice(deriveChoice)
                deriveChoice.remove(deriveIndex)
                incorrect.append(self.deriveUnit[deriveIndex][1])
            return(self.whichOne(correct,incorrect,relation))
            
            

def getInstance():
    return Base_DeriveGenerator()
        