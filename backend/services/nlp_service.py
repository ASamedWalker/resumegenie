import spacy
nlp = spacy.load('en_core_web_sm')


def extract_skills(job_description: str):
    doc = nlp(job_description)
    skills = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']]
    return list