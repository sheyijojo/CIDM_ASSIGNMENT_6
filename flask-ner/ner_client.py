from html import entities
import spacy



class NamedEntityClient:
    def __init__(self, model): #DIP NamedEntity client is dependent on abstraction(model) rather than low-leveldetails
        self.model = model

    
    def get_ents(self, sentence):
        #doc = self.model(sentence) - DIP in action, self.model is abstracted into Class NamedEntityClient.
        doc = self.model(sentence)
        entities = [{'ent': ent.text, 'label': self.map_label(ent.label_) } for ent in doc.ents]
        return { 'ents': entities, 'html': ''}

    @staticmethod
    def map_label(label):
        label_map = {

            'PERSON'    : 'Person',
            'NORP'      : 'Group',
            'LOC'       : 'Location',
            'LANGUAGE'  :'Language',
            'GPE'       :'Location',
        }
        return label_map.get(label)