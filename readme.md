# EdTech GraphQL API

This project is an EdTech dashboard backend built with FastAPI and Ariadne GraphQL.  
It supports managing users and courses with PostgreSQL and SQLAlchemy ORM.

---

## Prerequisites

- Python 3.9+
- PostgreSQL (or Dockerized PostgreSQL)
- Install dependencies: requirements.txt

Setup

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt
Configure your database connection in .env.

Create tables:

python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"

Run the app:

uvicorn app.main:app --reload

GraphQL Endpoint

Access the GraphQL playground at:
http://localhost:8000/graphql

API Overview
Completed Mutations
Create User

mutation CreateCourse($input: CreateCourseInput!) {
  createCourse(course: $input) {
    id
    title
    description
    teacher {
      id
      name
      email
    }
    created_at
  }
}
Example input:
{
  "input": {
    "title": "GraphQL for Beginners",
    "description": "An introductory course on GraphQL fundamentals.",
    "teacherId": "64b10518-d068-4481-8d08-0c6ca9af82e1"
  }
}

Create Course

mutation CreateCourse($input: CourseInput!) {
  createCourse(courseInput: $input) {
    id
    title
    description
    teacher {
      id
      name
    }
  }
}
Example input:
{
  "input": {
    "title": "GraphQL Basics",
    "description": "Introduction to GraphQL",
    "teacherId": "uuid-of-existing-teacher"
  }
}

Queries (Under Development)

Query to fetch users by role
Query to list all courses
Query to fetch courses by teacher

Other Mutations (Planned)

Update User
Update Course
Delete User/Course

Notes

Users must be created before creating courses to assign the teacher properly.
UUIDs are used as primary keys.
SQLAlchemy is used for ORM and schema generation.
PostgreSQL is the database backend (Docker recommended if local install unavailable).

🚧 Project is under active development.
