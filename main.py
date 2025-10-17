#!/usr/bin/env python3

from sellers import SellerManager
from cars import CarManager
from customers import CustomerManager
from sales import SaleManager
from payments import PaymentManager
import sys

def print_main_menu():
    print("\n" + "="*60)
    print("        CAR MANAGEMENT SYSTEM")
    print("="*60)
    print("1.  Seller Management")
    print("2.  Car Management")
    print("3.  Customer Management")
    print("4.  Sales Management")
    print("5.  Payment Management")
    print("6.  Reports & Analytics")
    print("0.  Exit")
    print("="*60)

def seller_menu():
    while True:
        print("\n" + "="*60)
        print("        SELLER MANAGEMENT")
        print("="*60)
        print("1. Add New Seller")
        print("2. View All Sellers")
        print("3. View Seller by ID")
        print("4. Update Seller")
        print("5. Delete Seller")
        print("0. Back to Main Menu")
        print("="*60)

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            name = input("Enter seller name: ").strip()
            email = input("Enter seller email: ").strip()
            phone = input("Enter seller phone: ").strip()
            commission = input("Enter commission rate (0-100): ").strip()
            try:
                SellerManager.create_seller(name, email, phone, float(commission))
            except ValueError:
                print("\nInvalid commission rate!")

        elif choice == '2':
            sellers = SellerManager.get_all_sellers()
            SellerManager.display_sellers(sellers)

        elif choice == '3':
            seller_id = input("Enter seller ID: ").strip()
            seller = SellerManager.get_seller_by_id(seller_id)
            if seller:
                SellerManager.display_sellers([seller])
            else:
                print("\nSeller not found!")

        elif choice == '4':
            seller_id = input("Enter seller ID to update: ").strip()
            print("\nLeave blank to keep current value")
            name = input("Enter new name (or press Enter): ").strip() or None
            email = input("Enter new email (or press Enter): ").strip() or None
            phone = input("Enter new phone (or press Enter): ").strip() or None
            commission = input("Enter new commission rate (or press Enter): ").strip()
            commission = float(commission) if commission else None
            SellerManager.update_seller(seller_id, name, email, phone, commission)

        elif choice == '5':
            seller_id = input("Enter seller ID to delete: ").strip()
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == 'yes':
                SellerManager.delete_seller(seller_id)

        elif choice == '0':
            break
        else:
            print("\nInvalid choice! Please try again.")

def car_menu():
    while True:
        print("\n" + "="*60)
        print("        CAR MANAGEMENT")
        print("="*60)
        print("1. Add New Car")
        print("2. View All Cars")
        print("3. View Available Cars")
        print("4. View Car by ID")
        print("5. Update Car")
        print("6. Delete Car")
        print("7. Mark Car as Sold")
        print("0. Back to Main Menu")
        print("="*60)

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            make = input("Enter car make: ").strip()
            model = input("Enter car model: ").strip()
            year = input("Enter year: ").strip()
            color = input("Enter color: ").strip()
            price = input("Enter price: ").strip()
            mileage = input("Enter mileage (or press Enter for 0): ").strip() or "0"
            condition = input("Enter condition (new/used/certified): ").strip() or "used"
            status = input("Enter status (available/sold/reserved): ").strip() or "available"
            seller_id = input("Enter seller ID (or press Enter to skip): ").strip() or None

            try:
                CarManager.create_car(make, model, int(year), color, float(price),
                                     int(mileage), condition, status, seller_id)
            except ValueError:
                print("\nInvalid input! Please check year, price, and mileage.")

        elif choice == '2':
            cars = CarManager.get_all_cars()
            CarManager.display_cars(cars)

        elif choice == '3':
            cars = CarManager.get_available_cars()
            CarManager.display_cars(cars)

        elif choice == '4':
            car_id = input("Enter car ID: ").strip()
            car = CarManager.get_car_by_id(car_id)
            if car:
                CarManager.display_cars([car])
            else:
                print("\nCar not found!")

        elif choice == '5':
            car_id = input("Enter car ID to update: ").strip()
            print("\nLeave blank to keep current value")
            make = input("Enter new make (or press Enter): ").strip() or None
            model = input("Enter new model (or press Enter): ").strip() or None
            year = input("Enter new year (or press Enter): ").strip()
            year = int(year) if year else None
            color = input("Enter new color (or press Enter): ").strip() or None
            price = input("Enter new price (or press Enter): ").strip()
            price = float(price) if price else None
            mileage = input("Enter new mileage (or press Enter): ").strip()
            mileage = int(mileage) if mileage else None
            condition = input("Enter new condition (or press Enter): ").strip() or None
            status = input("Enter new status (or press Enter): ").strip() or None

            CarManager.update_car(car_id, make, model, year, color, price,
                                 mileage, condition, status)

        elif choice == '6':
            car_id = input("Enter car ID to delete: ").strip()
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == 'yes':
                CarManager.delete_car(car_id)

        elif choice == '7':
            car_id = input("Enter car ID to mark as sold: ").strip()
            CarManager.mark_as_sold(car_id)

        elif choice == '0':
            break
        else:
            print("\nInvalid choice! Please try again.")

def customer_menu():
    while True:
        print("\n" + "="*60)
        print("        CUSTOMER MANAGEMENT")
        print("="*60)
        print("1. Add New Customer")
        print("2. View All Customers")
        print("3. View Customer by ID")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("0. Back to Main Menu")
        print("="*60)

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            name = input("Enter customer name: ").strip()
            email = input("Enter customer email: ").strip()
            phone = input("Enter customer phone: ").strip()
            address = input("Enter customer address (or press Enter): ").strip() or None
            CustomerManager.create_customer(name, email, phone, address)

        elif choice == '2':
            customers = CustomerManager.get_all_customers()
            CustomerManager.display_customers(customers)

        elif choice == '3':
            customer_id = input("Enter customer ID: ").strip()
            customer = CustomerManager.get_customer_by_id(customer_id)
            if customer:
                CustomerManager.display_customers([customer])
            else:
                print("\nCustomer not found!")

        elif choice == '4':
            customer_id = input("Enter customer ID to update: ").strip()
            print("\nLeave blank to keep current value")
            name = input("Enter new name (or press Enter): ").strip() or None
            email = input("Enter new email (or press Enter): ").strip() or None
            phone = input("Enter new phone (or press Enter): ").strip() or None
            address = input("Enter new address (or press Enter): ").strip() or None
            CustomerManager.update_customer(customer_id, name, email, phone, address)

        elif choice == '5':
            customer_id = input("Enter customer ID to delete: ").strip()
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == 'yes':
                CustomerManager.delete_customer(customer_id)

        elif choice == '0':
            break
        else:
            print("\nInvalid choice! Please try again.")

def sales_menu():
    while True:
        print("\n" + "="*60)
        print("        SALES MANAGEMENT")
        print("="*60)
        print("1. Create New Sale")
        print("2. View All Sales")
        print("3. View Sale by ID")
        print("4. View Sales by Seller")
        print("5. View Sales by Customer")
        print("6. Delete Sale")
        print("0. Back to Main Menu")
        print("="*60)

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            print("\nFirst, let's see available cars:")
            cars = CarManager.get_available_cars()
            CarManager.display_cars(cars)

            car_id = input("\nEnter car ID: ").strip()
            customer_id = input("Enter customer ID: ").strip()
            seller_id = input("Enter seller ID: ").strip()
            sale_price = input("Enter sale price: ").strip()

            try:
                SaleManager.create_sale(car_id, customer_id, seller_id, float(sale_price))
            except ValueError:
                print("\nInvalid sale price!")

        elif choice == '2':
            sales = SaleManager.get_all_sales()
            SaleManager.display_sales(sales)

        elif choice == '3':
            sale_id = input("Enter sale ID: ").strip()
            sale = SaleManager.get_sale_by_id(sale_id)
            if sale:
                SaleManager.display_sale_details(sale)
            else:
                print("\nSale not found!")

        elif choice == '4':
            seller_id = input("Enter seller ID: ").strip()
            sales = SaleManager.get_sales_by_seller(seller_id)
            SaleManager.display_sales(sales)

        elif choice == '5':
            customer_id = input("Enter customer ID: ").strip()
            sales = SaleManager.get_sales_by_customer(customer_id)
            SaleManager.display_sales(sales)

        elif choice == '6':
            sale_id = input("Enter sale ID to delete: ").strip()
            confirm = input("Are you sure? This will revert the car to available. (yes/no): ").strip().lower()
            if confirm == 'yes':
                SaleManager.delete_sale(sale_id)

        elif choice == '0':
            break
        else:
            print("\nInvalid choice! Please try again.")

def payment_menu():
    while True:
        print("\n" + "="*60)
        print("        PAYMENT MANAGEMENT")
        print("="*60)
        print("1. Create New Payment")
        print("2. View All Payments")
        print("3. View Payment by ID")
        print("4. View Payments by Sale")
        print("5. Update Payment Status")
        print("6. Delete Payment")
        print("0. Back to Main Menu")
        print("="*60)

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            sale_id = input("Enter sale ID: ").strip()
            amount = input("Enter payment amount: ").strip()
            payment_method = input("Enter payment method (cash/credit/bank_transfer/debit): ").strip()
            status = input("Enter status (pending/completed/failed): ").strip() or "pending"

            try:
                PaymentManager.create_payment(sale_id, float(amount), payment_method, status)
            except ValueError:
                print("\nInvalid payment amount!")

        elif choice == '2':
            payments = PaymentManager.get_all_payments()
            PaymentManager.display_payments(payments)

        elif choice == '3':
            payment_id = input("Enter payment ID: ").strip()
            payment = PaymentManager.get_payment_by_id(payment_id)
            if payment:
                PaymentManager.display_payment_details(payment)
            else:
                print("\nPayment not found!")

        elif choice == '4':
            sale_id = input("Enter sale ID: ").strip()
            payments = PaymentManager.get_payments_by_sale(sale_id)
            PaymentManager.display_payments(payments)
            total = PaymentManager.get_total_payments_for_sale(sale_id)
            print(f"\nTotal Completed Payments: ${total:,.2f}")

        elif choice == '5':
            payment_id = input("Enter payment ID: ").strip()
            status = input("Enter new status (pending/completed/failed): ").strip()
            PaymentManager.update_payment_status(payment_id, status)

        elif choice == '6':
            payment_id = input("Enter payment ID to delete: ").strip()
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == 'yes':
                PaymentManager.delete_payment(payment_id)

        elif choice == '0':
            break
        else:
            print("\nInvalid choice! Please try again.")

def reports_menu():
    while True:
        print("\n" + "="*60)
        print("        REPORTS & ANALYTICS")
        print("="*60)
        print("1. Total Sales Revenue")
        print("2. Available Cars Count")
        print("3. Sold Cars Count")
        print("4. Total Customers")
        print("5. Total Sellers")
        print("0. Back to Main Menu")
        print("="*60)

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            total = SaleManager.get_total_sales_revenue()
            print(f"\nTotal Sales Revenue: ${total:,.2f}")

        elif choice == '2':
            cars = CarManager.get_available_cars()
            print(f"\nAvailable Cars: {len(cars)}")

        elif choice == '3':
            all_cars = CarManager.get_all_cars()
            sold_cars = [car for car in all_cars if car.status == 'sold']
            print(f"\nSold Cars: {len(sold_cars)}")

        elif choice == '4':
            customers = CustomerManager.get_all_customers()
            print(f"\nTotal Customers: {len(customers)}")

        elif choice == '5':
            sellers = SellerManager.get_all_sellers()
            print(f"\nTotal Sellers: {len(sellers)}")

        elif choice == '0':
            break
        else:
            print("\nInvalid choice! Please try again.")

def main():
    print("\n")
    print("="*60)
    print("   WELCOME TO CAR MANAGEMENT SYSTEM")
    print("="*60)

    while True:
        print_main_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            seller_menu()
        elif choice == '2':
            car_menu()
        elif choice == '3':
            customer_menu()
        elif choice == '4':
            sales_menu()
        elif choice == '5':
            payment_menu()
        elif choice == '6':
            reports_menu()
        elif choice == '0':
            print("\nThank you for using Car Management System!")
            print("Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)
