class ServiceBot:

    # def __init__(self, vacancies_list):
    def __init__(self):
        self.vacancies_list = ''
        self.questions = ['От какого размера зарплаты смотреть?\n', 'За сколько дней сделать выборку?\n',
                          'Сколькими вакансиями ограничить выборку?\n']
        self.user_answers = []
        self.is_positive_answer = True
        self.is_correct = False

    def __repr__(self):
        return 'Приветствую! Я специальный бот для работы с полученным списком.'

    def speak_to_user(self):
        print('Задам несколько вопросов для создания выборки.')
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
    bot.speak_to_user()
    print(bot.user_answers)





