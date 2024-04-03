import sys
import re 
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")

import getFilePaths as gfp

non_cleaned_files, cleaned_files = gfp.separate_files_by_cleaned_status_v2("C:/Users/seanl/Documents/PearsonData/working_data")
    
# cleaned_files.append("C:/Users/seanl/Documents/PearsonData/working_data/student_logins/student_logins.csv")

# for filepath in non_cleaned_files:
#     print(filepath)

# print(

#     gfp.get_filepath_list_by_keyword("number, logins, student", clean = False)[0]
# )

# for file in cleaned_files:
#     print(file)

# print(

# gfp.get_filepath_list_by_keyword("training, act, rep", clean = True)[0]

# )
def getNumbers(value, chap_subchap_question = ""):
    """
    Entries in Question title look like : AC Step 1.1.1: Open, Save, and Enable Content in a Database
    Want to grab the numbers
    """
    numbers = re.findall(r'(\d+)\.(\d+)\.(\d+):', value)
    output =  [int(num) for nums in numbers for num in nums]
    chapter = output[0]
    subchap = output[1]
    question = output[2]

    if "chapter" == chap_subchap_question.lower():
        return chapter
    elif "subchapter" in chap_subchap_question.lower():
        return subchap
    elif "question" in chap_subchap_question.lower():
        return question
    else:
        return output 

print(

    getNumbers("AC Step 7.1.3: Set Tab Order Using Auto Order", "subchapter")
)


