import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_execute_success(client):
    response = client.post('/api/execute', json={
        "script": "deb\nimpr 42\nfin"
    })
    assert response.status_code == 200
    assert response.json == {"output": "42"}

def test_execute_empty_script(client):
    response = client.post('/api/execute', json={"script": ""})
    assert response.status_code == 400
    assert "Empty script provided" in response.json["error"]

def test_execute_missing_script(client):
    response = client.post('/api/execute', json={})
    assert response.status_code == 400
    assert "No script provided" in response.json["error"]

def test_docs_index(client):
    response = client.get('/api/docs/')
    assert response.status_code in [200, 404]  # Depends on if index.html exists

def test_docs_file_not_found(client):
    response = client.get('/api/docs/nonexistent.html')
    assert response.status_code == 404
    assert "Documentation file not found" in response.json["error"]
