import pytest
import jwt
from unittest.mock import MagicMock, patch
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from app.models.user import User
from app.services.auth_service import get_current_user
from app.services.auth_service import hash_password, verify_password, create_access_token
from datetime import timedelta
from app.config import settings

@pytest.fixture
def db():
    """Mock do banco de dados (SQLAlchemy Session)."""
    return MagicMock()

@pytest.fixture
def mock_user(db: MagicMock):
    """Mock de um usuário encontrado no banco."""
    user = User(
        id=1,
        username="testuser",
        email="testuser@example.com",
        hashed_password="hashedpassword"
    )
    db.query.return_value.filter.return_value.first.return_value = user
    return user

@patch("app.services.auth_service.SECRET_KEY", None)
@patch("app.services.auth_service.ALGORITHM", None)
def test_jwt_configuration_error(monkeypatch: pytest.MonkeyPatch, db: MagicMock):
    """Deve lançar erro 500 se variáveis SECRET_KEY ou ALGORITHM não estiverem configuradas."""

    monkeypatch.delenv("SECRET_KEY", raising=False)
    monkeypatch.delenv("ALGORITHM", raising=False)

    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials="fake_token")

    with pytest.raises(HTTPException) as exc_info:
        get_current_user(credentials=credentials, db=db)
    
    assert exc_info.value.status_code == 500
    assert "não configuradas" in exc_info.value.detail.lower()

def test_get_current_user(mock_user: User, db: MagicMock):
    """Deve retornar o usuário autenticado corretamente."""

    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials="valid_token")

    with patch("app.services.auth_service.jwt.decode", return_value={"sub": mock_user.username}):
        user = get_current_user(credentials=credentials, db=db)

    assert user.username == mock_user.username
    assert user.email == mock_user.email

def test_get_current_user_user_not_found(db: MagicMock):
    """Deve lançar erro 404 se o usuário não for encontrado."""

    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials="valid_token")

    db.query.return_value.filter.return_value.first.return_value = None

    with patch("app.services.auth_service.jwt.decode", return_value={"sub": "nonexistentuser"}):
        with pytest.raises(HTTPException) as exc_info:
            get_current_user(credentials=credentials, db=db)

    assert exc_info.value.status_code == 404
    assert "não encontrado" in exc_info.value.detail.lower()

def test_hash_password():
    password = "supersecret"
    hashed = hash_password(password)
    
    assert hashed != password
    assert verify_password(password, hashed)

def test_verify_password_correct():
    password = "testpassword"
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True

def test_verify_password_incorrect():
    password = "testpassword"
    hashed = hash_password(password)
    assert verify_password("wrongpassword", hashed) is False

def test_create_access_token():
    data = {"sub": "testuser"}
    token = create_access_token(data=data, expires_delta=timedelta(minutes=5))
    
    assert token is not None
    assert isinstance(token, str)

    alg = settings.ALGORITHM
    if alg is None:
        alg = "HS256"

    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[alg])
    assert decoded["sub"] == "testuser"
    assert "exp" in decoded