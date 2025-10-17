# Car Management System

A comprehensive backend CLI application for managing car dealership operations, built with Python, SQLAlchemy ORM, and PostgreSQL

## Project Overview

This car management system stores and manages information about cars, sellers, customers, sales, and payments. It provides a complete solution for organizing car dealership data and can be extended for use in car selling or buying websites.

## Features

### Core Functionality
- **Seller Management**: Add, view, update, and delete sellers with commission tracking
- **Car Inventory**: Manage car listings with detailed specifications and availability status
- **Customer Management**: Store and manage customer information
- **Sales Tracking**: Record sales transactions and automatically update car status
- **Payment Processing**: Track payments for sales with multiple payment methods
- **Reports & Analytics**: Generate business insights and statistics

## Database Schema

The system uses 5 interconnected tables:

1. **sellers**: Store seller information and commission rates
2. **cars**: Manage car inventory with make, model, year, price, and status
3. **customers**: Store customer contact and address information
4. **sales**: Track sales transactions linking cars, customers, and sellers
5. **payments**: Record payment details for each sale

## Project Structure

```
project/
├── models/                 # SQLAlchemy ORM Models
│   ├── __init__.py
│   ├── seller.py
│   ├── car.py
│   ├── customer.py
│   ├── sale.py
│   └── payment.py
├── database.py            # Database connection and session management
├── sellers.py             # Seller CRUD operations
├── cars.py                # Car CRUD operations
├── customers.py           # Customer CRUD operations
├── sales.py               # Sales CRUD operations
├── payments.py            # Payment CRUD operations
├── main.py                # CLI application entry point
├── Pipfile                # Pipenv dependencies
├── requirements.txt       # pip dependencies
├── .env                   # Environment variables (Supabase credentials)
└── setup_instructions.txt # Setup guide
```

## Technologies Used

- **Python 3.7+**: Core programming language
- **SQLAlchemy**: ORM for database operations
- **PostgreSQL**: Database system (via Supabase)
- **Pipenv**: Virtual environment and dependency management
- **python-dotenv**: Environment variable management
- **psycopg2-binary**: PostgreSQL database adapter

## Installation

### Prerequisites
- Python 3.7 or higher
- Internet connection (for Supabase database)

### Setup Steps

1. **Install Pipenv** (if not already installed):
   ```bash
   pip install pipenv
   ```

2. **Install project dependencies**:
   ```bash
   pipenv install
   ```

   Or without Pipenv:
   ```bash
   pip install -r requirements.txt
   ```

3. **Activate the virtual environment** (if using Pipenv):
   ```bash
   pipenv shell
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## Usage

The application provides an interactive CLI menu system:

### Main Menu Options
1. Seller Management
2. Car Management
3. Customer Management
4. Sales Management
5. Payment Management
6. Reports & Analytics

### Example Workflow

1. **Add a Seller**:
   - Navigate to Seller Management
   - Add seller details (name, email, phone, commission rate)

2. **Add a Car**:
   - Navigate to Car Management
   - Enter car details (make, model, year, price, etc.)
   - Link to a seller

3. **Register a Customer**:
   - Navigate to Customer Management
   - Add customer information

4. **Create a Sale**:
   - Navigate to Sales Management
   - Select an available car
   - Link customer and seller
   - Enter sale price
   - System automatically marks car as sold

5. **Record Payment**:
   - Navigate to Payment Management
   - Link to sale
   - Enter payment details and method

## Key Features Implementation

### Data Relationships
- **Cars** are linked to **Sellers** (who owns the inventory)
- **Sales** connect **Cars**, **Customers**, and **Sellers**
- **Payments** are associated with **Sales**
- Cascading deletes protect data integrity

### Data Validation
- Price and commission rate validation
- Year range checks
- Email uniqueness enforcement
- Status constraints (available/sold/reserved)
- Payment method validation

### Business Logic
- Automatic car status updates when sold
- Prevention of duplicate sales for the same car
- Payment tracking per sale
- Revenue calculation and reporting

## Data Structures Used

The project demonstrates use of:
- **Lists**: For storing and displaying multiple records
- **Dictionaries**: Model `to_dict()` methods for data serialization
- **Tuples**: In database query results and function returns
- **ORM Objects**: SQLAlchemy model instances

## Database Security

- Row Level Security (RLS) enabled on all tables
- Public access policies configured for CLI usage
- UUID primary keys for better security
- Foreign key constraints maintain referential integrity

## Future Enhancements

- User authentication and authorization
- Advanced search and filtering
- Export reports to CSV/PDF
- Email notifications
- REST API for web/mobile integration
- Image upload for cars
- Advanced analytics dashboard

## Troubleshooting

### Module Not Found
- Ensure dependencies are installed: `pipenv install`
- Check Python version: `python --version`

### Database Connection Error
- Verify `.env` file contains correct Supabase credentials
- Check internet connection
- Ensure Supabase database is active

### Import Errors
- Make sure you're in the project directory
- Activate virtual environment if using Pipenv

## License

This project is created for educational purposes.

## Author

Phase 3 Project - CLI and ORM Application
