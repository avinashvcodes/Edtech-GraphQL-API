# EdTech GraphQL API

This project is an EdTech dashboard backend built with FastAPI and Ariadne GraphQL.  
It supports managing users and courses with PostgreSQL and SQLAlchemy ORM.

---

## Prerequisites

- Python 3.9+
- PostgreSQL
- Install dependencies: requirements.txt

## Setup

**Create a virtual environment and activate it:**

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

**Install dependencies:**

pip install -r requirements.txt

**Create tables:**

python -c "from app.models import Base;from app.database import engine; Base.metadata.create_all(bind=engine)"

**Run the app:**

uvicorn app.main:app --reload

**GraphQL Endpoint**

Access the GraphQL playground at: http://localhost:8000/graphql

## API Overview
### Completed Mutations

<pre lang="markdown"> <code>
```graphql
# Create User
mutation createUser{
    createUser(user: {
        name: "John"
        email: "john@example.com"
        role: TEACHER
    }){
        __typename
    }
} 
# Create Course
mutation createCourse{
    createCourse(course: {
        teacherId: "d366b6d8-3fe3-4222-ab97-d67c049fd79a"
        description: "Introduction to GraphQL"
        title: "GraphQL Basics"
    }){
        __typename
    }
}
```
</code> </pre>

### Under Development

- Query to fetch users by role
- Query to list all courses
- Query to fetch courses by teacher

### Planned

- Update User
- Update Course
- Delete User/Course
- **GraphQL Subscriptions** for real-time updates (e.g., live course notifications)  
- **Docker** setup for easy deployment and development environment  

### Notes

- Users must be created before creating courses to assign the teacher properly.
- UUIDs are used as primary keys.
- SQLAlchemy is used for ORM and schema generation.
- PostgreSQL is the database backend.

🚧 Project is under active development.
