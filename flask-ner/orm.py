from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper,relationship 

from test_doubles import *

metadata = MetaData()

ner_model_test_double = Table(

    'ner_model_test_double', metadata,
    Column('sentence', String(500), primary_key= True),
    Column('label_', String(255)),
)

ner_doc_test_double = Table(
    
    'ner_doc_test_double', metadata,
    Column('text',  String(500), primary_key= True),
    Column('label_',  String(255)),

)

ner_span_test_double = Table(

    'ner_span_test_double', metadata,
    Column('text', String(500), primary_key= True),
    Column('label_',  String(255))


)  



def start_mappers():
    model_mapper = mapper(NerModelTestDouble, ner_model_test_double)
    doc_mapper = mapper(DocTestDouble, ner_doc_test_double)
    span_mapper = mapper(SpanTestDouble, ner_span_test_double)
  




