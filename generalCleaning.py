import pandas as pd
from datetime import datetime
from datetime import timedelta

def saveDFasCSV(df, filePath):
    df.to_csv(filePath, index=False)

def csvToDF(filePath):
    return pd.read_csv(filePath)

def time_to_seconds(time_input):
    # Check if the input is a timedelta object
    if isinstance(time_input, timedelta):
        # Directly convert timedelta to total seconds
        total_seconds = time_input.total_seconds()
        return total_seconds
    else:
        # If not a timedelta, try to parse it as a string (original logic)
        try:
            time_str = time_input.strip()  # Strip leading/trailing whitespace
            time_obj = datetime.strptime(time_str, "%H:%M:%S")
            total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
            return total_seconds
        except:
            total_seconds = 0
    try:
        # Assuming time_input might be a string representation of timedelta
        if isinstance(time_input, str):
            # Extract hours, minutes, and seconds from the string
            h, m, s = map(int, time_input.split(' days ')[1].split(':'))
            time_delta = timedelta(hours=h, minutes=m, seconds=s)
            return time_delta.total_seconds()
    except Exception as e:
        total_seconds = 0

    
    return total_seconds

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

    wasFilePath = False 

    if isinstance(df, str):
        wasFilePath = True
        # assume input is a filepath to a csv and convert it to a dataframe
        filepath = df 
        df = pd.read_csv(df)
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
    if not wasFilePath:
        return df
    elif wasFilePath:
        # save as overwriten csv
        df.to_csv(filepath, index=False)

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
            cleanedFilePath = filePath.replace('.csv', '_cleaned.csv')
            df.to_csv(cleanedFilePath, index=False)
    else:
        filePath = filePaths
        df = pd.read_csv(filePath)
        # iter through each column
        for column in df.columns:
            newName = input(f"\nFilepath: {filePath} \nEnter new name for column '{column}': ").strip()
            df = df.rename(columns={column: newName})
        cleanedFilePath = filePath.replace('.csv', '_cleaned.csv')
        df.to_csv(cleanedFilePath, index=False)

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

# given filepath and column will strip percentage sign and make all floats 
def stripPercentage(filePath, columnName):
    df = pd.read_csv(filePath)
    df[columnName] = df[columnName].str.replace('%', '').astype(float) / 100

# fields that are have "--" make null
def replaceDashes(filePath):
    df = pd.read_csv(filePath)
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = df[column].replace('--', None)
    df.to_csv(filePath, index=False)

def shouldBeNull(x):
    if "--" in str(x) and len(x) < 5:
        return None
    elif "--:--:--" in str(x):
        return None
    else: 
        return x

# given list of filepaths, for everyone, any field with "--" will be replaced with None
def fixNulls(filePaths):
    for filePath in filePaths:
        df = pd.read_csv(filePath)
        for column in df.columns:
            if df[column].dtype == 'object':
                df[column] = df[column].apply(shouldBeNull)
        df.to_csv(filePath, index=False)

# given filepath check "instructor" column and makes dummy variable for if there are two instructors
def twoInstructors(filePath):
    df = pd.read_csv(filePath)
    if "instructor" in df.columns:
        df['two_instructors'] = df['instructor'].apply(lambda x: 1 if ';' in x else 0)
        df.to_csv(filePath, index=False)
    elif "Instructor" in df.columns:
        df['two_instructors'] = df['Instructor'].apply(lambda x: 1 if ';' in x else 0)
        df.to_csv(filePath, index=False)
    else:
        print("No column named 'instructor' or 'Instructor' found in the file")

# given filepath and column name, strip % sign and convert to float out of 100
def convertPercentage(filePath, columnName):
    df = pd.read_csv(filePath)
    df[columnName] = df[columnName].apply(lambda x: float(''.join(filter(lambda c: c.isdigit() or c == '.', str(x)))) / 100 if pd.notnull(x) else x)
    df.to_csv(filePath, index=False)

def main():
    pass

if __name__ == "__main__":
    main()