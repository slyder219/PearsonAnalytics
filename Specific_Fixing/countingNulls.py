import pandas as pd


def countNulls(df, column):
    # Count the number of null values in the column
    nulls = df[column].isnull().sum()
    print(
        f"The column '{column}' has {nulls} null values out of {df[column].count()} total rows."
    )





def main():
    sessionData = pd.read_csv('Data_Outputs/cleaned_session_data.csv')

    countNulls(sessionData, "StudentID")
    

if __name__ == "__main__":
    main()