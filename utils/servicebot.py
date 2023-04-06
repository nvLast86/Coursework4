from datetime import datetime


class ServiceBot:
    """
    Класс ServiceBot предназначен для взаимодействия с пользователем для создания выборки из списка найденных
    вакансий на сайтах согласно заданным пользователем критериям по зарплате, дате публикации вакансии и
    отображения топа вакансий.
    """

    def __init__(self, vacancies_list):
        self.vacancies_list = vacancies_list
        self.questions = ['От какого размера зарплаты смотреть?\n', 'За сколько дней сделать выборку?\n',
                          'Сколькими вакансиями ограничить выборку?\n']
        self.user_answers = []
        self.is_positive_answer = True
        self.is_correct = False
        self.chosen_vacancies = []

    def __str__(self):
        """
        Экземпляр приветствует пользователя, объясняет, для чего он.
        Если пользователь не желает делать выборку, то бот ничего не делает.
        """
        if self.is_positive_answer:
            return f'Приветствую! Я специальный бот для работы с полученным списком.\n' \
                   f'Список большой, в нем {len(self.vacancies_list)} вакансий, могу сделать более ' \
                   f'точную выборку.\n'\
                   f'Если нажмешь (y), то я поработаю со списком.'
        else:
            return 'Хорошо, ничего не делаю.\n'

    def poll_user(self):
        """
        Опрос пользователя по критериям, задав ряд вопросов, хранящиеся в поле "questions".
        Если пользователь вводит не корректные данные, "бот" объяснит, в каком виде он ожидает ввод,
        и будет требовать до бесконечности корректный ввод. Результаты будут переданы в поле "бота"
        "user_answers" в виде списка.
        """
        print('Хорошо! Предварительно задам несколько вопросов для создания выборки.')
        for question in self.questions:
            while True:
                user_decision = input(question)
                self.is_correct = self.check_answer(user_decision)
                if self.is_correct:
                    self.user_answers.append(int(user_decision))
                    self.is_correct = False
                    break
                else:
                    print('Некорректное значение! Введите целое число, либо 0, чтобы пропустить данный вопрос.')

    def get_chosen_vacancies_list(self, user_answers):
        """
        Метод создания выборки на основе полученных условий от пользователя.
        От пользователя приходит список, содержащий информацию о том, начиная от какой суммы он хотел бы
        видеть зарплату, за сколько дней максимум от текущей даты могут быть вакансии, а также
        желаемое количество вакансий для отображения.
        """
        # Проверяем по критерию ожидаемой зарплаты. Если пользователь ввел 0, то пропускаем проверку.
        # Если ни одна вакансия не подходит, то функция завершает свое действие с уведомлением об
        # отсутствии подходящих вакансий.
        if user_answers[0] != 0:
            for vacancy in self.vacancies_list:
                if vacancy.payment[0] > user_answers[0]:
                    self.chosen_vacancies.append(vacancy)
                elif vacancy.payment[1] > user_answers[0]:
                    self.chosen_vacancies.append(vacancy)
        if self.have_vacancies(self.chosen_vacancies) is False:
            return 'Увы, вакансий с такой зп нет.'

        # Проверяем по критерию даты публикации. Если пользователь ввел 0, то пропускаем проверку.
        # Если ни одна вакансия не была в ожидаемый период опубликована, то функция завершает свое действие
        # с уведомлением об этом.
        if user_answers[1] != 0:
            for vacancy in self.chosen_vacancies:
                temp_list = vacancy.date_published.split('-')
                vacancy_date = datetime(int(temp_list[0]), int(temp_list[1]), int(temp_list[2][:2]))
                period = datetime.now() - vacancy_date
                if period.days >= user_answers[1]:
                    del vacancy
        if self.have_vacancies(self.chosen_vacancies) is False:
            return 'Увы, за такой временной промежуток вакансий не появлялось.'

        # Выдаем желаемое количество вакансий. Если вакансий меньше, чем желаемый топ, то выдаем все, что есть.
        if user_answers[2] == 0 or len(self.chosen_vacancies) < user_answers[2]:
            return self.chosen_vacancies
        return self.chosen_vacancies[0:user_answers[2]]

    @staticmethod
    def check_answer(answer):
        """
        Статистический метод проверки правильности ввода ответа пользователем.
        Если ответ состоит только из чисел, то ввод корректный.
        """
        if answer.isdigit():
            return True
        return False

    @staticmethod
    def have_vacancies(check_list):
        """
        Статистический метод проверки наличия вакансий в списке.
        """
        if len(check_list) > 0:
            return True
        return False
