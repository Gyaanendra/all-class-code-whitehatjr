
# creating a class
class Student(object):
    def __init__(self, name, age, gender, grade, marks=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade
        self.marks = marks or {}

    def setmark(self, subject, score):
        self.marks[subject] = score

    def getgrade(self, subject):
        return self.marks[subject]

    def getaverage(self):
        return sum(self.marks.values())/len(self.marks)


Student1 = Student("john", 21, "male", 6, {"maths": 90})
Student2 = Student("johnthan", 21, "male", 6, {"maths": 90})

print(Student1.getaverage())
print(Student2.getaverage())

# creating class2


class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating . .. ........")

    def change_gear(self, gear_type):
        print("gear changed")


Car1 = Car('audiA8', 'red', 'audi', 500)
print(Car1.accelerate())
