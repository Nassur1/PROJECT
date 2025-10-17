from models.car import Car
from database import get_db, close_db
from decimal import Decimal
import uuid

class CarManager:

    @staticmethod
    def create_car(make, model, year, color, price, mileage=0, condition='used', status='available', seller_id=None):
        db = get_db()
        try:
            car = Car(
                make=make,
                model=model,
                year=year,
                color=color,
                price=Decimal(str(price)),
                mileage=mileage,
                condition=condition,
                status=status,
                seller_id=uuid.UUID(seller_id) if seller_id else None
            )
            db.add(car)
            db.commit()
            db.refresh(car)
            print(f"\nCar created successfully! ID: {car.id}")
            return car
        except Exception as e:
            db.rollback()
            print(f"\nError creating car: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def get_all_cars():
        db = get_db()
        try:
            cars = db.query(Car).all()
            return cars
        except Exception as e:
            print(f"\nError fetching cars: {e}")
            return []
        finally:
            close_db(db)

    @staticmethod
    def get_available_cars():
        db = get_db()
        try:
            cars = db.query(Car).filter(Car.status == 'available').all()
            return cars
        except Exception as e:
            print(f"\nError fetching available cars: {e}")
            return []
        finally:
            close_db(db)

    @staticmethod
    def get_car_by_id(car_id):
        db = get_db()
        try:
            car = db.query(Car).filter(Car.id == car_id).first()
            return car
        except Exception as e:
            print(f"\nError fetching car: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def update_car(car_id, make=None, model=None, year=None, color=None, price=None,
                   mileage=None, condition=None, status=None, seller_id=None):
        db = get_db()
        try:
            car = db.query(Car).filter(Car.id == car_id).first()
            if not car:
                print("\nCar not found!")
                return None

            if make:
                car.make = make
            if model:
                car.model = model
            if year:
                car.year = year
            if color:
                car.color = color
            if price is not None:
                car.price = Decimal(str(price))
            if mileage is not None:
                car.mileage = mileage
            if condition:
                car.condition = condition
            if status:
                car.status = status
            if seller_id:
                car.seller_id = uuid.UUID(seller_id)

            db.commit()
            db.refresh(car)
            print("\nCar updated successfully!")
            return car
        except Exception as e:
            db.rollback()
            print(f"\nError updating car: {e}")
            return None
        finally:
            close_db(db)

    @staticmethod
    def delete_car(car_id):
        db = get_db()
        try:
            car = db.query(Car).filter(Car.id == car_id).first()
            if not car:
                print("\nCar not found!")
                return False

            db.delete(car)
            db.commit()
            print("\nCar deleted successfully!")
            return True
        except Exception as e:
            db.rollback()
            print(f"\nError deleting car: {e}")
            return False
        finally:
            close_db(db)

    @staticmethod
    def mark_as_sold(car_id):
        db = get_db()
        try:
            car = db.query(Car).filter(Car.id == car_id).first()
            if not car:
                print("\nCar not found!")
                return False

            car.status = 'sold'
            db.commit()
            print("\nCar marked as sold!")
            return True
        except Exception as e:
            db.rollback()
            print(f"\nError marking car as sold: {e}")
            return False
        finally:
            close_db(db)

    @staticmethod
    def display_cars(cars):
        if not cars:
            print("\nNo cars found.")
            return

        print("\n" + "="*120)
        print(f"{'ID':<38} {'Make':<12} {'Model':<15} {'Year':<6} {'Color':<10} {'Price':<12} {'Status':<10}")
        print("="*120)
        for car in cars:
            print(f"{str(car.id):<38} {car.make:<12} {car.model:<15} {car.year:<6} {car.color:<10} ${float(car.price):<11.2f} {car.status:<10}")
        print("="*120)
