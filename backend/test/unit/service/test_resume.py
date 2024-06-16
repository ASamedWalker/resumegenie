import pytest
from model.resume import Resume
from service import resume as code

sample = Resume(
    name="John Doe",
    email="john.doe@example.com",
    phone="123-456-7890",
    summary="I am a software engineer with experience in developing web applications.",
)

def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    resp = code.get_one("John Doe")
    assert resp == sample

