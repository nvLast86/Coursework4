class Vacancy:

    def __init__(self, title, area, url,description, salary):
        self.title = title
        self.area = area
        self.url = url
        self.description = description
        self.salary = salary

    def __repr__(self):
        return f'{self.title.title()} в городе {self.area.title()}.\nЗарплата: {self.salary}.\n{self.description}\n' \
               f'Ссылка на вакансию: {self.url}\n'


