from sqlalchemy import Column, String, TIMESTAMP, CheckConstraint, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    role = Column(String(20), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now()) # pylint: disable=not-callable

    __table_args__ = (
        CheckConstraint("role IN ('teacher', 'student')", name="role_check"),
    )

    courses = relationship("Course", back_populates="teacher")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, role={self.role})>"

class Course(Base):
    __tablename__ = "courses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    teacher_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now()) # pylint: disable=not-callable

    teacher = relationship("User", back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, title={self.title}, teacher_id={self.teacher_id})>"
