import requests
import os
import json
from engine import Engine
from utils.vacancy import Vacancy


class SuperJob(Engine):
    key = os.getenv('SJ_API_KEY')
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, keyword):
        self.keyword = keyword
        self.vacancies = []
        self.get_vacancies()

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
                                              [vacancy['payment_from'], vacancy['payment_to'], vacancy['currency']],
                                              vacancy['experience']['title'],
                                              self.get_description(vacancy),
                                              vacancy['link'],
                                              vacancy['date_published']))
        return self.vacancies

    @staticmethod
    def get_description(response):
        description = []
        temp = response['candidat'].split('.')
        for i in range(2):
            description.append(temp[i])
        return '. '.join(description)

    #


if __name__ == '__main__':
    test = SuperJob('python')
    x = test.get_request()
    print(test.get_vacancies_list(x))

    print(len(test.get_request()))
    # print(test.to_json())


