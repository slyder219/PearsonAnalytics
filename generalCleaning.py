import pandas as pd

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
            df[column] = df[column].astype(int)
        # check if column is float type
        if checkType(df[column]) == 'float':
            # remove any whitespace
            df[column] = df[column].astype(float)
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
    for filePath in filePaths:
        df = pd.read_csv(filePath)
        # iter through each column
        for column in df.columns:
            newName = input(f"\nFilepath: {filePath} \nEnter new name for column '{column}': ").strip()
            df = df.rename(columns={column: newName})
        df.to_csv(filePath, index=False)
        



def main():
    pass

if __name__ == "__main__":
    main()