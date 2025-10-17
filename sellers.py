from models.seller import Seller
from database import get_db, close_db
from decimal import Decimal

class SellerManager:

    @staticmethod
    def create_seller(name, email, phone, commission_rate=0.00):
        db = get_db()
        try:
            seller = Seller(
                name=name,
                email=email,
                phone=phone,
                commission_rate=Decimal(str(commission_rate))
            )
            db.add(seller)
            db.commit()
            db.refresh(seller)
            print(f"\nSeller created successfully! ID: {seller.id}")
            return seller
        except Exception as e:
            db.rollback()
            print(f"\nError creating seller: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def get_all_sellers():
        db = get_db()
        try:
            sellers = db.query(Seller).all()
            return sellers
        except Exception as e:
            print(f"\nError fetching sellers: {e}")
            return []
        finally:
            close_db(db)

    @staticmethod
    def get_seller_by_id(seller_id):
        db = get_db()
        try:
            seller = db.query(Seller).filter(Seller.id == seller_id).first()
            return seller
        except Exception as e:
            print(f"\nError fetching seller: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def update_seller(seller_id, name=None, email=None, phone=None, commission_rate=None):
        db = get_db()
        try:
            seller = db.query(Seller).filter(Seller.id == seller_id).first()
            if not seller:
                print("\nSeller not found!")
                return None

            if name:
                seller.name = name
            if email:
                seller.email = email
            if phone:
                seller.phone = phone
            if commission_rate is not None:
                seller.commission_rate = Decimal(str(commission_rate))

            db.commit()
            db.refresh(seller)
            print("\nSeller updated successfully!")
            return seller
        except Exception as e:
            db.rollback()
            print(f"\nError updating seller: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def delete_seller(seller_id):
        db = get_db()
        try:
            seller = db.query(Seller).filter(Seller.id == seller_id).first()
            if not seller:
                print("\nSeller not found!")
                return False

            db.delete(seller)
            db.commit()
            print("\nSeller deleted successfully!")
            return True
        except Exception as e:
            db.rollback()
            print(f"\nError deleting seller: {e}")
            return False
        finally:
            close_db(db)

    @staticmethod
    def display_sellers(sellers):
        if not sellers:
            print("\nNo sellers found.")
            return

        print("\n" + "="*100)
        print(f"{'ID':<38} {'Name':<20} {'Email':<25} {'Phone':<15} {'Commission %':<12}")
        print("="*100)
        for seller in sellers:
            print(f"{str(seller.id):<38} {seller.name:<20} {seller.email:<25} {seller.phone:<15} {float(seller.commission_rate):<12.2f}")
        print("="*100)
