import pandas as pd
import json

# add to sys.path so we can import getFilePaths
import sys
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")

import getFilePaths as gfp


# given csv with two column, create json map 
def create_session_map(csv_path, json_path):
    # read csv
    df = pd.read_csv(csv_path)

    # create map
    session_map = dict(zip(df["studentnum"], df["sessionnum"]))

    # save map as json
    with open(json_path, "w") as file:
        json.dump(session_map, file)

    return session_map


def map_session(csv_path, session_map):
    # read csv
    df = pd.read_csv(csv_path)

    # first delete "sessionnum" column if it exists
    if "sessionnum" in df.columns:
        df = df.drop(columns=["sessionnum"])
        df.to_csv(csv_path, index=False)
        
    if "studentnum" in df.columns:
        # map "session" column
        df["sessionnum"] = df["studentnum"].map(session_map)
        # save new csv
        df.to_csv(csv_path, index=False)





if __name__ == "__main__":    

    student_session_csv = "C:/Users/seanl/Documents/PearsonData/outputs/SQL_Outputs/studentnum_sessionnum_KEY.csv"

    logins = "C:/Users/seanl/Documents/PearsonData/working_data/student_logins/student_logins_cleaned.csv"

    session_map = create_session_map(student_session_csv, "studentToSession.json")

    # with open("studentToSession.json", "r") as file:
    #     session_map = json.load(file)

    map_session(logins, session_map)