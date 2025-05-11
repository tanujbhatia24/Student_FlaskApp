import pytest
from app import app  # Import your Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_student_by_name(client):
    # Prepopulate the database with test data
    from student_data import students_collection
    if not students_collection.find_one({"name": "Alice"}):
        students_collection.insert_one({"name": "Alice", "age": 21})

    # Fetch the student by name
    response = client.get('/students/name/Alice')
    assert response.status_code == 200
    assert len(response.json) > 0
    assert response.json[0]["name"] == "Alice"

def test_get_student_by_name_not_found(client):
    # Try to fetch a student by a name that doesn't exist
    response = client.get('/students/name/NonExistentName')
    assert response.status_code == 404
    assert response.json["error"] == "No students found with the given name"

def test_add_student(client):
    # Add a new student
    response = client.post('/students', json={"name": "Bob", "age": 22})
    assert response.status_code == 201
    assert response.json["name"] == "Bob"
    assert response.json["age"] == 22

def test_get_all_students(client):
    # Fetch all students
    response = client.get('/students')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0  # Ensure at least one student exists

def test_delete_student(client):
    # Prepopulate the database with test data
    from student_data import students_collection
    student = students_collection.insert_one({"name": "Charlie", "age": 23})

    # Delete the student by ID
    response = client.delete(f'/students/{student.inserted_id}')
    assert response.status_code == 200
    assert response.json["message"] == "Deleted"

    # Verify the student is no longer in the database
    response = client.get(f'/students/{student.inserted_id}')
    assert response.status_code == 404

def test_add_student_missing_fields(client):
    # Try to add a student with missing fields
    response = client.post('/students', json={"name": "Eve"})
    assert response.status_code == 400  # Bad Request
    assert "error" in response.json

def test_get_student_by_partial_name(client):
    # Prepopulate the database with test data
    from student_data import students_collection
    if not students_collection.find_one({"name": "Alice"}):
        students_collection.insert_one({"name": "Alice", "age": 21})

    # Fetch the student by partial name (if supported)
    response = client.get('/students/name/Ali')
    assert response.status_code == 200
    assert len(response.json) > 0
    assert response.json[0]["name"] == "Alice"