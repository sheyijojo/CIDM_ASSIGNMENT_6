from importlib.metadata import metadata
from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper,relationship 

from ner_client import *

metadata = metadata()

named_entity_client = Table(

    'named_entity_client', metadata,
    Column('PERSON', String(255), primary_key= False),
    Column('NORP', String(255)),
    Column('LANGUAGE', String(255)),
    Column('GPE', String(255)),

)

   

def start_mappers():
    entity_mapper = mapper(NamedEntityClient, named_entity_client)
  




