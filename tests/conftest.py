import pytest
from src.fake_db.database import Database
import importlib
user = importlib.import_module("src.routers.user")

@pytest.fixture(autouse=True)
def fresh_database(monkeypatch):
    monkeypatch.setattr(user, "db", Database())

