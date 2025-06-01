from ariadne import MutationType

mutation_courses = MutationType()

# Temporary in-memory storage for demo purposes
courses = []
course_id_counter = 1

@mutation_courses.field("createCourse")
def resolve_create_course(_, info, title, description=None, teacherId=None):
    global course_id_counter
    new_course = {
        "id": str(course_id_counter),
        "title": title,
        "description": description,
        "teacher": {"id": teacherId, "name": f"Teacher {teacherId}"},
        "students": [],
        "lessons": [],
    }
    courses.append(new_course)
    course_id_counter += 1
    return new_course
