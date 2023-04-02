from utils.connector import Connector
from utils.headhunter import HeadHunter
from utils.superjob import SuperJob

user_decisions = []

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
    user_decision = input('Распечатать в файл?\n(y) - да, остальные нажатия - нет\n')
    if user_decision.lower() == 'y':
        connector.print_vacancies_to_file(connector.united_vacancies_list)
        print('Файл создан!\n')
    else:
        print('ok, пропустим\n')

    # Предлагаем создать отдельный файл с выборкой
    user_decision = input('Может, сформировать выборку?\n(y) - да, остальные нажатия - нет\n')
    if user_decision.lower() != 'y':
        print('ok, пропустим\n')
    else:
        user_decision = int(input('От какого размера зарплаты смотреть?\n'))
        user_decisions.append(int(user_decision))
        user_decision = int(input('За сколько дней сделать выборку?\n'))
        user_decisions.append(int(user_decision))
        user_decision = int(input('Сколькими вакансиями ограничить выборку?\n'))
        user_decisions.append(int(user_decision))
        chosen_result = connector.get_chosen_vacancies_list(user_decisions)
        user_decision = input('Информация сформирована! Распечатать в файл?\n(y) - да, остальные нажатия - нет\n')
        if user_decision.lower() == 'y':
            connector.print_vacancies_to_file(chosen_result)
        else:
            print("Результаты выборки:\n")
            print(chosen_result)


main()


