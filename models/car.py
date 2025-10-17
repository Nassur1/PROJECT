from sqlalchemy import Column, String, Integer, Numeric, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import uuid

class Car(Base):
    __tablename__ = 'cars'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
    price = Column(Numeric(12, 2), nullable=False)
    mileage = Column(Integer, default=0)
    condition = Column(String, nullable=False, default='used')
    status = Column(String, nullable=False, default='available')
    seller_id = Column(UUID(as_uuid=True), ForeignKey('sellers.id', ondelete='SET NULL'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    seller = relationship("Seller", back_populates="cars")
    sales = relationship("Sale", back_populates="car")

    def __repr__(self):
        return f"<Car(id={self.id}, make='{self.make}', model='{self.model}', year={self.year}, status='{self.status}')>"

    def to_dict(self):
        return {
            'id': str(self.id),
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'color': self.color,
            'price': float(self.price),
            'mileage': self.mileage,
            'condition': self.condition,
            'status': self.status,
            'seller_id': str(self.seller_id) if self.seller_id else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
