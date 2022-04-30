#def test_entity_mapper_
#from requests import session
import test_doubles
from datetime import date


def test_model_mapper_can_load_sentence_and_label(session):
    session.execute(
        "INSERT INTO ner_model_test_double (sentence, label_) VALUES "
        '("United states is a great country", "United States")'

    )

    expected = [
        test_doubles.NerModelTestDouble("United states is a great country"),
        test_doubles.NerModelTestDouble("United States"),

    ]

    assert session.query(test_doubles.NerModelTestDouble).all() == expected


def test_doc_mapper_can_load_text_and_label(session):
    session.execute(
        "INSERT INTO ner_span_test_double (sentence, label_) VALUES "
        '("Nigeria is a country in west africa", "Nigeria")'

    )

    expected = [
        test_doubles.DocTestDouble("Nigeria is a country in west africa"),
        test_doubles.DocTestDouble("Nigeria"),

    ]

    assert session.query(test_doubles.NerModelTestDouble).all() == expected


def test_span_mapper_can_load_text_and_label(session):
    session.execute(
        "INSERT INTO ner_span_test_double (sentence, label_) VALUES "
        '("Nigeria is a country in west africa", "Nigeria")'

    )

    expected = [
        test_doubles.SpanTestDouble("Nigeria is a country in west africa"),
        test_doubles.SpanTestDouble("Nigeria"),

    ]

    assert session.query(test_doubles.SpanTestDouble).all() == expected






    