from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Fridge(Base):
    __tablename__ = 'Fridges'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    shelves = relationship("Shelf", back_populates="fridge", cascade="all, delete-orphan")


class Shelf(Base):
    __tablename__ = 'Shelves'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fridges_id = Column(Integer, ForeignKey('Fridges.id', ondelete='CASCADE'), nullable=False)
    name = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    free_place = Column(Integer, nullable=False)

    fridge = relationship("Fridge", back_populates="shelves")
    products = relationship("Product", back_populates="shelf", cascade="all, delete-orphan")


class Product(Base):
    __tablename__ = 'Product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    shelves_id = Column(Integer, ForeignKey('Shelves.id', ondelete='CASCADE'), nullable=False)
    name = Column(String, nullable=False)
    many = Column(Integer, nullable=False)

    shelf = relationship("Shelf", back_populates="products")