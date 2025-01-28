from db.engine import engine
from sqlalchemy.orm import Session

from db.models import User

if __name__ == "__main__":
    with Session(engine) as session:
        user = session.query(User).filter_by(id=1).first()
        session.delete(user)
        session.commit()
