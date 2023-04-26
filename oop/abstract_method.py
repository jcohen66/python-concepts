from abc import ABC, abstractmethod


class Phone(ABC):
    def __init__(self, model: str):
        self.model = model

    @property
    @abstractmethod
    def power(self):
        ...
        # raise NotImplementedError

    @abstractmethod
    def call_target(self, name: str):
        ...
        # raise NotImplementedError


class iBanana(Phone):
    def __init__(self, model: str):
        super().__init__(model)

    def call_target(self, name):
        raise NotImplementedError('Code missing.')

    @property
    def power(self):
        return '50% battery remaining.'


phone = iBanana('iBanana')
