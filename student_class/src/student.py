class Student:
    def __init__ (self, student_name, cohort):
        self.name = student_name
        self.cohort = cohort

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, favourite_language):
        return f"I love {favourite_language}"