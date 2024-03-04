import sys
import pandas as pd
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics")
import generalCleaning as gl
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")
import getFilePaths as gfp

main_students = "C:/Users/seanl/Documents/PearsonData/working_data/main_students/main_students_cleaned.csv"

if __name__ == "__main__":

    df = pd.read_csv(main_students)

    df['junior'] = df['level'].apply(lambda x: 1 if "junior" in x.lower() else 0)
    df['senior'] = df['level'].apply(lambda x: 1 if "senior" in x.lower() else 0)
    df['sophomore'] = df['level'].apply(lambda x: 1 if "sophomore" in x.lower() else 0)



    df.to_csv(main_students, index=False)

    pass 