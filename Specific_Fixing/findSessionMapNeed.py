import pandas as pd
import json 
# add to sys.path so we can import getFilePaths
import sys
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")
import getFilePaths as gfp


def main(csvPath, jsonMapPath, outputfilepath = None):
    with open(jsonMapPath, "r") as file:
        session_map = json.load(file)

    df = pd.read_csv(csvPath)

    # check if sessionnum already exists 
    for column in df.columns:
        if "sessionnum" in column.lower():
            print(f"ERROR: \nSessionNum column already exists in filename {csvPath}")
            return 
        if "sessionnumber" in column.lower():
            print(f"ERROR: \nSessionNum column already exists in filename {csvPath}")
            return

    targetColumn = None 
    for column in df.columns:
        if df[column].notna().empty:
            continue 
        validCount = df[column].apply(lambda x: x in session_map).sum()
        if validCount >= 0.75 * len(df[column].dropna()):
            targetColumn = column 
            break

    if not targetColumn:
        print(f"ERROR: \nNo suitable column found in filename {csvPath}") 
        return 

    # add mapped column
    df["SessionNum"] = df[targetColumn].map(session_map)

    # save
    if not outputfilepath:
        outputfilepath = csvPath
    df.to_csv(outputfilepath, index=False)



if __name__ == "__main__":
    
    non_cleaned_files, cleaned_files = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")

    for file in cleaned_files: 
        main(file, "C:/Users/seanl/Documents/PearsonAnalytics/sessionMap.json")