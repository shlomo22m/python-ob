from animal import  Animal

class Bird(Animal):

    def birdfly(self,speed):
        super().__init__()
        self.speed=speed


    def birdsspeed(self):
        print('birds fly speed ' + str(self.speed))

    def birdmakesound(self):
        super().makesound('tweet')

    def move(self):
        print('bird move')