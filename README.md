# Python Finance Backend System

## Overview
This is a Python-based backend for a finance tracking system.  
It allows users to **store, manage, and analyze financial transactions** such as income and expenses.  
The backend exposes **REST API endpoints** for CRUD operations, filtering, and analytics.

Built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

---

## Features

### User Management
- Register users with roles: `viewer`, `analyst`, `admin`
- Login authentication
- Role-based access control

### Transactions
- Create, update, delete transactions
- Transaction fields: `amount`, `type`, `category`, `note`, `date`
- Filter transactions by `type`, `category`, and `date`

### Analytics
- Total income and expenses
- Current balance
- Category-wise breakdown
- Monthly summaries

---

## Tech Stack
- **Python 3.11+**
- **FastAPI** – API framework
- **SQLAlchemy** – ORM
- **PostgreSQL** – Database
- **Pydantic** – Data validation
- **Python-dotenv** – Environment variables

---

## Installation

1. Clone the repo:

-git clone <your_repo_url>
-cd <your_project_folder>

2.Create a virtual environment:

-python -m venv venv
-source venv/bin/activate  # Linux/macOS
-venv\Scripts\activate     # Windows

3.Install dependencies:

-pip install -r requirements.txt

4.Create a .env file in the root:

-DATABASE_URL=postgresql://username:password@localhost:5432/finance

5.Run the app:

-uvicorn main:app --reload

##API Endpoints
| Endpoint      | Method | Request Body / Query Parameters                                            | Description                                                                |                      |                     |
| ------------- | ------ | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------- | ------------------- |
| `/register/`  | POST   | `{ "name": str, "email": str, "password": str, "role": "viewer             | analyst                                                                    | admin" }`            | Register a new user |
| `/login/`     | POST   | `{ "email": str, "password": str }`                                        | Login and get access                                                       |                      |                     |
| `/finance/`   | POST   | `{ "user_id": str, "amount": float, "type": "income                        | expense", "category": str, "note": str, "date": datetime }`                | Add a transaction    |                     |
| `/update/`    | PUT    | `{ "transaction_id": str, "user_id": str, "amount": float, "type": "income | expense", "category": str, "note": str, "date": datetime }`                | Update a transaction |                     |
| `/delete/`    | DELETE | `{ "transaction_id": str }`                                                | Delete a transaction                                                       |                      |                     |
| `/filtering/` | GET    | `type: str, category: str, date: datetime`                                 | Filter transactions                                                        |                      |                     |
| `/analytics/` | GET    | `user_id: str`                                                             | Get total income, expenses, balance, category breakdown, monthly summaries |                      |                     |


## **Database Schema**:

**1.Users Table**:

-id (UUID, PK)

-name (String)

-email (String, unique)

-password (String, hashed)

-role (String)

-created_at (DateTime)



**2.Transactions Table**:

-id (UUID, PK)

-user_id (UUID, FK to Users)

-amount (Float)

-type (String: income/expense)

-category (String)

-note (String, optional)

-date (DateTime)

-created_at (DateTime)


**Notes**:

-All passwords are hashed using bcrypt.

-The application uses UUIDs for primary keys.

-This (.env) file should never be pushed to GitHub.
 
-Designed for assessment purposes; not production-ready.
