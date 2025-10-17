from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import uuid

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sale_id = Column(UUID(as_uuid=True), ForeignKey('sales.id', ondelete='CASCADE'), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    payment_method = Column(String, nullable=False)
    payment_date = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String, nullable=False, default='pending')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    sale = relationship("Sale", back_populates="payments")

    def __repr__(self):
        return f"<Payment(id={self.id}, sale_id={self.sale_id}, amount={self.amount}, status='{self.status}')>"

    def to_dict(self):
        return {
            'id': str(self.id),
            'sale_id': str(self.sale_id),
            'amount': float(self.amount),
            'payment_method': self.payment_method,
            'payment_date': self.payment_date.isoformat() if self.payment_date else None,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
