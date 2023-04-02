from utils.connector import Connector
from utils.headhunter import HeadHunter
from utils.superjob import SuperJob


def main():
    # Объясняем для чего данная программа. Далее запрашиваем ключевое слово и производим парсинг
    print('Приветствую!\nДанный парсер собирает с сайтов HeadHunter и SuperJob 1000 вакансий (по 500 с каждого)\n'
          'по ключевому слову и формирует список вакансий, отсортированный по дате добавления на сайт.\n')
    user_keyword = input("Введите, что хотите найти:\n")
    hh = HeadHunter(user_keyword)
    sj = SuperJob(user_keyword)
    connector = Connector()
    connector.united_vacancies_list = [*hh.vacancies, *sj.vacancies]
    print(f'Список по ключевому слову {user_keyword} создан')

    # Создаем текстовый файл со всеми вакансиями по желанию пользователя
    user_decision = input('Распечатать в файл? (y) - да, остальные нажатия - нет')
    if user_decision.lower() == 'y':
        connector.print_vacancies_to_file(connector.united_vacancies_list)
        print('Файл создан!\n')
    else:
        print('ok, пропустим\n')

    # Предлагаем создать отдельный файл с топовыми вакансиями
    print('Может, сформировать топ вакансий по зарплате? (y) - да')





main()

