from datetime import datetime
class Vacancy:

    def __init__(self, source, vacancy_id, profession, firm_name, area, payment, experience, description, url,
                 date_published):
        self.source = source
        self.vacancy_id = vacancy_id
        self.profession = profession
        self.firm_name = firm_name
        self.area = area
        self.payment = payment
        self.experience = experience
        self.description = description
        self.url = url
        self.date_published = date_published

    def __repr__(self):
        return f'{self.profession}.\nКомпания {self.firm_name}, город {self.area}.\n' \
               f'Опыт: {self.format_experience_answer()}. Зарплата: {self.format_payment_answer()}.\n' \
               f'{self.description}\n' \
               f'Ссылка на вакансию: {self.url}.\nДата публикации: {self.format_date()}\n'

    def format_payment_answer(self):
        if self.payment[0] > 0 and self.payment[1] > 0:
            pay_answer = f'от {self.payment[0]} до {self.payment[1]} {self.payment[2]}'
        elif self.payment[0] > 0 and self.payment[1] == 0:
            pay_answer = f'от {self.payment[0]} {self.payment[2]}'
        elif self.payment[0] == 0 and self.payment[1] > 0:
            pay_answer = f'до {self.payment[1]} {self.payment[2]}'
        else:
            pay_answer = 'не указана'
        return pay_answer

    def format_experience_answer(self):
        if self.experience == 0:
            exp_answer = 'не указан'
        else:
            exp_answer = self.experience
        return exp_answer

    def format_date(self):
        if self.source == 'SuperJob':
            date = datetime.fromtimestamp(self.date_published).strftime("%d.%m.%Y %X")
        else:
            date = datetime.fromisoformat(self.date_published).strftime("%d.%m.%Y %X")
        return date






