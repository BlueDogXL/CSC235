# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def start(self):
#         print(f"{self.make} {self.model} is starting!")

#     def getYear(self):
#         return self.year
#     def setYear(self, year):
#         self.year = year
    
# myCar = Car("Ford", "Explorer", 2005)
# myCar.start()
# myCar.setYear(2004)
# print(myCar.getYear())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def displayInfo(self):
#         print(f"Name: {self.name} \nAge: {self.age}")

# class Student(Person):
#     def __init__(self, name, age, studentID):
#         super().__init__(name, age)
#         self.studentID = studentID
#     def displayInfo(self):
#         super().displayInfo()
#         print(f"Student ID: {self.studentID}")

# myStudent = Student("Alex", 21, "AC20174383")
# myStudent.displayInfo()

class LibraryItem:
    def __init__(self, title):
        self.title = title

    def getItemDetails(self):
        print(f"Title: {self.title}")

class Book(LibraryItem):
    def __init__(self, title, pageCount):
        super().__init__(title)
        self.pageCount = pageCount

    def getItemDetails(self):
        super().getItemDetails()
        print(f"Page count: {self.pageCount}")

class Magazine(LibraryItem):
    def __init__(self, title, edition):
        super().__init__(title)
        self.edition = edition

    def getItemDetails(self):
        super().getItemDetails()
        print(f"Edition: {self.edition}")

class DVD(LibraryItem):
    def __init__(self, title, runtime):
        super().__init__(title)
        self.runtime = runtime

    def getItemDetails(self):
        super().getItemDetails()
        print(f"Runtime: {self.runtime}")

newBook = Book("Example Book", 300)
newBook.getItemDetails()