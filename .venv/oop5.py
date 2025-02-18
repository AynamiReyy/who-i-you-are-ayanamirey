class Student:
    def __init__ (self, name = None, age = None, grade =  None, scores = None):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores
    def average_score(self):
        return sum(self.scores) / len(self.scores)