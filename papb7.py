import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ecity'
)

cursor = cnx.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS electricity_bill(
    tariffCode VARCHAR(10),
    customer_name VARCHAR(50),
    meter_number VARCHAR(50),
    previous_reading INT,
    current_reading INT
)
"""
cursor.execute(create_table_query)


def insert_bill_details(tariff_code, customer_name, meter_number, previous_reading, current_reading):
    insert_query = """
    INSERT INTO electricity_bill(tariffCode, customer_name, meter_number, previous_reading, current_reading)
    VALUES(%s, %s, %s, %s, %s)
    """
    values = (tariff_code, customer_name, meter_number, previous_reading, current_reading)
    cursor.execute(insert_query, values)
    cnx.commit()
    print("Bill details inserted successfully")


def update_customer_details(meter_number, new_customer_name):
    update_query = """
    UPDATE electricity_bill
    SET customer_name=%s
    WHERE meter_number=%s
    """
    values = (new_customer_name, meter_number)
    cursor.execute(update_query, values)
    cnx.commit()
    print("Customer details updated successfully")


def calculate_bill(meter_number):
    select_query = """
    SELECT tariffCode, current_reading, previous_reading
    FROM electricity_bill
    WHERE meter_number=%s
    """
    values = (meter_number,)
    cursor.execute(select_query, values)
    result = cursor.fetchone()
    if result is None:
        print("Meter number not found")
        return
    tariff_code = result[0]
    cr1 = result[1]
    pr1 = result[2]
    units_consumed = cr1 - pr1
    print("Current reading =", cr1)
    print("Previous reading =", pr1)
    print("Units consumed =", units_consumed)
    rate_per_unit = 0.0
    if tariff_code == "LT1":
        if units_consumed <= 30:
            rate_per_unit = 2.0
        elif units_consumed <= 100:
            rate_per_unit = 3.5
        elif units_consumed <= 200:
            rate_per_unit = 4.5
        else:
            rate_per_unit = 5.0
    elif tariff_code == "LT2":
        if units_consumed <= 30:
            rate_per_unit = 3.5
        elif units_consumed <= 100:
            rate_per_unit = 5.0
        elif units_consumed <= 200:
            rate_per_unit = 6.0
        else:
            rate_per_unit = 7.5
    else:
        print("Invalid Tariff code")
        return
    bill_amount = units_consumed * rate_per_unit
    print(f"Bill amount for Meter number {meter_number}: {bill_amount}")


name = input("Enter Customer name: ")
meter_no = input("Enter meter number: ")
p_read = int(input("Enter previous reading: "))
c_read = int(input("Enter current reading: "))
lt = input("Enter LT1 or LT2: ")

insert_bill_details(lt, name, meter_no, p_read, c_read)
update_customer_details(meter_no, name)
calculate_bill(meter_no)
