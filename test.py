import sys
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")

import getFilePaths as gfp

non_cleaned_files, cleaned_files = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")
    
cleaned_files.append("C:/Users/seanl/Documents/PearsonData/working_data/student_logins/student_logins.csv")

for filepath in cleaned_files:
    print(filepath)

