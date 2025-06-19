from abc import ABC, abstractmethod

class BaseHandler(ABC):
    @property
    @abstractmethod
    def handler(self):
        """Return the handler object to be registered"""
        pass
