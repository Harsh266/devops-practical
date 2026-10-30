from fastapi.testclient import TestClient
from app import app, students

client = TestClient(app)

def setup_function():
    students.clear()

def test_add_student():
    response = client.post("/students", json={
        "id": 1, "name": "Alice", "course": "DevOps", "marks": 85.5
    })
    assert response.status_code == 200

def test_get_students():
    students.clear()
    client.post("/students", json={"id": 1, "name": "Alice", "course": "DevOps", "marks": 90.0})
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_get_student_by_id():
    students.clear()
    client.post("/students", json={"id": 1, "name": "Alice", "course": "DevOps", "marks": 90.0})
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

def test_student_not_found():
    response = client.get("/students/999")
    assert response.status_code == 404

def test_login_success():
    response = client.post("/login", json={"username": "admin", "password": "admin123"})
    assert response.status_code == 200

def test_login_failure():
    response = client.post("/login", json={"username": "admin", "password": "wrong"})
    assert response.status_code == 401

