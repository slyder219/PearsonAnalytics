import pandas as pd


def uniqueSession(df, sessionColName):
    # get all unqiue sessions names
    return df[sessionColName].unique()


def printAll(filepaths):
    sessions = []

    for filepath in filepaths:
        df = pd.read_csv(filepath)
        sessions.extend(uniqueSession(df, 'Session'))

        print(f"{filepath}:\n{uniqueSession(df, 'Session')}\n")

    unqiues = list(set(sessions))

    print("Unique Sessions of all:\n")
    for item in unqiues:
        print(item)

filepaths = [
    "C:/Users/seanl/Documents/PearsonData/Activity_report_trainings/Activity_report_trainings_cleaned.csv",
    "C:/Users/seanl/Documents/PearsonData/Activity_report_with_student/Activity_report_with_student_cleaned.csv", 
    "C:/Users/seanl/Documents/PearsonData/Number_of_logins_per_student/cleaned_number_of_logins.csv", 
    "C:/Users/seanl/Documents/PearsonData/student_info_ids/student_info_ids_cleaned.csv"
]

def main():
    printAll(filepaths)

if __name__ == "__main__":
    main()