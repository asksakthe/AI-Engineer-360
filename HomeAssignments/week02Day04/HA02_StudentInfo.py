class Student:
# Constructor to initialize Student Attributes    
    def __init__(self,name,grade,department):
        self.name = name
        self.grade = grade
        self.department = department
        

    def print_info(self):
        return f"Student {self.name} has '{self.grade}' from {self.department} Department"
        
    
    def update_grade(self, grade_update):
        self.grade_update = grade_update
        self.grade = self.grade_update
        return f"Student {self.name} has updated grade is to '{self.grade}' from {self.department} Department"
        
        
        
if __name__ == "__main__":
    print("student list")
        