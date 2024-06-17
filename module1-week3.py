# Exercise 1
import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        c = torch.max(x)
        exp_x = torch.exp(x - c)
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
# print(output)

softmax_stable = SoftmaxStable()
output_stable = softmax_stable(data)
# print(output_stable)


# Exercise 2
class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(
            f'Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}')


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(
            f'Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}')


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(
            f'Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}')


class Ward:
    def __init__(self, name):
        self.name = name
        self.member = []

    def add_person(self, person):
        self.member.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.member:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.member:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.member.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        sum_age = 0
        num_teacher = 0
        for person in self.member:
            if isinstance(person, Teacher):
                sum_age += person.yob
                num_teacher += 1
        return sum_age / num_teacher


# 2(a)
student1 = Student(name="studentA", yob=2010, grade="7")
# student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
# teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
# doctor1.describe()


# 2(b)
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2(c)
print(f"\nNumber of doctors : {ward1.count_doctor()}")

# 2(d)
print('\nAfter sorting Age of Ward1 people')
ward1.sort_age()
ward1.describe()

# 2(e)
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")


# Exercise 3
class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_val = []

    def is_empty(self):
        return True if len(self.num_val) == 0 else False

    def is_full(self):
        return True if len(self.num_val) == self.capacity else False

    def pop(self):
        last_val = self.num_val.pop()
        return last_val

    def push(self, value):
        self.num_val.append(value)

    def top(self):
        return self.num_val[-1]


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
print()

# Exercise 4


class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_val = []

    def is_empty(self):
        return True if len(self.num_val) == 0 else False

    def is_full(self):
        return True if len(self.num_val) == self.capacity else False

    def dequeue(self):
        first_val = self.num_val.pop(0)
        return first_val

    def enqueue(self, value):
        self.num_val.append(value)

    def front(self):
        return self.num_val[0]


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())


# Multiple choice

# Question 1
data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
# print(output)


# Question 2
data = torch . Tensor([5, 2, 4])
my_softmax = Softmax()
output = my_softmax(data)
# print(output)


# Question 3
data = torch . Tensor([1, 2, 300000000])
my_softmax = Softmax()
output = my_softmax(data)
# print(output)


# Question 4
data = torch . Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
# print(output)


# Question 5
student1 = Student(name="studentZ2023", yob=2011, grade="6")
assert student1.yob == 2011
# student1.describe()


# Question 6
teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
assert teacher1.yob == 1991
# teacher1.describe()


# Question 7
doctor1 = Doctor(name="doctorZ2023", yob=1981, specialist="Endocrinologists")
assert doctor1.yob == 1981
# doctor1.describe()


# Question 8
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
# print(ward1.count_doctor())


# Question 9
stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
# print(stack1.is_full())


# Question 10
stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
# print(stack1.top())


# Question 11
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
# print(queue1.is_full())


# Question 12
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
# print(queue1.front())
