import generalCleaning as gl

# add to sys.path so we can import getFilePaths
import sys
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")

import getFilePaths as gfp





def main():

    # get file paths
    non_cleaned_files, cleaned_files = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")
    

    # gl.fixNulls(cleaned_files)

    gl.addSecondsColumn(
        gfp.get_filepath_list_by_keyword("training, report, act", clean = True)[0],
        "ActivityLevelAverageTimeonTask"

    )


    pass


if __name__ == "__main__":
    main()
    
