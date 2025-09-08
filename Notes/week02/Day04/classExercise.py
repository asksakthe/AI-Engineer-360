class Person():

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def greet(self):
        print(f"Good Evening {self.name}!!! \n  your ID is {self.ID}")



E1 = Person("Sakthi", 10443)
E2 = Person("karthi", 10446)

E1.greet()
E2.greet()