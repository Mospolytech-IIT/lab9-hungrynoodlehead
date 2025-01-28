from db.engine import engine
from sqlalchemy.orm import Session

from db.models import Post, User

if __name__ == "__main__":
    with Session(engine) as session:
        user = session.query(User).filter_by(username="andrew").first()
        user.email = "new_email@example.com"
        session.commit()

        post = session.query(Post).filter_by(id=1).first()
        post.content = "New post content"
        session.commit()
