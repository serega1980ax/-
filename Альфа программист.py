import datetime
import math


class Employee:
    def __init__(self, name, salary, days):
        self.name = name
        self.salary = salary
        self.days = days

    def work(self):
        return f"I come to the office."
 
    def check_salary(self):
        def zp(salary):
            first_data = datetime.date.today() - datetime.timedelta(days=datetime.date.today().day)
            data_now = datetime.date.today()
            delta = datetime.timedelta(1)

            days = 0
            while first_data != data_now:
                if data_now.isoweekday() not in (6, 7):
                    days += 1
                    data_now -= delta
                return salary * days

        zp_now = zp(self.salary)
        zp_month = Employee.zp_month_calc(self)
        return f"{zp_month}, {zp_now}"

    def zp_month_calc(self):
        return self.salary * self.days
                
    def gt(self, other):
        return self.zp_month_calc() > other.zp_month_calc()

    def ge(self, other):
        return self.zp_month_calc() >= other.zp_month_calc()
    
    def lt(self, other):
        return self.zp_month_calc() < other.zp_month_calc()

    def le(self, other):
        return self.zp_month_calc() <= other.zp_month_calc()

    def eq(self, other):
        return self.zp_month_calc() == other.zp_month_calc()

    def ne(self, other):
        return self.zp_month_calc() != other.zp_month_calc()

    
class Recruiter(Employee):
    def __init__(self, name, salary, days):
        super().__init__(name, salary, days)
    
    def work(self):
        return f"I come to the office and start to hiring."

    def __str__(self):
        return f"{self.__class__.__name__}:{self.name}"


class Programmer(Employee):
    def __init__(self, name, salary, days, tech_stack):
        super().__init__(name, salary, days)
        self.tech_stack = tech_stack
        
    def work(self):
        return f"I come to the office and start to coding."
    
    def __str__(self):
        return f"{self.__class__.__name__}:{self.name}"

    def gt(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def ge(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def lt(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def le(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def eq(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def ne(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def add(self, other):
        tech_stack = self.tech_stack | other.tech_stack
        name = self.name + other.name
        salary = self.salary + other.salary
        day = math.ceil((self.days + other.days) / 2)
        return Programmer(name, salary, day, tech_stack)


a = Recruiter("Vasya", 500, 24)
print(a)
print(a.work())
print(a.check_salary())
print()

b = Programmer("Tolya", 800, 24, {'JS', 'Java', 'PHP', 'Python'})
print(b)
print(b.work())
print(b.check_salary())
print(b.tech_stack)
print()
print(a == b)
print()

c = Programmer("Yuriy", 600, 24, {'PHP', 'Python'})
print(c)
print(c.work())
print(c.check_salary())
print(c.tech_stack)
print()
print(b == c)
print()

d = b + c
print(d)
print(d.work())
print(d.check_salary())
print(d.tech_stack)
print()

