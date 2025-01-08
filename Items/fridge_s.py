import logging
from shelf import Shelf


class Fridge:
    def __init__(self, name = None):
        self.shelfs = []
        self.name = name

    def app_shelf(self, shelf: Shelf):
        if not (shelf in self.shelfs):
            self.shelfs.append(shelf)
            if shelf.inside:
                logging.info("Создали полку %s с обемом в %s предмета, на полке уже есть %s", shelf.name, shelf.size, shelf.inside)
            logging.info("Создали полку %s с обемом в %s предмета", shelf.name, shelf.size)
        else:
            logging.info("Полка с названием %s сушествует", shelf.name)

    def create_shelf(self, name, size):
        shelf = Shelf(name, size)
        if not (shelf in self.shelfs):
            self.shelfs.append(shelf)
            logging.info("Создали полку %s с обемом в %s предмета", name, size)
        else:
            logging.info("Полка с названием %s сушествует", name)

    def delete_shelf(self, name):
        flag = False
        for i, shelf in enumerate(self.shelfs):
            if name == shelf.name:
                del self.shelfs[i]
                flag = True
                logging.info(" Полка %s удалена ", name)
        if not flag:
            logging.info("В холодильнике нет такой полки")

    def shelf_in_fridge(self):
        if not self.shelfs:
            logging.info("В холодильнике нет полок")

        for shelf in self.shelfs:
            shelf.what_in_shelf()

    def takes(self, item):
        shelf_with_item = []
        for shelf in self.shelfs:
            for item_in in shelf.inside:
                if item['name'] == item_in["name"]:
                    if item['many'] <= item_in["many"]:
                        shelf.take({"name": item["name"], "many": shelf.give_many(item)})
                        return
                    shelf_with_item.append(shelf)

        if shelf_with_item:
            for shelf in shelf_with_item:
                if item["many"] >= shelf.give_many(item):
                    item["many"] -= shelf.give_many(item)
                    shelf.take({"name": item["name"], "many": shelf.give_many(item)})
                else:
                    shelf.take(item)
        else:
            logging.info("В холодильнике нету %s", item["name"])