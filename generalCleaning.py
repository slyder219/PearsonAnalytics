import pandas as pd
from datetime import datetime

def saveDFasCSV(df, filePath):
    df.to_csv(filePath, index=False)

def csvToDF(filePath):
    return pd.read_csv(filePath)

def time_to_seconds(time_str):
    try:
        time_str = time_str.strip()  # Strip leading/trailing whitespace
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
        return total_seconds
    except:
        return 0

# function to check what type of data is in the column
def checkType(data):
    if data.dtype == 'int64':
        return 'int'
    elif data.dtype == 'float64':
        return 'float'
    elif data.dtype == 'object':
        return 'string'
    else:
        return 'unknown'
    
# function to clean all columns by confirming all data is right type and no whitespace if string
# takes in pandas df and returns cleaned df
def cleanColumns(df):
    # iterate through each column
    for column in df.columns:
        # check if column is string type
        if checkType(df[column]) == 'string':
            # remove any whitespace
            df[column] = df[column].str.strip()
        # check if column is int type
        if checkType(df[column]) == 'int':
            # remove any whitespace
            df[column] = df[column].astype(int, errors='ignore')
        # check if column is float type
        if checkType(df[column]) == 'float':
            # remove any whitespace
            df[column] = df[column].astype(float, errors='ignore')
    # drop any duplicate rows
    df = df.drop_duplicates()
    return df

# iterate through list of filepaths to csvs, clean each and save each as csv it same location with "cleaned" appended to filename
def cleanAllFiles(filePaths):
    cleanedFilePaths = []
    for filePath in filePaths:
        df = pd.read_csv(filePath)
        df = cleanColumns(df)
        cleanedFilePath = filePath.replace('.csv', '_cleaned.csv')
        df.to_csv(cleanedFilePath, index=False)
        cleanedFilePaths.append(cleanedFilePath)
    return cleanedFilePaths

# given list of filepaths to csvs, use input to rename columns and save file with same name to replace 
def renameColumns(filePaths):
    if isinstance(filePaths, list):
        for filePath in filePaths:
            df = pd.read_csv(filePath)
            # iter through each column
            for column in df.columns:
                newName = input(f"\nFilepath: {filePath} \nEnter new name for column '{column}': ").strip()
                df = df.rename(columns={column: newName})
            df.to_csv(filePath, index=False)
    else:
        filePath = filePaths
        df = pd.read_csv(filePath)
        # iter through each column
        for column in df.columns:
            newName = input(f"\nFilepath: {filePath} \nEnter new name for column '{column}': ").strip()
            df = df.rename(columns={column: newName})
        df.to_csv(filePath, index=False)

# given a filpath to a csv that has a column with letter grades (column name given as arg), map to new column with numerical values
def mapGrades(filePath, columnName):
    df = pd.read_csv(filePath)
    # create dictionary to map letter grades to numerical values
    gradeMap = {
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'D-': 0.7,
        'F': 0.0,
        'W': 0.0,
        'E': 0.0,
    }
    # create new column with numerical values
    df['NumericalGrade'] = df[columnName].map(gradeMap)
    df.to_csv(filePath, index=False)
        
# given csv path, for any column that has "time" in the name, add another column with the time in seconds
def addSecondsColumn(filePath):
    df = pd.read_csv(filePath)
    for column in df.columns:
        if 'time' in column.lower():
            df[column + '_seconds'] = df[column].apply(lambda x: time_to_seconds(x) if time_to_seconds(x) != 0 else None)
    df.to_csv(filePath, index=False)


# given csv path, for any column name that has a space, replace with underscore
def replaceSpaces(filePath):
    df = pd.read_csv(filePath)
    for column in df.columns:
        if ' ' in column:
            new_column = column.strip().replace(' ', '_')
            df = df.rename(columns={column: new_column})
    df.to_csv(filePath, index=False)


# replace column "studentnumber" with "StudentNum"
def replaceStudentNum(filePath):
    df = pd.read_csv(filePath)
    df = df.rename(columns={'StudentNumber': 'StudentNum'})
    df.to_csv(filePath, index=False)

# given csvpath strip leading and trailing whitespace from every cell
def stripWhitespace(filePath):
    df = pd.read_csv(filePath)
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = df[column].str.strip()
    df.to_csv(filePath, index=False)


def main():
    pass

if __name__ == "__main__":
    main()