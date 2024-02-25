import os
import csv
import mysql.connector
import sys
import pandas as pd
sys.path.append(r'C:/Users/seanl/Documents/tempSysPath')

from password import password

filepaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/activity_report_trainings_cleaned.csv",
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/activity_report_with_student_cleaned.csv", 
    "C:/Users/seanl/Documents/PearsonData/Number_of_logins_per_student/cleaned_number_of_logins.csv", 
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids_cleaned.csv"
]

def get_table_name_from_path(csvPath):
    return os.path.splitext(os.path.basename(csvPath))[0]

def get_table_names_from_db(cursor):
    cursor.execute("SHOW TABLES")
    table_names = cursor.fetchall()
    return [table[0].lower() for table in table_names]

def export_table_from_db(table_name, csv_filepathname, conn, cursor):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    headers = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    with open(csv_filepathname, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(rows)



def main():
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database = "pearson"
    )

    cursor = conn.cursor()

    for file in filepaths:
        table_name = get_table_name_from_path(file).lower()
        if table_name in get_table_names_from_db(cursor):
            export_table_from_db(table_name, file, conn, cursor)
            print(f"Exported {table_name}")

    cursor.close()
    conn.close()

if __name__ == "__main__": 
    main()