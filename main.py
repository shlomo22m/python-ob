

from animal import Animal
from dog import  Dog
from bird import Bird
from factory import Fact
from singletone import SingeltoneClass
from person import Person
#a = Animal()
#a.sleep(3)
'''d=Dog(3)
d.run()
d.sleep(5)
d.dogmakesound()
d.move()

b=Bird()
b.birdfly(9)
b.birdsspeed()
b.birdmakesound()
b.move()'''

r = Fact(2)
x = r.getobject()
x.drink()

'''obj1= SingeltoneClass()
print(obj1)

obj2=SingeltoneClass()
print(obj2)'''

p=Person()