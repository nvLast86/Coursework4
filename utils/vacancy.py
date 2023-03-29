class Vacancy:

    def __init__(self, source, id, profession, salary, area, description, url):
        self.source = source
        self.id = id
        self.profession = profession
        self.salary = salary
        self.area = area
        self.description = description
        self.url = url

    def __repr__(self):
        return f'{self.profession} в городе {self.area}.\nЗарплата: {self.salary}.\n{self.description}\n' \
               f'Ссылка на вакансию: {self.url}\n'


