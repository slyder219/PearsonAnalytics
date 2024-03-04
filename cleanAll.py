import generalCleaning as gl

# add to sys.path so we can import getFilePaths
import sys
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")

import getFilePaths as gfp

# list of all file paths to clean
filePaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/Activity_report_trainings.csv", 
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/Activity_report_with_student.csv", 
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids.csv"
]

# list of filepaths that have time columns that need seconds columns added
timeFilePaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/Activity_report_trainings_cleaned.csv", 
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/Activity_report_with_student_cleaned.csv"
]

cleanFilepaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/Activity_report_trainings_cleaned.csv",
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/Activity_report_with_student_cleaned.csv", 
    "C:/Users/seanl/Documents/PearsonData/Number_of_logins_per_student/cleaned_number_of_logins.csv", 
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids_cleaned.csv"
]

ogFilepaths = [
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids.csv",
]

freq_report = "C:/Users/seanl/Documents/PearsonData/working_data/frequency_analysis_report/freq_report.csv"
freq_report_cleaned = "C:/Users/seanl/Documents/PearsonData/working_data/frequency_analysis_report/freq_report_cleaned.csv"



def main():

    # get file paths
    non_cleaned_files, cleaned_files = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")
    

    gl.fixNulls(cleaned_files)


    pass


if __name__ == "__main__":
    main()
    
