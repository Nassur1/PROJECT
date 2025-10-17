from sqlalchemy import Column, Numeric, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import uuid

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    car_id = Column(UUID(as_uuid=True), ForeignKey('cars.id', ondelete='RESTRICT'), nullable=False)
    customer_id = Column(UUID(as_uuid=True), ForeignKey('customers.id', ondelete='RESTRICT'), nullable=False)
    seller_id = Column(UUID(as_uuid=True), ForeignKey('sellers.id', ondelete='RESTRICT'), nullable=False)
    sale_price = Column(Numeric(12, 2), nullable=False)
    sale_date = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    car = relationship("Car", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")
    seller = relationship("Seller", back_populates="sales")
    payments = relationship("Payment", back_populates="sale", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Sale(id={self.id}, car_id={self.car_id}, customer_id={self.customer_id}, sale_price={self.sale_price})>"

    def to_dict(self):
        return {
            'id': str(self.id),
            'car_id': str(self.car_id),
            'customer_id': str(self.customer_id),
            'seller_id': str(self.seller_id),
            'sale_price': float(self.sale_price),
            'sale_date': self.sale_date.isoformat() if self.sale_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
