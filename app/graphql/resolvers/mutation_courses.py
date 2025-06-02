from ariadne import MutationType

mutation_courses = MutationType()
from app.models import Course


@mutation_courses.field("createCourse")
def resolve_create_course(_, info, course):
    db = info.context["db"]
    print(info.context["request"])

    new_course = Course(
        title=course["title"],
        description=course.get("description"),
        teacher_id=course["teacherId"]
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course
