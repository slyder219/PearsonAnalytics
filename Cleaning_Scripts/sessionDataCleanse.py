import pandas as pd
from datetime import datetime
import json 


def sessionDataCleanse():
    # load the data
    df = pd.read_csv('data/SessionData.csv')

    # empty list to store student data
    newData = []

    # iter through each row
    for index, row in df.iterrows():

        # check if we have header table, if so then grab header info 
        if row['Status'] == "	Active":
            data = {
                "StudentID": row["StudentID"],
                "AvgNumLogins": row["AvgNumLogins"].strip(),
                "NumSubmissions": row["NumSubmissions"].strip(),
                "TotalCourseTime": row["TotalCourseTime"].strip(),
                "TotalLogins": row["TotalLogins"].strip(),
                "LastLogin": row["LastLogin"].strip(),
                "EnrollmentDate": row["EnrollmentDate"].strip(),
                "Instructor": row["Instructor"].strip(),
                "Section": row["Section"].strip() }
            
            # add all that data to list 
            newData.append(data)

    # Create a new DataFrame from the list of dictionaries
    new_df = pd.DataFrame(newData)

    # Save the new DataFrame to a CSV file
    new_df.to_csv('Data_Outputs/cleaned_session_data.csv', index=False)       

    return new_df


def addSecondsColumn(cleanedDF):

    df = cleanedDF

    def time_to_seconds(time_str):
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
        return total_seconds

    # Add a new column 'TotalTimeSeconds' to the DataFrame
    df['TotalTimeSeconds'] = df['TotalCourseTime'].apply(time_to_seconds)

    # Convert 'TotalTimeSeconds' column to integer
    df['TotalTimeSeconds'] = df['TotalTimeSeconds'].astype(int)

    # Convert 'TotalLogins' column to integer
    df['TotalLogins'] = df['TotalLogins'].astype(int)

    # Calculate average session time in seconds
    df['AvgSessionSeconds'] = df['TotalTimeSeconds'] / df['TotalLogins']

    # Round the average session time to the nearest whole number
    df['AvgSessionSeconds'] = df['AvgSessionSeconds'].round().astype(int)

    # also make student id, avg logins, and num submissions integers
    # df['StudentID'] = df['StudentID'].astype(int)
    df['AvgNumLogins'] = df['AvgNumLogins'].astype(int)
    df['NumSubmissions'] = df['NumSubmissions'].astype(int)

    # drop any duplicate rows
    df = df.drop_duplicates()

    # copy the df
    df2 = df.copy()

    # map section from json file
    with open("sessionMap.json","r") as file:
        mappingData = json.load(file)
    
    # map section column
    df2['Section'] = df2['Section'].map(mappingData)

    # rename section column to Session
    df2 = df2.rename(columns={'Section': 'Session'})

    # merge the two dataframes
    df = df2 


    # Save the updated DataFrame to a CSV file
    df.to_csv('Data_Outputs/cleaned_session_data.csv', index=False)

def main():
    
    addSecondsColumn(sessionDataCleanse())
  



if __name__ == "__main__":
    main()