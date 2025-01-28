from sqlalchemy.orm import Session
from db.engine import engine
from db.models import Post, User

if __name__ == "__main__":
    with Session(engine) as session:
        users = session.query(User).all()
        for user in users:
            print(user.id, user.username, user.email)

        posts = session.query(Post).join(User).all()
        for post in posts:
            print(post.id, post.title, post.user.username)

        user_posts = session.query(Post).filter(Post.user_id == 1).all()
        for post in user_posts:
            print(post.title, post.content)
