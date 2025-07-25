import uuid

from app.models.course import Course
from ariadne import MutationType
from app.models.user import User
from sqlalchemy.orm import Session

mutation = MutationType()

@mutation.field("createCourse")
def resolve_create_course(_, info, course):
    db = info.context["db"]

    new_course = Course(
        title=course["title"],
        description=course.get("description"),
        teacher_id=course["teacherId"]
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course

mutation = MutationType()

@mutation.field("createUser")
def resolve_create_user(_, info, user):
    db: Session = info.context["db"]
    new_user = User(id=uuid.uuid4(),
                    name=user["name"],
                    email=user["email"],
                    role=user["role"])
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
