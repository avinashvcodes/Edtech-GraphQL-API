from ariadne import QueryType
from app.models.course import Course

query = QueryType()

@query.field("coursesByTeacher")
def resolve_courses_by_teacher(_, info, teacherId):
    db = info.context["db"]
    courses = db.query(Course).filter(Course.teacher_id == teacherId).all()
    return courses
