import pandas as pd
import json

# add to sys.path so we can import getFilePaths
import sys
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")

import getFilePaths as gfp

# load session map from json file as dictionary
with open("sessionMap.json", "r") as file:
    session_map = json.load(file)



# given filepath to csv, session_map, find "Session" column, map it, save new csv as same filepath 
def map_session(csv_path, session_map):
    # read csv
    df = pd.read_csv(csv_path)

    # first delete "sessionnum" column if it exists
    if "sessionnum" in df.columns:
        df = df.drop(columns=["sessionnum"])
        df.to_csv(csv_path, index=False)
        
    if "Session" in df.columns:
        # map "Session" column
        df["sessionnum"] = df["Session"].map(session_map)
        # save new csv
        df.to_csv(csv_path, index=False)
    elif "session" in df.columns:
        # map "Session" column
        df["sessionnum"] = df["session"].map(session_map)
        # save new csv
        df.to_csv(csv_path, index=False)
    
filepaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/Activity_report_trainings_cleaned.csv",
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/Activity_report_with_student_cleaned.csv", 
    "C:/Users/seanl/Documents/PearsonData/Number_of_logins_per_student/cleaned_number_of_logins.csv", 
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids_cleaned.csv"
]



def main():
    # for filepath in filepaths:
    #     map_session(filepath, session_map)

    non_cleaned_files, cleaned_files = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")

    for filepath in cleaned_files:


        map_session(filepath, session_map)

if __name__ == "__main__":
    main()
