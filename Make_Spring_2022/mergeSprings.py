import pandas as pd


def main():

    df1 = pd.read_csv('Spring_2022_Data/Spring22_CapstoneData.csv')
    df2 = pd.read_csv('Spring_2022_Data/Spring22_SessionData.csv')
    df3 = pd.read_csv('Spring_2022_Data/Spring22_studentGradeSesMajor.csv')

    # Merge the DataFrames based on the "StudentID" column
    merged_df = pd.merge(df1, df2, on="StudentID", how="outer")
    merged_df = pd.merge(merged_df, df3, on="StudentID", how="outer")
    
    # drop rows with no numericalGrade or StudentID
    merged_df = merged_df.dropna(subset=['NumericalGrade', 'StudentID'])




    # save 
    merged_df.to_csv('Spring_2022_Data/Spring22_mergedData.csv', index=False)







if __name__ == "__main__":
    main()