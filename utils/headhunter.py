import json
import requests
from vacancy import Vacancy
from datetime import datetime
from engine import Engine

class HeadHunter(Engine):
    url = 'https://api.hh.ru/vacancies'

    def __init__(self, keyword):
        self.keyword = keyword
        self.vacancies = []


    def get_request(self):
        response_full = []
        for i in range(5):
            params = {'text': self.keyword, 'area': 113, 'page': i, 'per_page': 100}
            response = requests.get(HeadHunter.url, params=params).json()['items']
            response_full += response
            self.correct_vacancies(response_full)
        return response_full

    def get_vacancies_list(self, response):
        for vacancy in response:
            self.vacancies.append(Vacancy('HeadHunter',
                                          vacancy['id'],
                                          vacancy['name'],
                                          vacancy['employer']['name'],
                                          vacancy['area']['name'],
                                          [vacancy['salary']['from'], vacancy['salary']['to'],
                                          vacancy['salary']['currency']],
                                          vacancy['experience'] if 'experience' in vacancy.keys() else 'не указан',
                                          'отсутствует' if vacancy.get('snippet').get('responsibility') is None else
                                          vacancy.get('snippet').get('responsibility'),
                                          vacancy['alternate_url'],
                                          vacancy['published_at']))
        return self.vacancies

    def __add__(self, other):
        return self.vacancies + other.vacancies

    @staticmethod
    def correct_vacancies(response):
        for item in response:
            if item['salary'] is None:
                item['salary'] = {'from': 0, 'to': 0, 'currency': ''}
            if 'from' not in item['salary'].keys():
                item['salary']['from'] = 0
            if 'to' not in item['salary'].keys():
                item['salary']['to'] = 0
            if item['salary']['from'] is None:
                item['salary']['from'] = 0
            if item['salary']['to'] is None:
               item['salary']['to'] = 0

if __name__ == '__main__':
    test = HeadHunter('python')
    x = test.get_request()
    test.correct_vacancies(x)
    test.get_vacancies_list(x)
    print(test.vacancies)
    print(len(test.vacancies))
    # print(test.correct_vacancies(x))
