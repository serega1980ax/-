from models1 import Employee, Recruiter, Programmer, Candidate, Vacancy


if __name__ == '__main__':

    vasya = Recruiter('Vasya', 500, 24)
    print(vasya)
    tolya = Programmer('Tolya', 800, 24, {'JS', 'Java', 'PHP', 'Python'})
    print(tolya)
    yuriy = Programmer('Yuriy', 600, 24, {'PHP', 'Python'})
    print(yuriy)
    alex = Candidate(full_name='Alex', email='AlexBoom@gmail.com', technologies='Python', main_skill='junior', main_skill_grade='middle')
    print(alex)
    vovan = Candidate(full_name='Vovan', email='VovanTrue@gmail.com', technologies='JS', main_skill='junior', main_skill_grade='middle')
    print(vovan)
    ruslan = Candidate(full_name='Ruslan', email='Ruslan12@gmail.com', technologies='PHP', main_skill='middle', main_skill_grade='senior')
    print(ruslan)
    valera = Vacancy(title='PHP', main_skill='PHP', main_skill_level='junior')
    print(valera)
    timur = Vacancy(title='JS', main_skill='JS', main_skill_level='middle')
    print(timur)


