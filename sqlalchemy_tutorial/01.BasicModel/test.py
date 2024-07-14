from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()

class User1(Base):
    __tablename__ = "user1"
    rowid = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)

    def __repr__(self):
        return f"User<rowid = {self.rowid}, name = {self.name}, age = {self.age}>"

engine = create_engine("sqlite:///test.db")
session = Session(engine)

user = User1(name = "Alice", age = "49")
session.add(user)
session.commit()

