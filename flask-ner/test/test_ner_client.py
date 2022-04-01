from pyexpat import model
import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble


class TestNerClient(unittest.TestCase):
     # how the return data structure would look like(dict)
        # {ents: [{....}],
        #   html: "<span>..."}

    def test_get_ents_returns_dictionary_given_empty_str_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict) # returns a dict from a string input
        #self.assertEqual(ents, {})
    
    def test_get_ents_returns_list_given_non_empty_string(self):
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Sheyi is great guy")
        self.assertIsInstance(ents, dict)

