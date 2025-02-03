import logging

from sqlalchemy.orm import sessionmaker

from BD.models import Fridge, Shelfs


class BDFunctions:


    @staticmethod
    def add_fridge_with_shelves(session, fridge_name, shelves_data):

        """
        Добавляет новый холодильник и его полки в базу данных.

        :param session: Сессия SQLAlchemy для работы с БД.
        :param fridge_name: Название холодильника.
        :param shelves_data: Список словарей, содержащих данные о полках.
                             Например: [{"name": "Полка 1", "size": 17, "inside": [{"name": "Яблоки", "many": "5"}, {"name": "Банан", "many": "2"}], "free_place": 10}]
        """

        new_fridge = Fridge(name=fridge_name)

        for shelf in shelves_data:
            new_shelf = Shelfs(
                name=shelf['name'],
                size=shelf['size'],
                inside=shelf['inside'],
                free_place=shelf['free_place']
            )
            new_fridge.shelfs.append(new_shelf)

        session.add(new_fridge)
        session.commit()

    @staticmethod
    def get_fridges_with_shelves(session, fridge_name):
        """
        Получает холодильник с его полками из базы данных.

        :param session: Сессия SQLAlchemy для работы с БД.
        :param fridge_name: Название холодильника.
        :return: Холодильник с его полками.
        """

        fridges = session.query(Fridge).all()

        result = []
        for fridge in fridges:
            if fridge.name == fridge_name:
                fridge_data = {
                    'id': fridge.id,
                    'name': fridge.name,
                    'shelves': [{
                        'id': shelf.id,
                        'name': shelf.name,
                        'size': shelf.size,
                        'inside': shelf.inside,
                        'free_place': shelf.free_place
                    } for shelf in fridge.shelfs]
                }
                result.append(fridge_data)
            else:
                logging.info("Необходимого вам холодильника нету в базе данных")

        return result