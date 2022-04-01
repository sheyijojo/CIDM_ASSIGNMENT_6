import unittest
from ner_client import NamedEntityClient


class TestNerClient(unittest.TestCase):
     # how the return data structure would look like(dict)
        # {ents: [{....}],
        #   html: "<span>..."}

    def test_get_ents_returns_dictionary_given_empty_input(self):
        ner = NamedEntityClient()
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict) # retruns a dict from a string input


       