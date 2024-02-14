import pandas as pd
import json


def cleanse():
    
    df = pd.read_csv('Data/StudentGradeSessionMajor.csv')

    # strip white space where we can 
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # drop rows without studentID
    df = df.dropna(subset=['StudentID'])

    # drop rows without grades
    df = df.dropna(subset=['Official Grade'])

    # drop rows with grades W or Z or E 
    df = df[df['Official Grade'] != 'W']
    df = df[df['Official Grade'] != 'Z']
    df = df[df['Official Grade'] != 'E']

    # Add a binary column for IsSenior (1 if Senior, 0 otherwise)
    df['IsSenior'] = df['Level'].apply(lambda x: 1 if x.lower() == 'senior' else 0)

    # Add a binary column for IsJunior (1 if Junior, 0 otherwise)
    df['IsJunior'] = df['Level'].apply(lambda x: 1 if x.lower() == 'junior' else 0)

    # Add a binary column for IsSophomore (1 if Sophomore, 0 otherwise)
    df['IsSophomore'] = df['Level'].apply(lambda x: 1 if x.lower() == 'sophomore' else 0)

    # binary for if Business Admin major
    df['IsBusinessAdmin'] = df['Program and Plan'].apply(lambda x: 1 if 'Business Administration' in x else 0)

    # add column for numeric scale of letter grades
    # grade map: 
    grade_mapping = {
        'A': 4,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1,
        'D-': 0.7,
        'E': 0
    }

    df['NumericalGrade'] = df['Official Grade'].map(grade_mapping)

    # session mapping
    with open("sessionMap.json","r") as file:
        sessionMap = json.load(file)

    # map section from json file
    df['Session'] = df['Session'].map(sessionMap)

    

    # drop any duplicate rows
    df = df.drop_duplicates()

    # output csv
    df.to_csv('Data_Outputs/cleaned_studentGradeSesMajor.csv', index=False)





def main():
    cleanse()

if __name__ == "__main__":
    main()
