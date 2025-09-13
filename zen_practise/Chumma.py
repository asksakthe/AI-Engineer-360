class Employee :
    
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id= employee_id
     

class Tester(Employee):
    def __init__(self,name, employee_id):
        super().__init__(name,employee_id) 
        
    def run_tests(self):
        print(f"{self.name} and the id is {self.employee_id}")
        

e1 = Tester('sakthee', 'E797')
e1.run_tests()

