from app.models import Course
from ariadne import MutationType

course_mutation = MutationType()

@course_mutation.field("createCourse")
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
