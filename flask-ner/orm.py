from importlib.metadata import metadata
from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper,relationship 

import model 

metadata = metadata()

ent_table = Table(

    'ent_table', metadata,
    Column('person', String(255), primary_key = False),
    Column('NORP', String(255)),
    Column('LANGUAGE', String(255)),
    Column('GPE', String(255)),

)






