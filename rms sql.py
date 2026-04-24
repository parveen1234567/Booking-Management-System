import mysql.connector as a

# Use 'password' instead of 'passwd'
con = a.connect(
    host="localhost",
    user="root",
    password="Parveen@1234"
)

c = con.cursor()

c.execute("CREATE DATABASE IF NOT EXISTS rms")
c.execute("USE rms")

c.execute("""CREATE TABLE IF NOT EXISTS checkin (
    days VARCHAR(50),
    names VARCHAR(20),
    aadhaar VARCHAR(20),
    date VARCHAR(20),
    typenumber VARCHAR(20)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS checkout (
    typenumber VARCHAR(20),
    guests INT,
    fare INT,
    days INT,
    tbill INT,
    date VARCHAR(20)
)""")

con.commit()
print("Database and tables created successfully!")
