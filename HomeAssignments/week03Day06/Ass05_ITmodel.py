class Employee:
    def __init__(self,name,emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        return f"The Details of Employee: \n\tname:{self.name}\n\tID:{self.emp_id}\n\tDept:{self.department}"
    

class Manager(Employee):
    def __init__(self,name,emp_id, department,team_size):
        super().__init__(name,emp_id, department)
        self.team_size = int(team_size)

    def display_info(self):
        return f"Hello {self.name}!!! you are managing the Team Size is {self.team_size} under {self.department} department "
    
class Developer(Employee):
    def __init__(self,name,emp_id, department,programming_language):
        super().__init__(name,emp_id, department) 
        self.programming_language = programming_language

    def display_info(self):
        return f"{self.name} Dude!!! Well knowledge in {self.programming_language} language."
    

if __name__  == "__main__":
    mgrObj = Manager('sakthi','E79731','IT',7)
    print(mgrObj.display_info())
    devObj = Developer("juju",'E71931','DEV',"c++")
    print(devObj.display_info())
