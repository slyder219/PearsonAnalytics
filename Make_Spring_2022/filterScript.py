import pandas as pd

# fromat = "Spring 2022" and column = "Session"

def filterSpring(df):
    df = df[df["Session"] == "Spring 2022"]
    return df

def saveToFolder(df, name ):
    df.to_csv(f'Spring_2022_Data/{name}', index=False)

def run():
    df = pd.read_csv('Data_Outputs/cleaned_session_data.csv')
    df = filterSpring(df)
    saveToFolder(df, "Spring22_SessionData.csv")

    df = pd.read_csv('Data_Outputs/cleaned_Grouped_CapstoneData.csv')
    df = filterSpring(df)
    saveToFolder(df, "Spring22_CapstoneData.csv")

    df = pd.read_csv('Data_Outputs/cleaned_studentGradeSesMajor.csv')
    df = filterSpring(df)
    saveToFolder(df, "Spring22_studentGradeSesMajor.csv")



def main():
    run()

if __name__ == "__main__":
    main()