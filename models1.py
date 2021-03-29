import datetime
import math


class Employee:
    def __init__(self, name, salary, days):
        self.name = name
        self.salary = salary
        self.days = days

    @property
    def __str__(self):
        return f"name class: Employee."
        return f"name: "
        return f"surname: "
        return f"days: "
    
    def work(self):
        return f"I come to the office."
 
    @staticmethod
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


class Candidate:
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

        