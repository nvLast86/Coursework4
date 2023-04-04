from datetime import *
import json


class Connector:
    """
    Класс Connector предназначен для формирования общего ответа с двух сайтов
    на запрос пользователем вакансий по ключевому слову, а также печать в удобном для чтения
    пользователем файла .txt и в виде JSON файла.
    """

    def __init__(self):
        self.__united_vacancies_list = []
        self.__chosen_vacancies_list = []

    @property
    def united_vacancies_list(self):
        """
        Метод, задекорированный под функцию, т.к. аттрибут __united_vacancies_list приватный
        """
        return self.__united_vacancies_list

    @united_vacancies_list.setter
    def united_vacancies_list(self, value):
        """
        Прежде, чем аттрибут получит значение, происходит сортировка вакансий по дате
        размещения на сайте (от свежих к старым).
        """
        self.__united_vacancies_list = sorted(value, key=lambda x: x.date_published, reverse=True)

    @united_vacancies_list.getter
    def united_vacancies_list(self):
        return self.__united_vacancies_list

    @property
    def chosen_vacancies_list(self):
        """
        Метод, задекорированный под функцию, т.к. аттрибут __chosen_vacancies_list приватный
        """
        return self.__chosen_vacancies_list

    @chosen_vacancies_list.getter
    def chosen_vacancies_list(self):
        return self.__chosen_vacancies_list

    @chosen_vacancies_list.setter
    def chosen_vacancies_list(self, value):
        self.__chosen_vacancies_list = value

    def get_json(self, source):
        """
        Метод для вывода информации по вакансиям в виде JSON файла.
        Формируется список словарей, созданных на основе аттрибутов экземпляров класса Vacancy,
        после чего список конвертируется в JSON файл.
        """
        result = []
        current_date = datetime.now().strftime("%Y-%m-%d %H-%M")
        for i in range(len(source)):
            vacancy = {}
            vacancy['source'] = source[i].source
            vacancy['id'] = source[i].vacancy_id
            vacancy['profession'] = source[i].profession
            vacancy['firm_name'] = source[i].firm_name
            vacancy['area'] = source[i].area
            vacancy['payment'] = source[i].payment
            vacancy['experience'] = source[i].experience
            vacancy['description'] = source[i].description
            vacancy['url'] = source[i].url
            vacancy['date_published'] = source[i].date_published
            result.append(vacancy)
            x = json.dumps(result, ensure_ascii=False)
            if source is self.__united_vacancies_list:
                with open(f'vacancies json on {current_date}.txt', 'w', encoding='utf-8') as outfile:
                    json.dump(x, outfile, ensure_ascii=False)
            else:
                with open(f'sorted vacancies json on {current_date}.txt', 'w', encoding='utf-8') as outfile:
                    json.dump(x, outfile, ensure_ascii=False)

    def print_vacancies_to_file(self, vacancy_list):
        """
        Метод вывода списка вакансий в виде, удобном для чтения человеку.
        """
        current_date = datetime.now().strftime("%Y-%m-%d %H-%M")
        if vacancy_list is self.__united_vacancies_list:
            with open(f'vacancies on {current_date}.txt', 'w', encoding='utf-8') as outfile:
                for i in range(len(vacancy_list)):
                    outfile.write(f'{i+1}. {vacancy_list[i]}\n')
        else:
            with open(f'sorted vacancies on {current_date}.txt', 'w', encoding='utf-8') as outfile:
                for i in range(len(vacancy_list)):
                    outfile.write(f'{i+1}. {vacancy_list[i]}\n')

