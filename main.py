from utils.connector import Connector
from utils.headhunter import HeadHunter
from utils.superjob import SuperJob
from utils.servicebot import ServiceBot

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
    print(f'Список по ключевому слову {user_keyword} создан.\n'
          f'Количество вакансий: {len(connector.united_vacancies_list)}\n')

    # Создаем бота для опроса пользователя и создании выборки на основе ответов
    bot = ServiceBot(connector.united_vacancies_list)
    print(bot)
    user_answer = input()
    if user_answer != 'y':
        bot.is_positive_answer = False
        print(bot)
    else:
        bot.poll_user()
        bot.get_chosen_vacancies_list(bot.user_answers)

        # Предлагаем распечатать результаты
        connector.chosen_vacancies_list = bot.chosen_vacancies
        user_answer = input('Распечатать полный список вакансий в файл?\n(y) - да, иной ввод - нет\n')
        if user_answer.lower() == 'y':
            connector.print_vacancies_to_file(connector.united_vacancies_list)
            connector.get_json(connector.united_vacancies_list)
        if bot.is_positive_answer:
            user_answer = input('Распечатать список вакансий на основе выборки в файл?\n(y) - да, иной ввод - нет\n')
            if user_answer.lower() == 'y':
                connector.print_vacancies_to_file(connector.chosen_vacancies_list)
                connector.get_json(connector.chosen_vacancies_list)

    print('Готово!')


if __name__ == '__main__':
    main()
