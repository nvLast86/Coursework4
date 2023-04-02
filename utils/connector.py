from datetime import *
import json


class Connector:
    """
    Класс Connector предназначен для формирования общего ответа с двух сайтов
    на запрос пользователем вакансий по ключевому слову, а также формированию
    выборки на основе требований пользователя.
    """

    def __init__(self):
        self.__united_vacancies_list = []
        self.chosen_vacancies_list = []

    @property
    def united_vacancies_list(self):
        """
        Метод, задекорированный под функцию, т.к. аттрибут __united_vacancies_list приватный
        """
        return self.__united_vacancies_list

    @united_vacancies_list.setter
    def united_vacancies_list(self, value):
        """
        Прежде, чем аттрибут получит значение, происходит сортировка вакансий по дате
        размещения на сайте (от свежих к старым).
        """
        self.__united_vacancies_list = sorted(value, key=lambda x: x.date_published, reverse=True)

    @united_vacancies_list.getter
    def united_vacancies_list(self):
        return self.__united_vacancies_list

    @staticmethod
    def get_json(source_dict):
        """
        Статистический метод для вывода информации по вакансиям в виде JSON файла.
        Формируется список словарей, созданных на основе аттрибутов экземпляров класса Vacancy,
        после чего список конвертируется в JSON файл.
        """
        result = []
        for i in range(len(source_dict)):
            vacancy = {}
            vacancy['source'] = source_dict[i].source
            vacancy['id'] = source_dict[i].vacancy_id
            vacancy['profession'] = source_dict[i].profession
            vacancy['firm_name'] = source_dict[i].firm_name
            vacancy['area'] = source_dict[i].area
            vacancy['payment'] = source_dict[i].payment
            vacancy['experience'] = source_dict[i].experience
            vacancy['description'] = source_dict[i].description
            vacancy['url'] = source_dict[i].url
            vacancy['date_published'] = source_dict[i].date_published
            result.append(vacancy)
            x = json.dumps(result, ensure_ascii=False)
            with open(f'vacancies on {datetime.now().strftime("%Y-%m-%d %H-%M")}.txt', 'w',
                      encoding='utf-8') as outfile:
                json.dump(x, outfile, ensure_ascii=False)

    @staticmethod
    def print_vacancies_to_file(vacancy_list):
        """
        Статистический метод вывода списка вакансий в виде, удобном для чтения человеку.
        """
        with open(f'vacancies on {datetime.now().strftime("%Y-%m-%d %H-%M")}.txt', 'w', encoding='utf-8') as outfile:
            for i in range(len(vacancy_list)):
                outfile.write(f'{i+1}. {vacancy_list[i]}\n')

    def get_chosen_vacancies_list(self, user_answers):
        """
        Метод создания выборки на основе полученных условий от пользователя.
        От пользователя приходит список, содержаший информацию о том, начиная от какой суммы он хотел бы
        видеть зарплату, за сколько дней максимум от текущей даты могут быть вакансии, а также
        желаемое количество вакансий для отображения.
        """
        result = []
        for vacancy in self.__united_vacancies_list:
            if vacancy.payment[0] > user_answers[0]:
                result.append(vacancy)
            elif vacancy.payment[1] > user_answers[0]:
                result.append(vacancy)
        for vacancy in result:
            temp_list = vacancy.date_published.split('-')
            vacancy_date = datetime(int(temp_list[0]), int(temp_list[1]), int(temp_list[2][:2]))
            period = datetime.now() - vacancy_date
            if period.days >= user_answers[1]:
                del vacancy
        return result[0:user_answers[2]]
