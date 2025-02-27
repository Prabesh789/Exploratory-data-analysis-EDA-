from abc import ABC, abstractmethod

class DatasetLoader(ABC):
    @abstractmethod
    def load_data(self):
        pass
