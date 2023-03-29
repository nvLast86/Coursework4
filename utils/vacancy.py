class Vacancy:

    def __init__(self, source, vacancy_id, profession, firm_name, area, payment, experience, url, date_published):
        self.source = source
        self.vacancy_id = vacancy_id
        self.profession = profession
        self.firm_name = firm_name
        self.area = area
        self.payment = payment
        self.experience = experience
        self.url = url
        self.date_published = date_published

    def __repr__(self):
        return f'{self.profession} в городе {self.area}.\nЗарплата: {self.salary}.\n{self.description}\n' \
               f'Ссылка на вакансию: {self.url}\n'


