from abc import ABC, abstractmethod


class Engine(ABC):
    """
    Абстрактный класс, от которого наследуют классы HeadHunter и SuperJob
    """

    @abstractmethod
    def get_vacancies(self):
        pass
