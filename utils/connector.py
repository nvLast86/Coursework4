from utils.headhunter import HeadHunter
from utils.superjob import SuperJob


class Connector:

    def __init__(self):
        self.__united_vacancies_list = []

    @property
    def united_vacancies_list(self):
        return self.__united_vacancies_list

    @united_vacancies_list.setter
    def united_vacancies_list(self, value):
        self.__united_vacancies_list = value

    @united_vacancies_list.getter
    def united_vacancies_list(self):
        return self.__united_vacancies_list


if __name__ == '__main__':
    hh = HeadHunter('python')
    hh.get_vacancies_list(hh.get_request())
    sj = SuperJob('python')
    sj.get_vacancies_list(sj.get_request())
    connector = Connector()
    connector.united_vacancies_list = hh + sj
    print(connector.united_vacancies_list)
