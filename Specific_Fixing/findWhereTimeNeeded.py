import pandas as pd
import json 
from datetime import datetime
from datetime import timedelta
# add to sys.path so we can import getFilePaths
import sys
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")
import getFilePaths as gfp

def time_to_seconds(time_input):
    # Check if the input is a timedelta object
    if isinstance(time_input, timedelta):
        # Directly convert timedelta to total seconds
        total_seconds = time_input.total_seconds()
        return total_seconds
    else:
        # If not a timedelta, try to parse it as a string (original logic)
        try:
            time_str = time_input.strip()  # Strip leading/trailing whitespace
            time_obj = datetime.strptime(time_str, "%H:%M:%S")
            total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
            return total_seconds
        except:
            total_seconds = 0
    try:
        # Assuming time_input might be a string representation of timedelta
        if isinstance(time_input, str):
            # Extract hours, minutes, and seconds from the string
            h, m, s = map(int, time_input.split(' days ')[1].split(':'))
            time_delta = timedelta(hours=h, minutes=m, seconds=s)
            return time_delta.total_seconds()
    except Exception as e:
        total_seconds = 0

    
    return total_seconds

def time_bool(value):
    try:
        output = time_to_seconds(value)
        if isinstance(output, int) and output != 0:
            return True
        else:
            return False
    except Exception as e:
        return False 


def main(csvFilePath, outputFilePath = None):

    df = pd.read_csv(csvFilePath)

    # check if a column with "seconds" aready exists
    for column in df.columns:
        if "seconds" in column.lower():
            print(f"ERROR: \nSeconds column already exists in filename {csvFilePath}\nSkipping File\n'Seconds' in column, {column}\n")
            return
    
    columnFound = False
    for column in df.columns:

        validCount = df[column].dropna().apply(time_bool).sum()

        if validCount >= 0.50 * len(df[column].dropna()):

            print(
                f"Valid count achieved for column {column} in file {csvFilePath}\n"
            )
            columnFound = True 

            new_name = column + "Seconds"
            df[new_name] = df[column].apply(time_to_seconds)
            break
    
    if not columnFound:
        print(f"ERROR: \nNo suitable column found in filename {csvFilePath}\n")
        return

    if not outputFilePath:
        outputFilePath = csvFilePath
    df.to_csv(outputFilePath, index=False)








    

if __name__ == "__main__":
    
    non_cleaned_files, cleaned_files = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")

    for file in cleaned_files:
        main(file)