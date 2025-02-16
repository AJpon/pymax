import gui
from gui.qt import QtWidgets


class Menu(object):
    @property
    def main_menubar(self) -> QtWidgets.QMenuBar:
        return list(self.main_widget.findChildren(QtWidgets.QMenuBar))[0]

    def __init__(self):
        super().__init__()
        self.main_widget = gui.get_main_window()

    # def add_menu(self, name: str):
    #     """
    #     Add a menu to the main menubar.
    #     """
    #     menu_bar = self.main_menubar
    #     items = menu_bar.findChildren(QtWidgets.QMenu)
    #     for item in items:
    #         if item.title() == name:
    #             return item
    #         elif item.title() == "&Help":
    #             menu = menu_bar.addMenu(name)
    #             return menu
