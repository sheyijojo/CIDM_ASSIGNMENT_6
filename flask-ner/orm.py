from importlib.metadata import metadata
from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper,relationship 

import model 

metadata = metadata()

