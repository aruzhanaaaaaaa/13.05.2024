# class Car:
#     def __init__(self, marc, subname, age):
#         self.marc = marc
#         self.subname = subname
#         self.age = age

#     def my(self):
#         print("Марка " + self.marc, self.subname, self.age)

# p1 = Car("Tayota", "Camry", 2024)
# p1.my()



# # class Person:
# #     def __init__(self, name):
# #         self.name = name
# #     def get_info (self):
# #         print("Аты:",self.name)

# # class Employee (Person):
# #        def job(self,job_name):
# #           print("Аты:",self.name,"жұмыс:",job_name)



# #class Person:
#     #def __init__(self,name):
#    #     self.name = name
#  #  def get_info(self):
#  #       print("Аты:",self.name)

# #class Employee(Person):
#    # def job(self,job_name):
#   #      print("Аты:",self.name,"жұмысы:",job_name)

# #p1 = Person("Aruzhan")
# #1.get_info()



# #employee_obj:Employee("Aruzhan")
# #employee_obj.job("Programmer")


# class Person:
#     def __init__(self, name):
#         self.name = name
#     def get_info(self):
#         print("Аты:",self.name)

# class Employee(Person):
#     def job(self,job_name):
#         print("Аты:",self.name,"жұмысы:",job_name)

# employe_obj = Employee("Aruzhan")
# employe_obj.job("programmer")


# class Figure:
#     def __init__(self, name):
#         self.name = name
    
#     def display_info(self):
#         print("This is a figure named:", self.name)

# my_figure = Figure("Square")
# my_figure.display_info()


# class Figura:
#     def __init__(self,p):
#         self.p = p
#     def get_info(self):
#         print("Периметр", p)


# class  Triangle (Figura):
#     def perimetr(self, figura_name):
#         print("Периметр", self.p, "Фигура",figura_name)


# figure_obj= Figura()
# figure_obj.perimetr("triangle")


class Figura:
    def __init__(self, p):
        self.p = p
    
    def get_info(self):
        print("Периметр:", self.p)

class Triangle(Figura):
    def __init__(self, a, b, c):
        Figura.__init__(self, a + b + c)

triangle_obj = Triangle(10, 20, 30)
triangle_obj.get_info()



class Color:
    def __init__(self, color):
        self.color = color
    
    def get_info(self):
        print("Цвет:", self.color)

class Triangle(Color):
    def __init__(self, color):
        Color.__init__(self, color)

triangle_obj = Triangle("красный")
triangle_obj.get_info()