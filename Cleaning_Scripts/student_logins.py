import sys
import pandas as pd
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics")
import generalCleaning as gl
sys.path.append("C:/Users/seanl/Documents/PearsonAnalytics/Specific_Fixing")
import getFilePaths as gfp

student_logins = "C:/Users/seanl/Documents/PearsonData/working_data/student_logins/student_logins_cleaned.csv"

if __name__ == "__main__":
    
    gl.twoInstructors(student_logins)
    
    
    pass