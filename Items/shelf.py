import logging


class Shelf:
    def __init__(self, name: str, size: int, inside = []):
        self.name = name
        self.size = size
        self.inside = inside
        self.free_place = size

    def what_in_shelf(self):
        logging.info("НА полка %s находиться : %s ; "
                     "свободного места %s", self.name, self.inside, self.free_place)

    def what_in_for_work(self):
        item_name = []
        for item_in in self.inside:
            item_name.append(item_in['name'])
        return item_name

    def give_many(self, item):
        for items in self.inside:
            if item["name"] == items["name"]:
                return items["many"]

    def put(self, item: str):
        if self.free_place > 0 and self.free_place >= item["many"]:
            if not self.inside:
                self.inside.append(item)
                logging.info("Поставили на полку %s", self.name)
                self.free_place -= item["many"]
            else:
                for item_in in self.inside:
                    if item["name"] == item_in["name"]:
                        if self.free_place > 0 and self.free_place >= item["many"]:
                            item_in["many"] += item["many"]
                            logging.info("Поставили на полку %s уже к имеющимся,"
                                         " теперь %s - %s шт", self.name, item["name"], item_in["many"])
                            self.free_place -= item["many"]

        elif self.size < len(self.inside) + item["many"]:
            logging.info("На полке %s не хватает места ", self.name)

        else:
            logging.info("Полка полная %s", self.name)

    def removed(self, item: str):
        self.inside.remove(item)
        self.free_place += item["many"]

    def take(self, item):
        if item['name'] in self.what_in_for_work():
            for item_in in self.inside:
                if item["name"] == item_in["name"]:
                    if item["many"] == item_in["many"]:
                        self.removed(item)
                    elif item["many"] < item_in["many"]:
                        item_in["many"] -= item["many"]
                        self.free_place += item["many"]

        else:
            logging.info("%s предмета нет на полке %s", item["name"], self.name)
