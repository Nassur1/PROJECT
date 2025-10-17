from models.sale import Sale
from models.car import Car
from database import get_db, close_db
from decimal import Decimal
import uuid

class SaleManager:

    @staticmethod
    def create_sale(car_id, customer_id, seller_id, sale_price):
        db = get_db()
        try:
            car = db.query(Car).filter(Car.id == uuid.UUID(car_id)).first()
            if not car:
                print("\nCar not found!")
                return None

            if car.status != 'available':
                print(f"\nCar is not available! Current status: {car.status}")
                return None

            sale = Sale(
                car_id=uuid.UUID(car_id),
                customer_id=uuid.UUID(customer_id),
                seller_id=uuid.UUID(seller_id),
                sale_price=Decimal(str(sale_price))
            )
            db.add(sale)

            car.status = 'sold'

            db.commit()
            db.refresh(sale)
            print(f"\nSale created successfully! ID: {sale.id}")
            print(f"Car status updated to 'sold'")
            return sale
        except Exception as e:
            db.rollback()
            print(f"\nError creating sale: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def get_all_sales():
        db = get_db()
        try:
            sales = db.query(Sale).all()
            return sales
        except Exception as e:
            print(f"\nError fetching sales: {e}")
            return []
        finally:
            close_db(db)

    @staticmethod
    def get_sale_by_id(sale_id):
        db = get_db()
        try:
            sale = db.query(Sale).filter(Sale.id == sale_id).first()
            return sale
        except Exception as e:
            print(f"\nError fetching sale: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def get_sales_by_seller(seller_id):
        db = get_db()
        try:
            sales = db.query(Sale).filter(Sale.seller_id == uuid.UUID(seller_id)).all()
            return sales
        except Exception as e:
            print(f"\nError fetching sales by seller: {e}")
            return []
        finally:
            close_db(db)

    @staticmethod
    def get_sales_by_customer(customer_id):
        db = get_db()
        try:
            sales = db.query(Sale).filter(Sale.customer_id == uuid.UUID(customer_id)).all()
            return sales
        except Exception as e:
            print(f"\nError fetching sales by customer: {e}")
            return []
        finally:
            close_db(db)

    @staticmethod
    def delete_sale(sale_id):
        db = get_db()
        try:
            sale = db.query(Sale).filter(Sale.id == sale_id).first()
            if not sale:
                print("\nSale not found!")
                return False

            car = db.query(Car).filter(Car.id == sale.car_id).first()
            if car:
                car.status = 'available'

            db.delete(sale)
            db.commit()
            print("\nSale deleted successfully!")
            print("Car status reverted to 'available'")
            return True
        except Exception as e:
            db.rollback()
            print(f"\nError deleting sale: {e}")
            return False
        finally:
            close_db(db)

    @staticmethod
    def get_total_sales_revenue():
        db = get_db()
        try:
            total = db.query(Sale).with_entities(db.func.sum(Sale.sale_price)).scalar()
            return float(total) if total else 0.0
        except Exception as e:
            print(f"\nError calculating total revenue: {e}")
            return 0.0
        finally:
            close_db(db)

    @staticmethod
    def display_sales(sales):
        if not sales:
            print("\nNo sales found.")
            return

        print("\n" + "="*120)
        print(f"{'ID':<38} {'Car ID':<38} {'Customer ID':<38} {'Price':<12}")
        print("="*120)
        for sale in sales:
            print(f"{str(sale.id):<38} {str(sale.car_id):<38} {str(sale.customer_id):<38} ${float(sale.sale_price):<11.2f}")
        print("="*120)

    @staticmethod
    def display_sale_details(sale):
        if not sale:
            print("\nSale not found.")
            return

        db = get_db()
        try:
            car = db.query(Car).filter(Car.id == sale.car_id).first()
            car_info = f"{car.make} {car.model} ({car.year})" if car else "Unknown"

            print("\n" + "="*80)
            print("SALE DETAILS")
            print("="*80)
            print(f"Sale ID:       {sale.id}")
            print(f"Car:           {car_info}")
            print(f"Sale Price:    ${float(sale.sale_price):,.2f}")
            print(f"Sale Date:     {sale.sale_date}")
            print("="*80)
        finally:
            close_db(db)
