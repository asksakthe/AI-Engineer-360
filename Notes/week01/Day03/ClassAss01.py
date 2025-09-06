marks = [78, 85, 62, 90, 55, 88]

#print high and low marks
print(f"highest mark: {max(marks)} and lowest mark: {min(marks)}")

#average marks
print(f"average mark: {sum(marks)/len(marks)}")
Distinction_marks = []
for mark in marks:
    if mark > 75:
        Distinction_marks.append(mark)
print(f"Distinction mark: {mark}")

#Add a new mark 95 to the list

marks.append(95)
print(marks)


#using remove()
marks.remove(55)
print(f"removed Marks : {marks}")

#Sortig the marks
marks.sort()
print(f"sorted marks : {marks}")