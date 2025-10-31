import pytest

import sys
import os

# base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
# if base_dir not in sys.path:
#     sys.path.insert(0, base_dir)

# print("Current sys.path:", sys.path)

from src.app import app
from src.database import db

@pytest.fixture(scope="module")
def test_client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://dbuser:dbpass@localhost/test_inventory"
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()
