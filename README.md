# Booking Management System

A Python + MySQL based project to manage hotel/room bookings.  
This system allows check-in, check-out, fare calculation, and amenities tracking with a simple command-line interface.

---

## 🚀 Features
- **Check-In**: Record guest details with Aadhaar, room type & number, and stay duration.
- **Check-Out**: Calculate total bill based on fare and days stayed.
- **Fare & Amenities**: Display room fare and available amenities.
- **Database Integration**: Uses MySQL for persistent storage of guest and booking data.

---

## 🛠️ Tech Stack
- **Language**: Python 3.11
- **Database**: MySQL
- **Connector**: `mysql-connector-python`

---

## 📂 Database Schema
### Database: `rms`
- **Table: checkin**
  - `days` (VARCHAR)
  - `names` (VARCHAR)
  - `aadhaar` (VARCHAR)
  - `date` (VARCHAR)
  - `typenumber` (VARCHAR)

- **Table: checkout**
  - `typenumber` (VARCHAR)
  - `guests` (INT)
  - `fare` (INT)
  - `days` (INT)
  - `tbill` (INT)
  - `date` (VARCHAR)

---

## ⚙️ Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/parveen1234567/Booking-Management-System.git
   cd Booking-Management-System
Install dependencies

bash
pip install mysql-connector-python
Configure MySQL

Ensure MySQL server is running.

Update your connection credentials in rms_sql.py:

python
con = a.connect(host="localhost", user="root", password="Parveen@1234")
Run the project

bash
python rms.py
📸 Demo
Menu Options:

Check-In

Check-Out

Fare and Amenities

Example interaction:

Code:

Choice: 1

Type & Number: F20

Name: Bhavana

Aadhaar: 123456789012

Days: 3

Date: 24-04-2026

📌 Notes

-Enter numbers for guest count (e.g., 2), not names, to avoid errors.

-Use Guest Name field separately if you want to store names.

Links:
LinkedIn (linkedin.com in Bing)

GitHub (github.com in Bing)






