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

    @staticmethod
    def get_dict(source_dict):
        result =[]
        vacancy = {'source': '', 'id': '', 'profession': '', 'firm_name': '', 'area': '', 'payment': '',
                  'experience': '', 'description': '', 'url': '', 'date_published': ''}
        for item in source_dict:
            vacancy['source'] = item.source
            vacancy['id'] = item.vacancy_id
            vacancy['profession'] = item.profession
            vacancy['firm_name'] = item.firm_name
            vacancy['area'] = item.area
            vacancy['payment'] = item.payment
            vacancy['experience'] = item.experience
            vacancy['description'] = item.description
            vacancy['url'] = item.url
            vacancy['date_published'] = item.date_published
            result.append(vacancy)
        return result
    @staticmethod
    def get_json(source_list):
        return json.dumps(source_list, ensure_ascii = False)

    @staticmethod
    def print_to_file(json_file):
        with open(f'vacancies on {datetime.now().date()}.txt', 'w', encoding='utf-8') as outfile:
            json.dump(json_file, outfile, ensure_ascii=False)




if __name__ == '__main__':
    hh = HeadHunter('python')
    hh.get_vacancies_list(hh.get_request())
    sj = SuperJob('python')
    sj.get_vacancies_list(sj.get_request())
    connector = Connector()
    connector.united_vacancies_list = hh + sj
    print(connector.united_vacancies_list)
