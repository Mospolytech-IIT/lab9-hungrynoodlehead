from fastapi import FastAPI, Depends
from fastapi.responses import Response
from sqlalchemy.orm import sessionmaker, Session
from db.engine import engine
from db.models import User, Post
from pydantic import BaseModel

app = FastAPI()
SessionLocal = sessionmaker(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class user_form(BaseModel):
    username: str
    email: str
    password: str

@app.post("/user")
def create_user(form: user_form, db: Session = Depends(get_db)):
    user = User(username=form.username, email=form.email, password=form.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/user/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=user_id).first()
    if user is None:
        return Response(status_code=404)
    return user

@app.put("/user/{user_id}")
def update_user(user_id: int, form: user_form, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=user_id).first()
    if user is None:
        return Response(status_code=404)
    user.username = form.username
    user.email = form.email
    user.password = form.password
    db.commit()
    db.refresh(user)
    return user

@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=user_id).first()
    if user is None:
        return Response(status_code=404)
    db.delete(user)
    db.commit()
    return Response(status_code=204)

@app.post("/post")
def create_post(user_id: int, title: str, content: str, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=user_id).first()
    if user is None:
        return Response("user not found", status_code=400)
    post = Post(title=title, content=content, user_id=user.id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@app.get("/post/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter_by(id=post_id).first()
    if post is None:
        return Response(status_code=404)
    return post

@app.put("/post/{post_id}")
def update_post(post_id: int, title: str, content: str, db: Session = Depends(get_db)):
    post = db.query(Post).filter_by(id=post_id).first()
    if post is None:
        return Response(status_code=404)
    post.title = title
    post.content = content
    db.commit()
    db.refresh(post)
    return post

@app.delete("/post/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter_by(id=post_id).first()
    if post is None:
        return Response(status_code=404)
    db.delete(post)
    db.commit()
    return Response(status_code=204)
