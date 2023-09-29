#!/usr/bin/env python

from user import User

import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
        
    
    def teach(self):
        if self.knowledge:
           return random.choice(self.knowledge)
        else:
           return f"Knowledge base is empty"

    # def teach(self):
    #     if self.knowledge:
    #         random_index = random.randint(0, len(self.knowledge) - 1)
    #         return self.knowledge[random_index]
    #     else:
    #         return "Knowledge base is empty."


teacher = Teacher("Julius", "Nyerere", knowledge)
# print(teacher.knowledge)

print(teacher.teach())
