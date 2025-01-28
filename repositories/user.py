from sqlalchemy import Engine
from sqlalchemy.orm import Session
from db.models import User

class user_repository:
    def __init__(self, engine: Engine):
        self.engine = engine

    def create_users(self, u: list[User]):
        with Session(self.engine) as session:
            session.add_all(u)
            session.commit()
    
    def get_all(self):
        with Session(self.engine) as session:
            users = session.query(User).all()
            return users
