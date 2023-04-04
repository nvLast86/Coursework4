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

    @staticmethod
    def check_answer(answer):
        if answer.isdigit():
            return True
        return False




    # def make_deal_with_user(self, ):


if __name__ == '__main__':
    bot = ServiceBot()
    print(bot)
    bot.poll_user()
    print(bot.user_answers)





