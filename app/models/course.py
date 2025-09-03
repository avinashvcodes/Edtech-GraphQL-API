from sqlalchemy import Column, String, TIMESTAMP, Text, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from .base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    teacher_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now()) # pylint: disable=not-callable

    teacher = relationship(
        "User",
        back_populates="courses"
    )

    sections = relationship(
        "Section",
        back_populates="course",
        order_by="Section.order_index",
        cascade="all, delete-orphan"
    )

    __table_args__ = (
        UniqueConstraint('title', 'teacher_id', name='unique_title_per_teacher'),
    )

    def __repr__(self):
        return f"<Course(id={self.id}, title={self.title}, teacher_id={self.teacher_id})>"
