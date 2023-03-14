from sqlalchemy import String, create_engine
from sqlalchemy.orm import *

engine = create_engine("sqlite:///data.db", echo=True)


class Base(DeclarativeBase):
    pass


class DataStore(Base):
    __tablename__ = "data_store"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"

Base.metadata.create_all(engine)
