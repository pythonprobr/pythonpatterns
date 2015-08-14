from menuabc import MenuComponent


class Menu(MenuComponent):

    def __init__(self, name, description):
        self.menu_components = []
        self.__name = name
        self.__description = description

    def append(self, menu_component):
        self.menu_components.append(menu_component)

    def remove(self, menu_component):
        self.menu_components.remove(menu_component)

    def __getitem__(self, index):
        return self.menu_components[index]

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def is_vegetarian(self):
        return all(sub_menu.is_vegetarian for sub_menu in self.menu_components)

    def display(self):
        print('\n' + self.name, end='')
        if self.is_vegetarian:
            print(' (v)', end='')
        print(', ', self.description, sep='')
        print('-' * 60)
        for menu_component in self.menu_components:
            menu_component.display()


class MenuItem(MenuComponent):

    def __init__(self, name, description, vegetarian, price):
        self.__name = name
        self.__description = description
        self.__vegetarian = vegetarian
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def is_vegetarian(self):
        return self.__vegetarian

    @property
    def price(self):
        return self.__price

    def display(self):
        print('  ' + self.name, end='')
        if self.is_vegetarian:
            print(' (v)', end='')
        print(',', self.price)
        print('     --', self.description)
