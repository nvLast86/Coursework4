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
                                              vacancy['firm_name'],
                                              vacancy['town']['title'],
                                              [vacancy['payment_from'], vacancy['payment_to'], vacancy['currency']],
                                              vacancy['experience']['title'],
                                              vacancy['link'],
                                              vacancy['date_published']))
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
    print(test.get_request())
    print(len(test.get_request()))
    # print(test.to_json())


