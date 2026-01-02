#ASSIGNMENT5

#TASK1: Create a Dictionary of Student Marks

student_marks = {'Abhi' : 92 , 'Harshad' : 89 , 'Renuka' : 79 , 'Sam' : 98 , 'Preet' : 85}
name = input("Enter the student's name: ")
if name in student_marks:
    print(f"{name}'s marks: {student_marks.get(name)}")
else:
    print("Student not found")


#TASK2 : Demonstrate List Slicing
og_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = list(og_list[:5])
rev = list(og_list[:5][::-1])
print("Original List: ",og_list)
print("Extracted first five elements: ",first_five)
print("Reversed extracted elements: ",rev)