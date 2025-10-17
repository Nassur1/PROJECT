from models.payment import Payment
from models.sale import Sale
from database import get_db, close_db
from decimal import Decimal
import uuid

class PaymentManager:

    @staticmethod
    def create_payment(sale_id, amount, payment_method, status='pending'):
        db = get_db()
        try:
            sale = db.query(Sale).filter(Sale.id == uuid.UUID(sale_id)).first()
            if not sale:
                print("\nSale not found!")
                return None

            payment = Payment(
                sale_id=uuid.UUID(sale_id),
                amount=Decimal(str(amount)),
                payment_method=payment_method,
                status=status
            )
            db.add(payment)
            db.commit()
            db.refresh(payment)
            print(f"\nPayment created successfully! ID: {payment.id}")
            return payment
        except Exception as e:
            db.rollback()
            print(f"\nError creating payment: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def get_all_payments():
        db = get_db()
        try:
            payments = db.query(Payment).all()
            return payments
        except Exception as e:
            print(f"\nError fetching payments: {e}")
            return []
        finally:
            close_db(db)

    @staticmethod
    def get_payment_by_id(payment_id):
        db = get_db()
        try:
            payment = db.query(Payment).filter(Payment.id == payment_id).first()
            return payment
        except Exception as e:
            print(f"\nError fetching payment: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def get_payments_by_sale(sale_id):
        db = get_db()
        try:
            payments = db.query(Payment).filter(Payment.sale_id == uuid.UUID(sale_id)).all()
            return payments
        except Exception as e:
            print(f"\nError fetching payments by sale: {e}")
            return []
        finally:
            close_db(db)

    @staticmethod
    def update_payment_status(payment_id, status):
        db = get_db()
        try:
            payment = db.query(Payment).filter(Payment.id == payment_id).first()
            if not payment:
                print("\nPayment not found!")
                return None

            payment.status = status
            db.commit()
            db.refresh(payment)
            print(f"\nPayment status updated to '{status}'!")
            return payment
        except Exception as e:
            db.rollback()
            print(f"\nError updating payment status: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def delete_payment(payment_id):
        db = get_db()
        try:
            payment = db.query(Payment).filter(Payment.id == payment_id).first()
            if not payment:
                print("\nPayment not found!")
                return False

            db.delete(payment)
            db.commit()
            print("\nPayment deleted successfully!")
            return True
        except Exception as e:
            db.rollback()
            print(f"\nError deleting payment: {e}")
            return False
        finally:
            close_db(db)

    @staticmethod
    def get_total_payments_for_sale(sale_id):
        db = get_db()
        try:
            total = db.query(Payment).filter(
                Payment.sale_id == uuid.UUID(sale_id),
                Payment.status == 'completed'
            ).with_entities(db.func.sum(Payment.amount)).scalar()
            return float(total) if total else 0.0
        except Exception as e:
            print(f"\nError calculating total payments: {e}")
            return 0.0
        finally:
            close_db(db)

    @staticmethod
    def display_payments(payments):
        if not payments:
            print("\nNo payments found.")
            return

        print("\n" + "="*120)
        print(f"{'ID':<38} {'Sale ID':<38} {'Amount':<12} {'Method':<15} {'Status':<10}")
        print("="*120)
        for payment in payments:
            print(f"{str(payment.id):<38} {str(payment.sale_id):<38} ${float(payment.amount):<11.2f} {payment.payment_method:<15} {payment.status:<10}")
        print("="*120)

    @staticmethod
    def display_payment_details(payment):
        if not payment:
            print("\nPayment not found.")
            return

        print("\n" + "="*80)
        print("PAYMENT DETAILS")
        print("="*80)
        print(f"Payment ID:      {payment.id}")
        print(f"Sale ID:         {payment.sale_id}")
        print(f"Amount:          ${float(payment.amount):,.2f}")
        print(f"Payment Method:  {payment.payment_method}")
        print(f"Status:          {payment.status}")
        print(f"Payment Date:    {payment.payment_date}")
        print("="*80)
