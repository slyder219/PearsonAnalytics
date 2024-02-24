import generalCleaning as gl

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




def main():
    # clean all files
    # cleanedFilePaths = gl.cleanAllFiles(filePaths)
    # rename columns
    # gl.renameColumns(cleanedFilePaths)

    # add numerical column for letter grades to student info ids sheet
    # gl.mapGrades("C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids_cleaned.csv", "Official_Grade")

    # add second column where necessary 
    # for filePath in timeFilePaths:
    # gl.addSecondsColumn(filePath)

    # replace spaces with underscores
    for filePath in cleanFilepaths:
        gl.replaceSpaces(filePath)


if __name__ == "__main__":
    main()
    
