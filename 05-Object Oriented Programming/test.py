# class Dog():
#     def __init__(self,name,breed,sex):
#         self.name = name
#         self.breed = breed
#         self.sex = sex

#     def speak(self):
#         return f'Woof, my name is {self.name}'
    
#     def tosex(self):
#         return f'Woof, I am a {self.sex}, looking for a partner'
    
#     def mybreed(self):
#         return f"Woof, my breed is {self.breed}, looking forward to meet another breeds"
    
# dog = Dog('Lost','Dvirterier','Boy')

# print(dog.speak())
# print(dog.mybreed())
# print(dog.tosex())

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self,distance):
        self.distance = distance
    
    def slope(self):
        return self.coor1 - self.coor2


coor1 = (3,2)
coor2 = (8,10)
l = Line(coor1,coor2)
l.distance()