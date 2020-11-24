import spacy

nlp = spacy.load("cs_core_web_sm")
doc = nlp("This is a sentence.")
