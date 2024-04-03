import sys
import pandas as pd
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics")
import generalCleaning as gl
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")
import getFilePaths as gfp


if __name__ == "__main__":
    
    nonClean, clean = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")

    training = gfp.get_filepath_list_by_keyword("training, act, rep", clean = True)[0]

    df = pd.read_csv(training)
    
    df["ChapterNumber"] = df["ActivityName"].str.extract(r"(\d+)")


    #save
    df.to_csv(training, index=False)

