import pandas as pd
import sys
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")
import getFilePaths as gfp


# given list of filepaths, for each, print all columns 
def findDuplicateColumns(filepaths):
    for filepath in filepaths:
        df = pd.read_csv(filepath)
        print(filepath)
        for column in df.columns:
            print(column)
        print("\n")

if __name__ == "__main__":
    non_cleaned_files, cleaned_files = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")
    cleaned_files.append("C:/Users/seanl/Documents/PearsonData/working_data/student_logins/student_logins.csv")
    findDuplicateColumns(cleaned_files)