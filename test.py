import sys
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")

import getFilePaths as gfp

non_cleaned_files, cleaned_files = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")
    
# cleaned_files.append("C:/Users/seanl/Documents/PearsonData/working_data/student_logins/student_logins.csv")

# for filepath in non_cleaned_files:
#     print(filepath)

# print(

#     gfp.get_filepath_list_by_keyword("number, logins, student", clean = False)[0]
# )

for file in cleaned_files:
    print(file)