from datetime import datetime


class ServiceBot:

    # def __init__(self, vacancies_list):
    def __init__(self):
        self.vacancies_list = []
        self.questions = ['От какого размера зарплаты смотреть?\n', 'За сколько дней сделать выборку?\n',
                          'Сколькими вакансиями ограничить выборку?\n']
        self.user_answers = []
        self.is_positive_answer = False
        self.is_correct = False

    def __str__(self):
        if self.is_positive_answer:
            return f'Приветствую! Я специальный бот для работы с полученным списком.\n' \
                   f'Список большой, в нем {len(self.vacancies_list)} вакансий, могу сделать более ' \
                   f'точную выборку.\n'\
                   f'Если нажмешь (y), то я поработаю со списком.\n'
        else:
            return 'Хорошо, тогда просто выведу список вакансий в файл.\n'

    def poll_user(self):
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
        От пользователя приходит список, содержаший информацию о том, начиная от какой суммы он хотел бы
        видеть зарплату, за сколько дней максимум от текущей даты могут быть вакансии, а также
        желаемое количество вакансий для отображения.
        """
        result = []

        if user_answers[0] != 0:
            for vacancy in self.vacancies_list:
                if vacancy.payment[0] > user_answers[0]:
                    result.append(vacancy)
                elif vacancy.payment[1] > user_answers[0]:
                    result.append(vacancy)
        if self.have_vacancies(result) is False:
            return 'Увы, вакансий с такой зп нет.'

        if user_answers[1] != 0:
            for vacancy in result:
                temp_list = vacancy.date_published.split('-')
                vacancy_date = datetime(int(temp_list[0]), int(temp_list[1]), int(temp_list[2][:2]))
                period = datetime.now() - vacancy_date
                if period.days >= user_answers[1]:
                    del vacancy
        if self.have_vacancies(result) is False:
            return 'Увы, за такой временной промежуток вакансий не появлялось.'

        if user_answers[2] != 0 or len(result) < user_answers[2]:
            return result
        return result[0:user_answers[2]]

    @staticmethod
    def check_answer(answer):
        if answer.isdigit():
            return True
        return False

    @staticmethod
    def have_vacancies(check_list):
        if len(check_list) > 0:
            return True
        return False





