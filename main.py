from utils.connector import Connector
from utils.headhunter import HeadHunter
from utils.superjob import SuperJob
from utils.vacancy import Vacancy

def main():
    print('Приветствую! Данный парсер собирает с сайтов HeadHunter и SuperJob 1000 вакансий (по 500 с каждого) по'
          'ключевому слову и формирует список, отсортированный по дате добавления на сайт.\n\n')
    user_keyword = input("Введите, что хотите найти:\n")
    hh = HeadHunter(user_keyword)
    sj = SuperJob(user_keyword)
    connector = Connector()
    connector.united_vacancies_list = [*hh.vacancies, *sj.vacancies]
    connector.print_vacancies_to_file(connector.united_vacancies_list)

main()

