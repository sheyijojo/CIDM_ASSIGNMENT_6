from abc import ABC, abstractmethod
import abc
from test_doubles import DocTestDouble, NerModelTestDouble
import orm
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

#the ssimplest repo has just two methods get(), add(). use these methods only for domain and service layer
#this is to prevent coupling domaiin to database.

class AbstractRespository(abc.ABC):

    @abc.abstractmethod
    def add(self, doc:DocTestDouble):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, text, label_) -> DocTestDouble:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRespository):
    def __init__(self, session):
        self.session = session

    def add(self, doc):
        self.session.add(doc)

    def get(self, text, label_):
        return self.session.query(DocTestDouble).filter_by(reference=(text, label_))

    
