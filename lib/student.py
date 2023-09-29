#!/usr/bin/env python

from user import User

class Student(User):
   
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, topic):
        self.knowledge.append(topic)
            

medrine =Student("Medrine", "Mulindi")
medrine.learn("python")
medrine.learn("sqlalchemy")
print(medrine.knowledge)

ariella = Student("Ariell", "Kidini")
ariella.learn("javascript")
ariella.learn("css")

print(ariella.knowledge)
        

