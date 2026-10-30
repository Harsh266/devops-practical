
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# Pydantic Student Model
class Student(BaseModel):
    id: int
    name: str
    course: str
    marks: float = Field(ge=0, le=100)

# In-memory student list
students: List[Student] = []

# POST - Add a student
@app.post("/students")
def add_student(student: Student):
    for s in students:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="Student already exists")

    students.append(student)
    return {"message": "Student added successfully", "student": student}

# GET - List all students (with optional course filter)
@app.get("/students")
def get_students(course: Optional[str] = Query(None, description="Filter students by course")):
    if course:
        return [s for s in students if s.course.lower() == course.lower()]
    return students

# GET - Fetch student by ID
@app.get("/students/{id}")
def get_student(id: int):
    for student in students:
        if student.id == id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")

# PUT - Update a student by ID
@app.put("/students/{id}")
def update_student(id: int, updated_student: Student):
    for i, student in enumerate(students):
        if student.id == id:
            students[i] = updated_student
            return {"message": "Student updated successfully", "student": updated_student}
    raise HTTPException(status_code=404, detail="Student not found")

# DELETE - Remove a student by ID
@app.delete("/students/{id}")
def delete_student(id: int):
    for i, student in enumerate(students):
        if student.id == id:
            students.pop(i)
            return {"message": f"Student with id {id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")
