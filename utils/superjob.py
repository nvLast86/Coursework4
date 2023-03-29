import requests
import os
import json
from engine import Engine
from utils.vacancy import Vacancy


class SuperJob(Engine):
    sj_key = os.getenv('SJ_API_KEY')
    sj_vacancies = []
    sj_url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, keyword):
        self.keyword = keyword
        self.vacancies = []

    def get_request(self):
        header = {'X-Api-App-Id': SuperJob.sj_key}
        for i in range(5):
            params = {'keyword': self.keyword, 'count': 100, 'page': i}
            response = requests.get(
                SuperJob.sj_url, headers=header, params=params).json()['objects']
            for vacancy in response:
                self.vacancies.append(Vacancy('SuperJob',
                                              vacancy['id'],
                                              vacancy['profession'],
                                              vacancy['payment_from'],
                                              vacancy['town']['title'],
                                              vacancy['candidat'],
                                              vacancy['link']))
        return self.vacancies

    # def to_json(self):
    #     vacancies_listtemp = []
    #     for vacancy in self.vacancies:
    #          vacancies_listtemp.append({'source': vacancy.source,
    #                                     'id': vacancy.id,
    #                                     'profession': vacancy.profession,
    #                                     'salary': vacancy.salary,
    #                                     'area': vacancy.area,
    #                                     'description': vacancy.description,
    #                                     'url': vacancy.url
    #                                     # 'publish_date': vacancy.date
    #                                     })
    #     return json.dumps(vacancies_listtemp)

if __name__ == '__main__':
    test = SuperJob('python')
    print({test.get_request())

