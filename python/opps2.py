# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no= acc_no
#         self.acc_pass = acc_pass
        
# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.acc_pass)

# class Car:
#     @staticmethod
#     def start():
#         print("car started...")
    
#     @staticmethod
#     def stop():
#         print("car stopped")

# class Toyotacar(Car):
#     def __init__(self, name):
#         self.name = name
        
# car1 = Toyotacar("fortuner")
# car2 = Toyotacar("prius")

# print(car1.start())

# class Person:
#     name = "anonymous"
    
#     def changeName(self, name):
#         self.__class__.name = "rahul"
        
# p1 = Person()
# p1.changename("rahul kumar")
# print(p1.name)
# print(Person.name)

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def shownumber(self):
#         print(f"{self.real}i + {self.img}j")
        
#     def __add__(self, num2):
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return Complex(newreal, newimg) 


# num1 = Complex(1, 3)
# num1.shownumber()

# num2 = Complex(4, 6)
# num2.shownumber()

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         return(22/7) * self.radius ** 2
        
#     def perimeter(self):
#         return 2*(22/7) * self.radius
# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showdetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "it", "75,000")
engg1 = Engineer("eloun mask", 40)
engg1.showdetails()