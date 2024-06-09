from database import (
    engine, 
    SessionLocal, 
    Base
)
from test_massege import Message
from sqlalchemy import MetaData, Table, Column, Integer, String


metadata = MetaData()

message_store = Table(
    'message_store', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('content', String, nullable=False)
)

try:
    Base.metadata.create_all(engine)
    print("Таблица создана успешно")
except Exception as e:
    print("Ошибка создания таблицы:", e)

session = SessionLocal()
def read_messages():
    messages = session.query(Message).all()
    
    for message in messages:
        print(f"ID: {message.id}, Content: {message.content}")

def add_test_messages():
    test_messages = [
        "Hello, World!",
        "This is a test message.",
        "SQLAlchemy is great!"
    ]

    try:
        session.execute(
            Message.__table__.insert(),
            [{"content": message} for message in test_messages]
        )
        session.commit()
        print("Данные вставлены успешно")
    except Exception as e:
        session.rollback()
        print("Ошибка вставки данных:", e)

if __name__ == "__main__":

    Base.metadata.create_all(engine)
    print("////////////////////////////////")
    
    add_test_messages()
    print("////////////////////////////////")
    read_messages()
    print("////////////////////////////////")