import os
import csv
import mysql.connector
import sys
import pandas as pd
from createMysql import infer_data_types 
sys.path.append(r'C:/Users/seanl/Documents/tempSysPath')

from password import password

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

def get_table_name(csvPath):
    return os.path.splitext(os.path.basename(csvPath))[0]

# given path to csv, drop associated table from database if it exists
def drop_table(csvPath, cursor):
    tableName = get_table_name(csvPath)
    cursor.execute(f"DROP TABLE IF EXISTS {tableName}")


filepaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/Activity_report_trainings_cleaned.csv",
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/Activity_report_with_student_cleaned.csv", 
    "C:/Users/seanl/Documents/PearsonData/Number_of_logins_per_student/cleaned_number_of_logins.csv", 
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids_cleaned.csv"
]

# def create_table(csv_path, table_name, cursor, conn):

def main():
    
    # table we want to update:
    csvTablePath = filepaths[3]

    # table name:
    tableName = get_table_name(csvTablePath)

    # connect 
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database = "pearson"
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # drop table
    drop_table(csvTablePath, cursor)

    conn.commit()

    # create table
    create_table(csvTablePath, tableName, cursor, conn)

    # Close cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()