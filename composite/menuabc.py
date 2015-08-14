from abc import ABC, abstractmethod


class MenuComponent(ABC):
    '''Item do cardápio, com sub-itens'''

    def append(self, item):
        '''incluir sub-item'''
        raise NotImplementedError()

    def remove(self, item):
        '''remover sub-item'''
        raise NotImplementedError()

    def __getitem__(self, i):
        '''obter sub-item pelo índice'''
        raise NotImplementedError()

    @property
    @abstractmethod
    def name(self):
        '''obter nome do item'''

    @property
    @abstractmethod
    def description(self):
        '''obter descrição do item'''

    @property
    def price(self):
        '''obter preço do item'''
        raise NotImplementedError()

    @property
    @abstractmethod
    def is_vegetarian(self):
        '''obter booleano indicador de item vegetariano'''

    @abstractmethod
    def display(self):
        '''exibir item e sub-itens'''
