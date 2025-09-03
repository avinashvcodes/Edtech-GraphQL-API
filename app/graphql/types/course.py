from ariadne import ObjectType

course_object = ObjectType("Course")

@course_object.field("sections")
def resolve_sections(course_obj, info):
    # need to integrate db
    return []

@course_object.field("students")
def resolve_students(course_obj, info):
    # need to integrate db
    return []
