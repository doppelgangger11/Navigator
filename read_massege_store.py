from database import (
    engine, 
    SessionLocal, 
    Base
)
from sqlalchemy import MetaData
from test_massege import Message
from time import sleep


metadata = MetaData()

# try:
#     Base.metadata.create_all(engine)
#     print("Таблица создана успешно")
# except Exception as e:
#     print("Ошибка создания таблицы:", e)

session = SessionLocal()

def read_messages():
    messages = session.query(Message).all()
    
    for message in messages:
        print(f"ID: {message.id}, type: {message.type}")

if __name__ == "__main__":

    while True:

        read_messages()
        print("////////////////////////////////")
        sleep(1)