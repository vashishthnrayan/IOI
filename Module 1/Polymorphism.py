class cricket:
    def __init__(self,player_name,score):
        self.__player_name = player_name
        self.__score = score
        
    def get_score(self):
        return self.__score
    
    def set_score(self,new_score):
        if new_score >=0:
            self.__score= new_score 

Cricket=cricket("Rohit",85)

cricket.__score = 999
print(Cricket.get_score())
Cricket.set_score(100)
print(Cricket.get_score())
