import test_doubles
from test_doubles import *
import repository
import pytest
from datetime import date
from repository import SqlAlchemyRepository
from sqlalchemy.orm import Session



def test_repository_can_save_a_text_and_label(session):
    doc = DocTestDouble("This should be saved to my mode", "label_ should also be saved")
    
    repo = SqlAlchemyRepository(session)
    repo.add(doc)
    session.commit()

    rows = list(session.execute(
        'SELECT text,label_ FROM "text"'
    ))
    assert list(rows) == [("1", "1")]

