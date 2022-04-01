import spacy


class NamedEntityClient:
    def __init__(self, model): #DIP NamedEntity client is dependent on abstraction(model) rather than low-leveldetails
        self.model = model

    
    def get_ents(self, sentence):
        #doc = self.model(sentence) - DIP in action, self.model is abstracted into Class NamedEntityClient.
        return {}