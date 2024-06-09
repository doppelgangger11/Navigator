import sqlalchemy
from sqlalchemy import Column, Integer, String, Time, Date, DateTime, JSON


Base = sqlalchemy.orm.declarative_base()

class Message(Base):
    __table_args__ = {'schema': 'message_store'}
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    global_position = Column(Integer, autoincrement=True, nullable=True)
    position = Column(Integer, autoincrement=True, nullable=True)
    time = Column(DateTime, autoincrement=True, nullable=True)
    stream_name = Column(String, nullable=True)
    type = Column(String, nullable=True)
    data = Column(JSON, nullable=True)