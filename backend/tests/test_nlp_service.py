from services.nlp_service import extract_skills

def test_extract_skills():
    job_description = "Looking for a candidate skilled in Python, machine learning, and data analysis."
    expected_skills = {'Python', 'machine learning', 'data analysis'}
    extracted_skills = extract_skills(job_description)
    assert extracted_skills == expected_skills, f"Expected {expected_skills}, got {extracted_skills}"
