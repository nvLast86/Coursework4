from headhunter import HeadHunter
from superjob import SuperJob


class Connector:

    def __init__(self):
        self.__united_vacancies_list = []

    @property
    def united_vacancies_list(self):
        return self.__united_vacancies_list

    @united_vacancies_list.setter
    def united_vacancies_list(self, object1, object2):
        self.__united_vacancies_list = object1 + object2

    @united_vacancies_list.getter
    def united_vacancies_list(self):
        return self.__united_vacancies_list

if __name__ == '__main__':
    hh = HeadHunter('python')
    sj = SuperJob('python')
    connector = Connector()
    connector.united_vacancies_list(hh, sj)
