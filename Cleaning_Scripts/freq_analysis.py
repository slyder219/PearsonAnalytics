import sys
import pandas as pd
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics")
import generalCleaning as gl
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")
import getFilePaths as gfp
import re 


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



if __name__ == "__main__":    

    freq_report_cleaned = gfp.get_filepath_list_by_keyword("freq, report", clean = True)[0]

    df = pd.read_csv(freq_report_cleaned)

    # df["ChapterNumber"] = df["Training"].str.extract(r"(\d+)")
    
    df["SubChapter"] = df["QuestionTitle"].apply(lambda x: getNumbers(x, "subchapter"))
    df["QuestionNumber"] = df["QuestionTitle"].apply(lambda x: getNumbers(x, "question"))




    df.to_csv(freq_report_cleaned, index=False)
