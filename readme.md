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

python -c "from app.models.base import Base;from app.database import engine; Base.metadata.create_all(bind=engine)"

**Run the app:**

uvicorn app.main:app --reload

**GraphQL Endpoint**

Access the GraphQL playground at: http://localhost:8000/graphql


🚧 Project is under active development.
