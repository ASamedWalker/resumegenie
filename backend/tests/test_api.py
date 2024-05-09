import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_create_resume_endpoint():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/resumes/", json={
            "resume_data": {"name": "John Doe", "email": "john@example.com"},
            "job_description": "Experience with Python and machine learning is required."
        })
        assert response.status_code == 200
        response_data = response.json()
        assert response_data is not None, "Response data is None"
        data = response.json()
        assert "skills" in data, "Skills key is missing in response"
        assert "Python" in data["skills"], "Python is not listed in skills"
