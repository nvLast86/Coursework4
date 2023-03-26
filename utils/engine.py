from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file):
            """ return the instance of class Connector """
            pass