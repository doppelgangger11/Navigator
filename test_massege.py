import sqlalchemy
from sqlalchemy import Column, Integer, String


Base = sqlalchemy.orm.declarative_base()

class Message(Base):
    __tablename__ = "message_store"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)