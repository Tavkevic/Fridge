import logging
import sys

from Items.fridge_s import Fridge
logging.basicConfig(level=logging.INFO,
                    format=" %(message)s "
                           "\n %(asctime)s - %(levelname)s ")



if __name__ == "__main__":
    logging.info("Напиши имя холодильника: ")
    name = str(input())
    fridge = Fridge(name)

    while True:
        logging.info("Что хотите сделать?"
                     "\n 1 - добавить_полку"
                     "\n 2 - убрать_полку"
                     "\n 3 - что_в_х"
                     "\n 4 - поставить"
                     "\n 5 - взять"
                     "\n 6 - уйти")

        x = int(input())
        if x == 3:
            fridge.shelf_in_fridge()

        elif x == 1:

            fridge.shelf_in_fridge()
            logging.info("имя полки")
            name = str(input())
            logging.info("размер полки %s", name)
            size = int(input())
            fridge.create_shelf(name, size)
            fridge.shelf_in_fridge()

        elif x == 2:
            fridge.shelf_in_fridge()
            if fridge.shelfs:
                logging.info("какую полку вы хотите убрать(предметы с полки пропадут)")
                name = str(input())
                fridge.delete_shelf(name)
                fridge.shelf_in_fridge()
            else:
                logging.info("Добавьте полки в холодильник")

        elif x == 4:
            fridge.shelf_in_fridge()
            if fridge.shelfs:
                logging.info("Название предмета")
                name = str(input())
                logging.info("Добавить кол-во")
                many = int(input())
                item = {
                    "name": name,
                    "many": many
                }
                logging.info("название полки")
                shelf = str(input())
                for t in fridge.shelfs:
                    if shelf in t.name:
                        t.put(item)
                        fridge.shelf_in_fridge()
                    else:
                        logging.info("В холодильнике нет такой полки")
            else:
                logging.info("Добавьте полки в холодильник")

        elif x == 5:
                fridge.shelf_in_fridge()
                if fridge.shelfs:
                    logging.info("Что хотите взять?")
                    name = str(input())
                    logging.info("Сколько хотите взять?")
                    many = int(input())
                    item = {
                        "name": name,
                        "many": many
                    }
                    fridge.takes(item)
                    fridge.shelf_in_fridge()
                else:
                    logging.info("Добавьте полки в холодильник")

        elif x == 6:
            sys.exit()
#    except ValueError:
 #       logging.warning("Некорректный ввод. Введите число")

            #"""
        #    __call__
         #   добваить декораторы
          # - раскидать по файлам
           # - добавить if name = main"

