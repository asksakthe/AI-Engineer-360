"""This Class is to find the age of the book based on publication year"""
import datetime
#Book Class
class Book:
    # Constructor to initialize Book Attributes
    def __init__(self,title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    #mothod to calculate age of the book based on current year  
    def get_age(self):
        current_year = datetime.datetime.now().year
        age_is = current_year - self.publication_year
        return f"the Age of {self.title} Book is {age_is}"
        
    
#create object of Book Class    
book_obj_01 = Book('aws', 'todd J', 2018)
print(book_obj_01.get_age()) 
        
	