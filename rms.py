import mysql.connector as a
con = a.connect(host="localhost",user="root",passwd="Parveen@1234",database="rms")
def checkin():
    d = input("Days:")
    g = input("Names:")
    a = input("Aadhaar:")
    dt = input("Date:")
    b = input("Type & Number:")
    data = (d,g,a,dt,b)
    sql = 'insert into checkin values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    main()

def checkout():
    b = input("Type & Number:")
    tg = int(input("Guests:"))
    f = int(input("Fare:"))
    d = int(input("Days:"))
    bl = f*d*tg
    cod = input("Date:")
    data = (b,tg,f,d,bl,cod)
    sql = 'insert into checkout values(%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    main()

def rooms():
    print("Executive - 5000/d/g")
    print(" ")
    print(""" Facilities -Wifi,TV,AC,Bathroom With  Tub and Geyser,Breakfast,Lunch,Dinner""")
    print(" ")
    print("Deluxe - 2500/d/g")
    print(" ")
    print("""Facilities - Wifi,TV,AC,BAthroom with Tub and Geyser""")
    print(" ") 
    print("Simple - 1000/d/g")
    print(" ")
    print("""Facilities - Wifi, TV,Bathroom With Geyser""")
    main()

def main():
    print("!.Check In")
    print("2.Check Out")
    print("3. Fare and Amenities")
    c = int(input("Choice: "))
    if c == 1:
        checkin()
    elif c == 2:
        checkout()
    elif c == 3:
        rooms()
    else:
        print("Enter Correct Choice:")
    main() 
main()
    