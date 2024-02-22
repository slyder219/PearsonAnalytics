import pandas as pd


def uniqueSession(df, sessionColName):
    # get all unqiue sessions names
    return df[sessionColName].unique()


def printAll():

    print()

    df = pd.read_csv('Data_Outputs/cleaned_studentGradeSesMajor.csv')

    # add unqiues to list
    sessions = []
    sessions.extend(uniqueSession(df, 'Session'))


    print(
        f"Student Grade Major Sheet:\n{uniqueSession(df, 'Session')}\n"
    )

    df = pd.read_csv("Data_Outputs/cleaned_session_data.csv")

    sessions.extend(uniqueSession(df, 'Session'))

    print(
        f"Session Data Sheet:\n{uniqueSession(df, 'Session')}\n"
    )

    df = pd.read_csv("Data_Outputs/cleaned_CapstoneData.csv")

    sessions.extend(uniqueSession(df, 'Course Name'))

    print(
        f"Capstone Data Sheet:\n{uniqueSession(df, 'Course Name')}\n"
    )

    unqiues = list(set(sessions))

    print("Unique Sessions of all:\n")
    for item in unqiues:
        print(item)


def main():
    printAll()

if __name__ == "__main__":
    main()