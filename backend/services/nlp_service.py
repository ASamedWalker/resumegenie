import spacy
nlp = spacy.load('en_core_web_sm')


def extract_skills(job_description: str):
    known_skills = ['Python', 'machine learning', 'data analysis']  # Replace with your actual list of known skills
    doc = nlp(job_description)
    skills = {chunk.text for chunk in doc.noun_chunks if chunk.root.pos_ in ['NOUN', 'PROPN'] and chunk.text in known_skills}
    return skills