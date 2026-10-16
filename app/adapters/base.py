from abc import ABC, abstractmethod


class PMSAdapter(ABC):

    @abstractmethod
    def get_data(self, resource: str):
        pass
