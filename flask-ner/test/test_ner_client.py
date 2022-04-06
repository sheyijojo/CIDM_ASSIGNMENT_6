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
    
    def test_get_ents_returns_dict_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Sheyi is great guy")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_required_serializes_to_person(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Dr Babbs', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Dr Babbs', 'label': 'Person'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_required_serializes_to_group(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Nigerian', 'label_': 'NORP'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Nigerian', 'label': 'Group'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])


    def test_get_ents_given_spacy_LOC_is_required_serializes_to_location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'the ocean', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'the ocean', 'label': 'Location'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LANGUAGE_is_required_serializes_to_language(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'ASL', 'label_': 'LANGUAGE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'ASL', 'label': 'Language'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])
    
    def test_get_ents_given_spacy_GPE_is_required_serializes_to_Location(self):#GEOPOLICALENTITTY
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Nigeria', 'label_': 'GPE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Nigeria', 'label': 'Location'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_given_multiple_ents_serializes_all(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Nigeria', 'label_': 'GPE'}, {'text': 'Novak Jokovich', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': 
        [{'ent': 'Nigeria', 'label': 'Location'}, 
        {'ent': 'Novak Jokovich', 'label':'Person'}], 'html': ""}
        self.assertListEqual(result['ents'], expected_result['ents'])