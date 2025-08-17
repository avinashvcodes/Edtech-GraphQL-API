import uuid
from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .base import Base

class Section(Base):
    __tablename__ = "sections"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(200), nullable=False)
    order_index = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now()) # pylint: disable=not-callable

    course = relationship("Course", back_populates="sections")
    lessons = relationship("Lesson", back_populates="sections", cascade="all, delete-orphan")

    __table_args__ = (
        UniqueConstraint("course_id", "order_index", name="unique_section_order_per_course"),
    )

    def __repr__(self):
        return f"<Section(id={self.id}, title={self.title}, order_index={self.order_index})>"
