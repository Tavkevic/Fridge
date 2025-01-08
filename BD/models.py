from ctypes import ARRAY
from tokenize import String

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Создаем базовый класс для модели
Base = declarative_base()


# Определяем модель таблицы 'data'
class Fridge(Base):
    __tablename__ = 'Fridge'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    shelfs = relationship('Shelfs', back_populates = 'fridge', cascade='all, delete-orphan')

    def __repr__(self):
        return f"id={self.id}, name='{self.name}'"

class Shelfs(Base):
    __tablename__ = 'Shelfs'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, primary_key=False)
    size = sa.Column(sa.Integer, primary_key=False)
    inside = sa.Column(ARRAY(String))
    free_place = sa.Column(sa.Integer, primary_key=False)
    fridge = relationship('Fridge', back_populates='shelfs')

    def __repr__(self):
        return (f"id = {self.id}, name = {self.name}, "
                f"size = {self.size}, inside = {self.inside}, "
                f"free_place ={self.free_place}")
