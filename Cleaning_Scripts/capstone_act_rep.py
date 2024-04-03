import sys
import pandas as pd
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics")
import generalCleaning as gl
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")
import getFilePaths as gfp

def hwOrAs(filepath):
    df = pd.read_csv(filepath)

    df["IsAssessment"] = df["Type"].apply(lambda x: 0 if "homework" in x.lower() else 1)

    df.to_csv(filepath, index=False)

    pass


if __name__ == "__main__":

    nonClean, clean = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")

    capstone = gfp.get_filepath_list_by_keyword("capstone, act, rep", clean = True)[0]
    
    # df = pd.read_csv(capstone)

    # # acitivty_name column looks like this: Access Chapter 10 Capstone Assessment - Drivers (PC only). Parse out the chapter number into new column
    # df["ChapterNumber"] = df["ActivityName"].str.extract(r"(\d+)")
    
    # df.to_csv(capstone, index=False)

    # pass

    hwOrAs(capstone)