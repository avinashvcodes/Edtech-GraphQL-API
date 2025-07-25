from sqlalchemy import Column, String, TIMESTAMP, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    role = Column(String(20), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now()) # pylint: disable=not-callable

    __table_args__ = (
        CheckConstraint("role IN ('TEACHER', 'STUDENT', 'ADMIN')", name="role_check"),
    )

    courses = relationship("Course", back_populates="teacher")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, role={self.role})>"
