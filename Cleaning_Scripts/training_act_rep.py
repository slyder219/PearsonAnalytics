import sys
import pandas as pd
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics")
import generalCleaning as gl
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")
import getFilePaths as gfp

training_act_rep = "C:/Users/seanl/Documents/PearsonData/working_data/training_activity_report/training_act_rep_cleaned.csv"

if __name__ == "__main__":
    
    df = pd.read_csv(training_act_rep)

    df["activity_lvl_avg_score"] = [float(val) * 100 for val in df["activity_lvl_avg_score"]]
    df['score'] = [float(val) * 100 for val in df['score']]


    pass