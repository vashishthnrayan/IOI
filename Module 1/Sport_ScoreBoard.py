class Cricket:
    def __init__(self,player,score):
            self.__player = player
            self.__score = score

    def info(self):
        print("Cricket Player name",self.__player,"palyer Score",self.__score)

    def play(self):
         print(self.__player,"hits a 6")

        
