from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    posts: Mapped[list['Post']] = relationship(back_populates='user', cascade="all, delete-orphan")

class Post(Base):
    __tablename__ = 'post'

    def __init__(self, title: str, content: str, user_id: int):
        self.title = title
        self.content = content
        self.user_id = user_id

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(Text)
    user_id = Column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship('User', back_populates='posts')
