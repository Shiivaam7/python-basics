# class Student:
#     college_name = "abc college"  # Fixed typo: 'collage' -> 'college'

#     def __init__(self, name, marks):  # Corrected __init__ method
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome Student,", self.name)

#     def get_marks(self):
#         return self.marks


# s1 = Student("Karan", 97)
# s1.welcome()
# print(s1.get_marks())


#create student class that takes name & marks of 3 subject as argument in constructor.then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self .marks:
            sum += val
        print("hi",self.name,"your avg score is:",sum/3) 
s1 = Student("tony starck",[99,97,95])
s1.get_avg()
    