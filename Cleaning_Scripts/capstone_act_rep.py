import sys
import pandas as pd
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics")
import generalCleaning as gl
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")
import getFilePaths as gfp

capstone_act_rep = "C:/Users/seanl/Documents/PearsonData/working_data/capstone_activity_report/capstone_ac_rep_cleaned.csv"

if __name__ == "__main__":
    
    df = pd.read_csv(capstone_act_rep)

    # acitivty_name column looks like this: Access Chapter 10 Capstone Assessment - Drivers (PC only). Parse out the chapter number into new column
    df["chapter_number"] = df["activity_name"].str.extract(r"(\d+)")
    
    df.to_csv(capstone_act_rep, index=False)

    pass