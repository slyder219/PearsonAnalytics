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

import sys
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")
import getFilePaths as gfp

# Function to infer data types from CSV columns
def infer_data_types(csv_file, cursor):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Read the first row as headers
        sample_data = next(csv_reader)  # Read the second row to infer data types
        studentnum_index = None
        data_types = []
        for i, value in enumerate(sample_data):
            if headers[i].lower() == "studentnum":
                studentnum_index = i
            # Infer data type based on the value
            try:
                float(value)
                data_types.append('FLOAT')  # Treat as float
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
    # Treat all 'INT' data types as 'FLOAT'
    col_data_types = ['FLOAT' if data_type == 'INT' else data_type for data_type in col_data_types]
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # First row has headers
        columns = ', '.join([f'`{header}` {data_type}' for header, data_type in zip(headers, col_data_types)])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        cursor.execute(create_table_query)
        conn.commit()

        # Insert data into table
        for row in csv_reader:
            sanitized_row = []
            for value, data_type in zip(row, col_data_types):
                try:
                    if data_type == 'FLOAT':
                        sanitized_value = value.strip() if value != '' and value != "--" else None
                    else:
                        sanitized_value = value
                except ValueError:
                    sanitized_value = None
                sanitized_row.append(sanitized_value)
            placeholders = ', '.join(['%s'] * len(sanitized_row))
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(insert_query, sanitized_row)
            conn.commit()

# List of all file paths to add to the database
filepaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/activity_report_trainings_cleaned.csv",
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/activity_report_with_student_cleaned.csv", 
    "C:/Users/seanl/Documents/PearsonData/Number_of_logins_per_student/cleaned_number_of_logins.csv", 
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids_cleaned.csv",
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids.csv"
]

def main():
    
    uncleaned_files, cleaned_files = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")

    cleaned_files.append("C:/Users/seanl/Documents/PearsonData/working_data/main_students/main_students.csv")

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
    for filepath in cleaned_files:
        table_name = os.path.splitext(os.path.basename(filepath))[0]  # Use file name as table name
        create_table(filepath, table_name, cursor, conn)

    # Close cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()