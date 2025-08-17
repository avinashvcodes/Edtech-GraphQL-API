import uuid
from sqlalchemy import Column, String, Text, TIMESTAMP, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .base import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    section_id = Column(UUID(as_uuid=True), ForeignKey("sections.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=True)
    order_index = Column(Integer, nullable=False, default=10)
    created_at = Column(TIMESTAMP, server_default=func.now()) # pylint: disable=not-callable

    section = relationship("Section", back_populates="lessons")

    __table_args__ = (
        UniqueConstraint("section_id", "order_index", name="unique_lesson_order_per_section"),
    )

    def __repr__(self):
        return f"<Lesson(id={self.id}, title={self.title}, order_index={self.order_index})>"
