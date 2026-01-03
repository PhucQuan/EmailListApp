from datetime import date

# ----- Lớp cha -----
class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        return f"Name: {self.name}, Year of Birth: {self.yob}"


# ----- Lớp con -----
class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f"Student - {super().describe()}, Grade: {self.grade}"


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f"Teacher - {super().describe()}, Subject: {self.subject}"


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"Doctor - {super().describe()}, Specialist: {self.specialist}"


# ----- Ward -----
class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def addPerson(self, person):
        self.people.append(person)

    def describe(self):
        print(f"--- Ward: {self.name} ---")
        for p in self.people:
            print(p.describe())

    def countDoctor(self):
        return sum(isinstance(p, Doctor) for p in self.people)

    def sortAge(self):
        self.people.sort(key=lambda p: p.yob)  # nhỏ yob => lớn tuổi
        # Nếu muốn tuổi tăng dần: sắp theo (2025 - yob)

    def aveTeacherYearOfBirth(self):
        teachers = [p.yob for p in self.people if isinstance(p, Teacher)]
        return sum(teachers) / len(teachers) if teachers else None


# ----- Demo -----
ward = Ward("Central Ward")
ward.addPerson(Student("An", 2005, "12A1"))
ward.addPerson(Teacher("Bình", 1980, "Math"))
ward.addPerson(Teacher("Cường", 1975, "Physics"))
ward.addPerson(Doctor("Dung", 1988, "Cardiology"))
ward.addPerson(Doctor("Hà", 1990, "Neurology"))

ward.describe()
print("Số Doctor:", ward.countDoctor())
ward.sortAge()
print("\nSau khi sort theo tuổi:")
ward.describe()
print("Trung bình năm sinh Teacher:", ward.aveTeacherYearOfBirth())



#bai2 

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.capacity

    def push(self, value):
        if self.isFull():
            print("Error: Stack is full")
        else:
            self.items.append(value)

    def pop(self):
        if self.isEmpty():
            print("Error: Stack is empty")
        else:
            return self.items.pop()

    def top(self):
        if self.isEmpty():
            return None
        return self.items[-1]
#bai3 
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.capacity

    def enqueue(self, value):
        if self.isFull():
            print("Error: Queue is full")
        else:
            self.items.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("Error: Queue is empty")
        else:
            return self.items.pop(0)

    def front(self):
        if self.isEmpty():
            return None
        return self.items[0]


#bai 4

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


# Demo
points = [Point(1, 2), Point(3, 4), Point(-1, 5)]
result = Point(0, 0)
for p in points:
    result = result + p

print("Tổng các points:", result)



#bai5
import datetime

class Employee:
    count = 0

    def __init__(self, emp_id, name, dob, phone, department, base_salary, emp_type):
        self.emp_id = emp_id
        self.name = name
        self.dob = dob  # datetime.date
        self.phone = phone
        self.department = department
        self.base_salary = base_salary
        self.emp_type = emp_type
        Employee.count += 1

    def compute_salary(self):
        return self.base_salary

    def show_info(self):
        return (f"ID: {self.emp_id}, Name: {self.name}, DOB: {self.dob}, "
                f"Phone: {self.phone}, Dept: {self.department}, Salary: {self.compute_salary()}")

    def update_department(self, new_dept):
        self.department = new_dept


class Manager(Employee):
    def __init__(self, emp_id, name, dob, phone, department, base_salary, bonus):
        super().__init__(emp_id, name, dob, phone, department, base_salary, 0)
        self.bonus = bonus

    def compute_salary(self):
        return self.base_salary + self.bonus


class Developer(Employee):
    def __init__(self, emp_id, name, dob, phone, department, base_salary, overtime_hours):
        super().__init__(emp_id, name, dob, phone, department, base_salary, 1)
        self.overtime_hours = overtime_hours

    def compute_salary(self):
        return self.base_salary + self.overtime_hours * 200000  # giả sử 200k/h OT


class Tester(Employee):
    def __init__(self, emp_id, name, dob, phone, department, base_salary, allowance):
        super().__init__(emp_id, name, dob, phone, department, base_salary, 2)
        self.allowance = allowance

    def compute_salary(self):
        return self.base_salary + self.allowance


# Demo
staffs = [
    Manager("M01", "Lan", datetime.date(1980, 5, 12), "0901", "HR", 15000000, 5000000),
    Developer("D01", "Nam", datetime.date(1990, 7, 1), "0902", "IT", 12000000, 10),
    Tester("T01", "Hùng", datetime.date(1995, 2, 20), "0903", "QA", 10000000, 2000000)
]

for emp in staffs:
    print(emp.show_info())

print("Tổng nhân viên:", Employee.count)
