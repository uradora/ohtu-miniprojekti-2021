import tempfile
import pytest
from flask import Flask
from database import db

_test_app = Flask(__name__)

_test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

_test_app.secret_key = "test"
test_db_file = tempfile.NamedTemporaryFile()
_test_app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{test_db_file.name}"
_test_app.config["SQLALCHEMY_ECHO"] = True

_test_app_ctx = _test_app.app_context()

def load_test_app():
    _test_app_ctx.push()
    db.init_app(_test_app)
    db.create_all()

def unload_test_app():
    _test_app_ctx.pop()

def clear_tables():
    db.session.rollback()
    for table in reversed(db.metadata.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()

@pytest.fixture(scope='function')
def fixture_test_app():
    load_test_app()
    yield db
    clear_tables()
    unload_test_app()
