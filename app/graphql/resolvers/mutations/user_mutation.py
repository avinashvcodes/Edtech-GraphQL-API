import uuid

from ariadne import MutationType
from app.models import User
from sqlalchemy.orm import Session

user_mutation = MutationType()

@user_mutation.field("createUser")
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
