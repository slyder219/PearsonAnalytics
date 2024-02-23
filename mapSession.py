import pandas as pd
import json

# load session map from json file as dictionary
with open("sessionMap.json", "r") as file:
    session_map = json.load(file)



# given filepath to csv, session_map, find "Session" column, map it, save new csv as same filepath 
def map_session(csv_path, session_map):
    # read csv
    df = pd.read_csv(csv_path)
    # map "Session" column
    df["SessionNum"] = df["Session"].map(session_map)
    # save new csv
    df.to_csv(csv_path, index=False)
    
filepaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/Activity_report_trainings_cleaned.csv",
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/Activity_report_with_student_cleaned.csv", 
    "C:/Users/seanl/Documents/PearsonData/Number_of_logins_per_student/cleaned_number_of_logins.csv", 
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids_cleaned.csv"
]



def main():
    for filepath in filepaths:
        map_session(filepath, session_map)

if __name__ == "__main__":
    main()
