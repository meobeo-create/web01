import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.main import app
from app.database import get_session

# Tạo engine SQLite chạy hoàn toàn trong bộ nhớ (RAM)
SQLLITE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLLITE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

@pytest.fixture(name="session")
def session_fixture():
    # Tạo tất cả các bảng trong DB ảo
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    # Xóa sạch bảng sau khi test xong
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="client")
def client_fixture(session: Session):
    # Ghi đè (override) hàm get_session của FastAPI bằng DB ảo
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()