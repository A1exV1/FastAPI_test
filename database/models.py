import datetime as dt

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Walker(Base):
    __tablename__ = 'walkers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class Dog(Base):
    __tablename__ = 'dogs'
    __table_args__ = (UniqueConstraint('flat', 'name'),)

    id: Mapped[int] = mapped_column(primary_key=True)
    flat: Mapped[int]
    name: Mapped[str]
    breed: Mapped[str]


class Order(Base):
    __tablename__ = 'orders'
    __table_args__ = (UniqueConstraint('dog_id', 'walk_at'),)

    id: Mapped[int] = mapped_column(primary_key=True)
    dog_walker_id: Mapped[int] = mapped_column(ForeignKey('walkers.id'))
    dog_id: Mapped[int] = mapped_column(ForeignKey('dogs.id'))
    walk_at: Mapped[dt.datetime] = mapped_column(DateTime(timezone=True))
