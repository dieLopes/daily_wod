import os
from app.config.database import SessionLocal
from app.models.user import User
from passlib.context import CryptContext
from sqlalchemy.exc import SQLAlchemyError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def seed_admin():
    db = SessionLocal()
    try:
        admin_email = os.getenv("ADMIN_EMAIL")
        admin_password = os.getenv("ADMIN_PASSWORD")
        admin_username = os.getenv("ADMIN_USERNAME")

        if admin_email is None or admin_password is None or admin_username is None:
            print("Variáveis do admin não configiradas")
            return

        existing_admin = db.query(User).filter(User.email == admin_email).first()
        if existing_admin:
            return

        hashed_password = pwd_context.hash(admin_password)
        admin_user = User(
            username=admin_username,
            email=admin_email,
            hashed_password=hashed_password
        )
        db.add(admin_user)
        db.commit()
        print("Usuário admin criado com sucesso.")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Erro ao criar admin: {e}")
    finally:
        db.close()
