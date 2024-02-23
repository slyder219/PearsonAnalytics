import generalCleaning as gl

# list of all file paths to clean
filePaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/Activity_report_trainings.csv", 
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/Activity_report_with_student.csv", 
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids.csv"
]




def main(filePaths):
    # clean all files
    cleanedFilePaths = gl.cleanAllFiles(filePaths)
    # rename columns
    gl.renameColumns(cleanedFilePaths)


if __name__ == "__main__":
    main(filePaths)
    
