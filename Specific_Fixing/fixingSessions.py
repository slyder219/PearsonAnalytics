import pandas as pd

filepaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/activity_report_trainings_cleaned.csv",
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/activity_report_with_student_cleaned.csv", 
    "C:/Users/seanl/Documents/PearsonData/Number_of_logins_per_student/cleaned_number_of_logins.csv", 
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids_cleaned.csv"
]

def get_session_map(sessionMapPath):
    sessionMap = pd.read_csv(sessionMapPath)
    sessionMap = sessionMap.set_index("studentnum")
    sessionMap = sessionMap.to_dict()["sessionnum"]
    return sessionMap

def map_session(csv_path, session_map):
    # read csv
    df = pd.read_csv(csv_path)
    # map "Session" column
    df["SessionNum"] = df["StudentNum"].map(session_map)
    # save new csv
    df.to_csv(csv_path, index=False)

# delete columns "sessionnum" if it exists
def delete_sessionnum(csv_path):
    df = pd.read_csv(csv_path)
    if "sessionnum" in df.columns:
        df = df.drop(columns=["sessionnum"])
        df.to_csv(csv_path, index=False)



def main():

    sessionMapPath = "C:/Users/seanl/Documents/PearsonData/SQL_Outputs/studentnum_sessionnum_KEY.csv"
    sessionMap = get_session_map(sessionMapPath)

    file = "C:/Users/seanl/Documents/PearsonData/working_data/capstone_activity_report/capstone_ac_rep_cleaned.csv"
    delete_sessionnum(file)
    map_session(file, sessionMap)
    

if __name__ == "__main__":
    main()