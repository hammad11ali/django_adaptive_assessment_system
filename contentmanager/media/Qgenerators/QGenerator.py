import random
class QBase:
    def __init__(self):
        self.name="base"
    def printName(self):
        print(self.name)
    def isOf(self,fact,relation,incorrect):
        question=("",[], 0,detail)
        gIndex=random.choice([0,1])
        if gIndex==0:
            given=fact[0]
            ans=fact[1]
            q=given+ " is "+ relation + " of __________:"
            ansList=["","","",""]
            choices=[0,1,2,3]
            selected=random.choice(choices)
            ansList[selected]=ans
            correctIndex=selected
            choices.remove(selected)
            for i in range(0,3):
                selected=random.choice(choices)
                ansList[selected]=incorrect[i][1]
                choices.remove(selected)
            detail="It is basic information"
            question=(q,ansList,correctIndex,detail)
        elif gIndex==1:
            given=fact[1]
            ans=fact[0]
            q= relation + " of " + given + " is "
            ansList=["","","",""]
            choices=[0,1,2,3]
            selected=random.choice(choices)
            ansList[selected]=ans
            correctIndex=selected
            choices.remove(selected)
            for i in range(0,3):
                selected=random.choice(choices)
                ansList[selected]=incorrect[i][0]
                choices.remove(selected)
            detail="It is basic information"
            question=(q,ansList,correctIndex,detail)
        return question
    def whichIs(self,fact,relation,incorrect):
        question=("",[], 0)
        given=fact[1]
        q="Which"+ " is "+ relation + " of "+given+":"
        ansList=["","","",""]
        choices=[0,1,2,3]
        selected=random.choice(choices)
        ansList[selected]=fact[0]
        correctIndex=selected
        choices.remove(selected)
        for i in range(0,3):
            selected=random.choice(choices)
            ansList[selected]=incorrect[i][0]
            choices.remove(selected)
        detail="It is basic information"
        question=(q,ansList,correctIndex,detail)
        return question
    def whatIs(self,fact,relation,incorrect):
        question=("",[], 0)
        given=fact[1]
        q="Which"+ " is "+ relation + " of "+given+":"
        ansList=["","","",""]
        choices=[0,1,2,3]
        selected=random.choice(choices)
        ansList[selected]=fact[0]
        correctIndex=selected
        choices.remove(selected)
        for i in range(0,3):
            selected=random.choice(choices)
            ansList[selected]=incorrect[i][0]
            choices.remove(selected)
        detail="It is basic information"
        question=(q,ansList,correctIndex,detail)
        return question
    
    def simple(self,fact,incorrect):
        question=("",[], 0)
        given=fact[1]
        q=given+" is equal to: "
        ansList=["","","",""]
        choices=[0,1,2,3]
        selected=random.choice(choices)
        ansList[selected]=fact[0]
        correctIndex=selected
        choices.remove(selected)
        for i in range(0,3):
            selected=random.choice(choices)
            ansList[selected]=incorrect[i][0]
            choices.remove(selected)
        detail="It is basic information"
        question=(q,ansList,correctIndex,detail)
        return question
    
    def How(self,fact,incorrect):
        question=("",[], 0)
        given=fact[0][0]
        q=given+" have significant Figure: "
        ansList=["","","",""]
        choices=[0,1,2,3]
        selected=random.choice(choices)
        ansList[selected]=fact[0][1]
        correctIndex=selected
        choices.remove(selected)
        for i in range(0,3):
            selected=random.choice(choices)
            ansList[selected]=incorrect[i][0]
            choices.remove(selected)
        detail="It is basic information"
        question=(q,ansList,correctIndex,detail)
        return question