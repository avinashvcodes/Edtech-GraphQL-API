import uuid
from sqlalchemy import Column, String, Text, TIMESTAMP, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .base import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=True)
    order_index = Column(Integer, nullable=False, default=10)
    created_at = Column(TIMESTAMP, server_default=func.now()) # pylint: disable=not-callable

    course = relationship("Course", back_populates="lessons")

    def __repr__(self):
        return f"<Lesson(id={self.id}, title={self.title}, order_index={self.order_index})>"
