#def test_entity_mapper_
#from requests import session
import ner_client
from datetime import date

def_test_entity_mapper_can_load_entity(session):
    session.execute(
        "INSERT INTO named_entity_client(PERSON, NORP, LANGUAGE, GPE) VALUES"
        '("Sheyi", "Nigerian", "English", "Africa")'

    )
    expected = [
        ner_client.NamedEntityClient("Sheyi", "Nigerian", "English", "Africa")

    ]

    assert session.query(ner_client.NamedEntityClient).all() == expected


    