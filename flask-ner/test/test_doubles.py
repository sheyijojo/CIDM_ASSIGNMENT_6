class NerModelTestDouble:
    """
    Test Double for Spacy NLP model
    """

    def __init__(self, model):
        self.model = model

    def returns_doc_ents(self, ents):
        self.ents = ents

    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)


class DocTestDouble:
    """
    Test double for spaCy Doc
    """

    def __init__(self, sent, ents): 
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents] #spacy format

    def patch_method(self, attr, return_value):
        def patched(): return_value
        setattr(self, attr, patched)
        return self

class SpanTestDouble:
    """
    Test double for spacy Span
    """
    def __init__(self, text, label):
        self.text = text
        self.label_ = label
