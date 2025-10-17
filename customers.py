from models.customer import Customer
from database import get_db, close_db

class CustomerManager:

    @staticmethod
    def create_customer(name, email, phone, address=None):
        db = get_db()
        try:
            customer = Customer(
                name=name,
                email=email,
                phone=phone,
                address=address
            )
            db.add(customer)
            db.commit()
            db.refresh(customer)
            print(f"\nCustomer created successfully! ID: {customer.id}")
            return customer
        except Exception as e:
            db.rollback()
            print(f"\nError creating customer: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def get_all_customers():
        db = get_db()
        try:
            customers = db.query(Customer).all()
            return customers
        except Exception as e:
            print(f"\nError fetching customers: {e}")
            return []
        finally:
            close_db(db)

    @staticmethod
    def get_customer_by_id(customer_id):
        db = get_db()
        try:
            customer = db.query(Customer).filter(Customer.id == customer_id).first()
            return customer
        except Exception as e:
            print(f"\nError fetching customer: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def update_customer(customer_id, name=None, email=None, phone=None, address=None):
        db = get_db()
        try:
            customer = db.query(Customer).filter(Customer.id == customer_id).first()
            if not customer:
                print("\nCustomer not found!")
                return None

            if name:
                customer.name = name
            if email:
                customer.email = email
            if phone:
                customer.phone = phone
            if address:
                customer.address = address

            db.commit()
            db.refresh(customer)
            print("\nCustomer updated successfully!")
            return customer
        except Exception as e:
            db.rollback()
            print(f"\nError updating customer: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def delete_customer(customer_id):
        db = get_db()
        try:
            customer = db.query(Customer).filter(Customer.id == customer_id).first()
            if not customer:
                print("\nCustomer not found!")
                return False

            db.delete(customer)
            db.commit()
            print("\nCustomer deleted successfully!")
            return True
        except Exception as e:
            db.rollback()
            print(f"\nError deleting customer: {e}")
            return False
        finally:
            close_db(db)

    @staticmethod
    def display_customers(customers):
        if not customers:
            print("\nNo customers found.")
            return

        print("\n" + "="*120)
        print(f"{'ID':<38} {'Name':<20} {'Email':<30} {'Phone':<15} {'Address':<17}")
        print("="*120)
        for customer in customers:
            address = customer.address if customer.address else "N/A"
            print(f"{str(customer.id):<38} {customer.name:<20} {customer.email:<30} {customer.phone:<15} {address:<17}")
        print("="*120)
