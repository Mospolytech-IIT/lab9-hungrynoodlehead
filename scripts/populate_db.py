from sqlalchemy.orm import Session
from db.engine import engine
from db.models import User, Post

if __name__ == "__main__":
    with Session(engine) as session:
        user1 = User(username="andrew", email="andrew@example.com", password="12345")
        user2 = User(username="julia", email="julia@example.com", password="54321")
        session.add_all([user1, user2])
        session.commit()

        post1 = Post(title="First post", content="First post content", user_id=user1.id)
        post2 = Post(title="Second post", content="Second post content", user_id=user2.id)
        session.add_all([post1, post2])
        session.commit()
