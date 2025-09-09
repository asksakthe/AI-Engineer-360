import HA02_StudentInfo as stu

stud_obj_01 = stu.Student('Sakthi', 'A', 'ECE')
print(stud_obj_01.print_info())
print(stud_obj_01.update_grade('A+'))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

stud_obj_02 = stu.Student('Karthi', 'B', 'CSE')
print(stud_obj_02.print_info())
print(stud_obj_02.update_grade('A'))
