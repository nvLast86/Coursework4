import requests
import os
from utils.engine import Engine
from utils.vacancy import Vacancy
from datetime import datetime


class SuperJob(Engine):
    key = os.getenv('SJ_API_KEY')
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, keyword):
        self.keyword = keyword
        self.vacancies = []
        self.get_vacancies()

    def __repr__(self):
        return f'Результат парсинга по сайту SuperJob.ru по ключевому слову {self.keyword}\n' \
               f'Количество вакансий: {len(self.vacancies)}'

    def get_vacancies(self):
        header = {'X-Api-App-Id': SuperJob.key}
        for i in range(5):
            params = {'keyword': self.keyword, 'count': 100, 'page': i}
            response = requests.get(SuperJob.url, headers=header, params=params).json()['objects']
            for vacancy in response:
                self.vacancies.append(Vacancy('SuperJob',
                                              vacancy['id'],
                                              vacancy['profession'],
                                              vacancy['firm_name'],
                                              vacancy['town']['title'],
                                              [int(vacancy['payment_from']), int(vacancy['payment_to']), vacancy['currency']],
                                              vacancy['experience']['title'],
                                              vacancy['candidat'],
                                              vacancy['link'],
                                              self.format_date(vacancy['date_published'])))
        return self.vacancies

    @staticmethod
    def format_date(value):
        date = datetime.fromtimestamp(value).strftime("%Y-%m-%d %X")
        return date

