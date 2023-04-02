from utils.headhunter import HeadHunter
from utils.superjob import SuperJob
from datetime import *
import json


class Connector:

    def __init__(self):
        self.__united_vacancies_list = []
        self.chosen_vacancies_list = []

    @property
    def united_vacancies_list(self):
        return self.__united_vacancies_list

    @united_vacancies_list.setter
    def united_vacancies_list(self, value):
        self.__united_vacancies_list = sorted(value, key=lambda x: x.date_published, reverse=True)

    @united_vacancies_list.getter
    def united_vacancies_list(self):
        return self.__united_vacancies_list

    @staticmethod
    def get_json(source_dict):
        result =[]
        vacancy = {'source': '', 'id': '', 'profession': '', 'firm_name': '', 'area': '', 'payment': '',
                  'experience': '', 'description': '', 'url': '', 'date_published': ''}
        for item in source_dict:
            vacancy['source'] = item.source
            vacancy['id'] = item.vacancy_id
            vacancy['profession'] = item.profession
            vacancy['firm_name'] = item.firm_name
            vacancy['area'] = item.area
            vacancy['payment'] = item.payment
            vacancy['experience'] = item.experience
            vacancy['description'] = item.description
            vacancy['url'] = item.url
            vacancy['date_published'] = item.date_published
            result.append(vacancy)
        return json.dumps(result, ensure_ascii = False)

    @staticmethod
    def print_json_to_file(json_file):
        with open(f'vacancies on {datetime.now()}.txt', 'w', encoding='utf-8') as outfile:
            json.dump(json_file, outfile, ensure_ascii=False)

    @staticmethod
    def print_vacancies_to_file(vacancy_list):
        with open(f'vacancies on {datetime.now().strftime("%Y-%m-%d %H-%M")}.txt', 'w', encoding='utf-8') as outfile:
            for i in range(len(vacancy_list)):
                outfile.write(f'{i+1}. {vacancy_list[i]}\n')

    def get_chosen_vacancies_list(self, user_answers):
        result = []
        oldest_date = datetime.today() - timedelta(days=user_answers[1])
        for vacancy in self.__united_vacancies_list:
            if vacancy.payment[0] > user_answers[0]:
                result.append(vacancy)
            elif vacancy.payment[1] > user_answers[0]:
                result.append(vacancy)
        for vacancy in result:
            temp_list = vacancy.date_published.split('-')
            vacancy_date = datetime(int(temp_list[0]), int(temp_list[1]), int(temp_list[2][:2]))
            period = datetime.now() - vacancy_date
            if period.days >= user_answers[1]:
                del vacancy
        return result[0:user_answers[2]]
