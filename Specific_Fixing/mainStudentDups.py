import pandas as pd

main_students_cleaned = "C:/Users/seanl/Documents/PearsonData/working_data/main_students/main_students_cleaned.csv"

if __name__ == "__main__":
    
    df = pd.read_csv(main_students_cleaned)

    cleaned_df = df.drop_duplicates(subset='studentnum', keep='first')


    # save
    cleaned_df.to_csv(main_students_cleaned, index=False)