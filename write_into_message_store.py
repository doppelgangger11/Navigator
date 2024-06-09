from database import (
    engine, 
    SessionLocal, 
    Base
)
from test_massege import Message
from random import randint
from datetime import datetime



session = SessionLocal()

def add_test_messages():
    test_messages = [
        {"type": "Hello, World!", "data": {"content": "Hello, World!"}},
        {"type": "This is a test message.", "data": {"content": "This is a test message."}},
        {"type": "SQLAlchemy is great!", "data": {"content": "SQLAlchemy is great!"}}
    ]
    
    try:
        for message in test_messages:
            new_message = Message(
                global_position=randint(0, 100),
                position=randint(100, 200),
                time=datetime.now(),
                stream_name="test_stream",
                type=message["type"],
                data=message["data"]
            )
            session.add(new_message)
        
        session.commit()
        print("Данные вставлены успешно")
    except Exception as e:
        session.rollback()
        print("Ошибка вставки данных:", e)

if __name__ == "__main__":

    add_test_messages()
    print("////////////////////////////////")
