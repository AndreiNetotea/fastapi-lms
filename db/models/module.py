from ..db_setup import Base

from .mixins import Timestamp
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship


class Module(Timestamp, Base):
    """
    Modules contain multiple courses,
    and multiple users can be in the same module.
    """

    __tablename__ = "module"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)

    users = relationship("User", back_populates="module")
    courses = relationship("Course", back_populates="module")
