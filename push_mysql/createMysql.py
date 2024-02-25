import os
import csv
import mysql.connector
import sys
import pandas as pd
import sys
import os
import csv
import mysql.connector

sys.path.append(r'C:/Users/seanl/Documents/tempSysPath')

from password import password

# Function to infer data types from CSV columns
def infer_data_types(csv_file, cursor):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        sample_data = next(csv_reader)  # Read the first row to infer data types
        studentnum_index = None
        data_types = []
        for i, value in enumerate(sample_data):
            if value.lower() == "studentnum":
                studentnum_index = i
            # Infer data type based on the value
            try:
                int(value)
                data_types.append('INT')  # Treat as integer
            except ValueError:
                try:
                    float(value)
                    data_types.append('FLOAT')  # If value can be converted to float, it's a float
                except ValueError:
                    data_types.append('VARCHAR(255)')  # If value is neither int nor float, treat as string
        return data_types



# Function to drop all tables in the database
def drop_all_tables(cursor):
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for table in tables:
        cursor.execute(f"DROP TABLE {table[0]}")



# Create the 'pearson' database if it doesn't exist
# cursor.execute("CREATE DATABASE IF NOT EXISTS pearson")

def create_table(csv_path, table_name, cursor, conn):
    col_data_types = infer_data_types(csv_path, cursor)
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # First row has headers
        columns = ', '.join([f'`{header}` {data_type}' for header, data_type in zip(headers, col_data_types)])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        cursor.execute(create_table_query)
        conn.commit()

        # Insert data into table
        for row in csv_reader:
            placeholders = ', '.join(['%s'] * len(row))
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(insert_query, row)
            conn.commit()

# List of all file paths to add to the database
filepaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/Activity_report_trainings_cleaned.csv",
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/Activity_report_with_student_cleaned.csv", 
    "C:/Users/seanl/Documents/PearsonData/Number_of_logins_per_student/cleaned_number_of_logins.csv", 
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids_cleaned.csv"
]

def main():
        # Connect to MySQL and create a database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database = "pearson"
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

        # Drop all tables in the database
    drop_all_tables(cursor)

    # Commit the changes
    conn.commit()

    # Iterate over CSV files and create tables
    for filepath in filepaths:
        table_name = os.path.splitext(os.path.basename(filepath))[0]  # Use file name as table name
        create_table(filepath, table_name, cursor, conn)

    # Close cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()