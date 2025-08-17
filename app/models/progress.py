import uuid
from sqlalchemy import Column, TIMESTAMP, ForeignKey, UniqueConstraint, Boolean
from sqlalchemy.dialects.postgresql import UUID

from .base import Base

class Progress(Base):
    __tablename__ = "progress"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    lesson_id = Column(UUID(as_uuid=True), ForeignKey("lessons.id", ondelete="CASCADE"), nullable=False)

    completed = Column(Boolean, default=False)
    completed_at = Column(TIMESTAMP)

    __table_args__ = (
        UniqueConstraint("student_id", "lesson_id", name="unique_student_lesson"),
    )

    def __repr__(self):
        return f"<Progress(id={self.id}, student_id={self.student_id}, lesson_id={self.lesson_id}, completed={self.completed})>"
