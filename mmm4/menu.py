"""
создать меню
добавить 1 пункт:
    Описание
    Схема работы
добавить 2 пункт:
    ...

а = вывод(приглашение)
меню.запуск(а)
"""


from typing import Callable

class MenuItem():
    description: str
    procedure: Callable[[], None]
    def __init__(self, description: str, procedure: Callable[[], None]):
        self.description = description
        self.procedure = procedure

class Menu():
    menu_items: list[MenuItem] = []
    def add(self, item : MenuItem, index:int = -1):
        ...
    
    def add(self, description:str, procedure: Callable[[], None], index:int = -1):
        item = MenuItem(description, procedure)
        if index>=0:
            self.menu_items.insert(index, item)
        else:
            self.menu_items.append(item)

    def get_readable_menu(self) -> str:
        paper = ""
        for i in range(len(self.menu_items)):
            paper += f"{i}:\t{self.menu_items[i].description}\n"
        return paper

    def run(self, variant_index: int):
        self.menu_items[variant_index].procedure()