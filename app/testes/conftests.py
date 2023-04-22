import pytest
from aplicacao import create_app, db

@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        yield app

@pytest.fixture(scope="module")
def test_db(test_app):
    db.create_all()
    yield db
    db.drop_all()

@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        yield app

@pytest.fixture(scope="module")
def test_db(test_app):
    db.create_all()
    yield db
    db.drop_all()

@pytest.fixture(scope="module")
def test_client(test_app):
    with test_app.test_client() as client:
        yield client

