from sqlalchemy import Column, String, Numeric, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import uuid

class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    commission_rate = Column(Numeric(5, 2), default=0.00)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    cars = relationship("Car", back_populates="seller")
    sales = relationship("Sale", back_populates="seller")

    def __repr__(self):
        return f"<Seller(id={self.id}, name='{self.name}', email='{self.email}')>"

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'commission_rate': float(self.commission_rate),
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
